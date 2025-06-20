# models/forecasting_models.py

import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
import random

class ForecastingEngine:
    def __init__(self):
        self.model = self._train_ml_model()

    def _train_ml_model(self):
        """Train an XGBoost model for deal scoring"""
        X, y = self._generate_training_data()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = XGBClassifier(
            n_estimators=100,
            max_depth=3,
            learning_rate=0.1,
            eval_metric="logloss"
        )
        model.fit(X_train, y_train)

        # Evaluate model
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
        print(f"🧠 ML Model Accuracy: {accuracy:.2f}, ROC-AUC: {auc:.2f}")

        return model

    def _generate_training_data(self):
        """Generate synthetic training data for deal scoring"""
        X = []
        y = []

        for _ in range(1000):
            channel = random.choice(["google", "linkedin", "email", "content", "direct"])
            rep = random.choice(["Rep A", "Rep B", "Rep C", "Rep D"])
            touchpoints = random.randint(1, 6)
            deal_age = random.randint(30, 180)
            deal_value = random.uniform(10_000, 500_000)
            converted = random.random() > 0.5

            feature_vector = [
                touchpoints,
                deal_age,
                {"google": 0.8, "linkedin": 0.5, "email": 0.3, "content": 0.2, "direct": 0.65}[channel],
                {"Rep A": 0.9, "Rep B": 0.7, "Rep C": 0.4, "Rep D": 0.25}[rep],
                deal_value
            ]

            X.append(feature_vector)
            y.append(int(converted))

        return np.array(X), np.array(y)

    def deal_probability_scoring(self, journeys: list):
        """Score deals using trained XGBoost model"""
        results = []
        for j in journeys:
            feature_vector = [
                j["touchpoints"],
                j["deal_age"],
                {"google": 0.8, "linkedin": 0.5, "email": 0.3, "content": 0.2, "direct": 
0.65}.get(j["channel"], 0.5),
                {"Rep A": 0.9, "Rep B": 0.7, "Rep C": 0.4, "Rep D": 0.25}.get(j.get("rep", "Rep A"), 
0.7),
                j["amount"]
            ]

            predicted_prob = self.model.predict_proba([feature_vector])[0][1]
            results.append({
                "deal_id": j["deal_id"],
                "probability": max(0.05, min(0.95, predicted_prob)),
                "rep": j.get("rep", "Rep A"),
                "channel": j["channel"]
            })

        return results

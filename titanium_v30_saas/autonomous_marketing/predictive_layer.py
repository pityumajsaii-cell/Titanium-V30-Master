import random
import numpy as np

class PredictiveLayer:
    def __init__(self):
        self.history = []

    def log_campaign_result(self, revenue, engagement):
        self.history.append((revenue, engagement))
        if len(self.history) > 50:
            self.history.pop(0)

    def predict_best_segment(self):
        # AI predikció a legjövedelmezőbb szegmensre
        if not self.history:
            return random.randint(1, 1000)
        revenues = np.array([r for r,_ in self.history])
        engagements = np.array([e for _,e in self.history])
        scores = revenues * 0.7 + engagements * 0.3
        top_index = np.argmax(scores)
        return top_index  # egyszerű szegmens index (helyettesíthető valós felhasználói adatbázissal)

predictive_ai = PredictiveLayer()

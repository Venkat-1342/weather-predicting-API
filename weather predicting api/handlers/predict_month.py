import tornado.web
import json

class PredictMonthHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            days = int(self.get_query_argument("days", 30))
            if days > 31 or days < 1:
                raise ValueError("days must be between 1 and 31")

            predictions = []
            for day in range(1, days + 1):
                # Dummy temperature logic instead of model prediction
                temp = 20 + (day % 10)
                predictions.append({
                    "day": day,
                    "predicted_temperature": temp
                })

            self.set_header("Content-Type", "application/json")
            self.write(json.dumps({"month_predictions": predictions}))
        except Exception as e:
            self.set_status(400)
            self.write({"error": str(e)})

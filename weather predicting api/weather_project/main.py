# main.py

import tornado.ioloop
import tornado.web
from handlers.predict_month import PredictMonthHandler



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("✅ Welcome to the Tornado Weather API!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/predict-month", PredictMonthHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8858)
    print("🚀 Server running at http://127.0.0.1:8858")
    tornado.ioloop.IOLoop.current().start()

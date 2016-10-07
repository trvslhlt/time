from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def epochTime():
    return '<h1>' + str(int(time.time())) + '</h1>'

if __name__ == '__main__':
    app.run()


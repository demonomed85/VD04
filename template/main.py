from flask import Flask
import datetime as dt

app = Flask(__name__)

@app.route("/")
def hello_world():
    current_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time

if __name__ == "__main__":
    app.run(debug=True)
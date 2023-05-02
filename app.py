from flask import Flask, render_template, jsonify
from database import load_trips_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
  trips = load_trips_from_db()
  return render_template('home.html', trips=trips)

@app.route("/api/trips")
def list_trips():
  trips = load_trips_from_db()
  return jsonify(trips)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
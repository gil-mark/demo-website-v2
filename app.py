from flask import Flask, render_template, jsonify
from database import load_trips_from_db

app = Flask(__name__)

TRIPS = [
  {
    'id': 1,
    'title': 'Annapurna Circuit',
    'country': 'Nepal',
    'cost': 5000
  },
  {
    'id': 2,
    'title': 'England Bike Tour',
    'country': 'United Kingdom',
    'cost': 5000
  },
  {
    'id': 3,
    'title': 'Portugal Digital Nomad',
    'country': 'Portugal',
    'cost': 3000
  }
]


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
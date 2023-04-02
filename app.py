from flask import Flask, render_template

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
  return render_template('home.html', trips=TRIPS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
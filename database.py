from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string, connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

def load_trips_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from trips;"))
    results_all = result.all()
    trips = []
    for row in results_all:
      trips.append(
        {
          "id": row[0],
          "title": row[1],
          "country": row[2],
          "cost": row[3],
          "currency": row[4],
          "activities": row[5],
          "requirements": row[6]
        }
      )
    return trips

from sqlalchemy import create_engine, text

QUERY_FLIGHT_BY_ID = "SELECT flights.*, airlines.airline, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY FROM flights JOIN airlines ON flights.airline = airlines.id WHERE flights.ID = :id"
QUERY_FLIGHT_BY_DATE = "SELECT flights.*, airlines.airline, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY FROM flights JOIN airlines ON flights.airline = airlines.id WHERE flights.DAY = :day AND flights.MONTH = :month AND flights.YEAR = :year"
QUERY_DELAYED_FLIGHTS_BY_AIRPORT = "SELECT flights.*, airlines.airline, airports.AIRPORT, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY AS DELAY FROM flights JOIN airlines ON flights.airline = airlines.id JOIN airports ON flights.ORIGIN_AIRPORT = airports.IATA_CODE WHERE airports.IATA_CODE = :IATA_CODE AND flights.DEPARTURE_DELAY > 20 AND flights.DEPARTURE_DELAY IS NOT NULL"
QUERY_DELAYED_FLIGHTS_BY_AIRLINE =  "SELECT flights.*, airlines.airline, airports.AIRPORT, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY AS DELAY FROM flights JOIN airlines ON flights.airline = airlines.id JOIN airports ON flights.ORIGIN_AIRPORT = airports.IATA_CODE WHERE airlines.AIRLINE LIKE :AIRLINE AND flights.DEPARTURE_DELAY > 20 AND flights.DEPARTURE_DELAY IS NOT NULL"

# Define the database URL
DATABASE_URL = "sqlite:///data/flights.sqlite3"

# Create the engine
engine = create_engine(DATABASE_URL)


def execute_query(query, params):
    """
    Execute an SQL query with the params provided in a dictionary,
    and returns a list of records (dictionary-like objects).
    If an exception was raised, print the error, and return an empty list.
    """
    try:
        with engine.connect() as conn:
            results = conn.execute(text(query), params)
            rows = results.fetchall()
            return rows

    except Exception as e:
        print("Query error:", e)
        return []


def get_flight_by_id(flight_id):
    """
    Searches for flight details using flight ID.
    If the flight was found, returns a list with a single record.
    """
    params = {'id': flight_id}
    return execute_query(QUERY_FLIGHT_BY_ID, params)

def get_flights_by_date(day, month, year):
    """
    Searches for flight details using flight date.
    If the flight was found, returns a list with a single record.
    """
    params = {'day': day,
              'month' : month,
              'year' : year}
    return execute_query(QUERY_FLIGHT_BY_DATE, params)

def get_delayed_flights_by_airport(iata_code):
    """
    Searches for flight details using airport IATA_CODE.
    If the flight was found, returns a list with a single record.
    """
    params = {'IATA_CODE': iata_code}
    return execute_query(QUERY_DELAYED_FLIGHTS_BY_AIRPORT, params)

def get_delayed_flights_by_airline(airline):
    """
    Searches for flight details using airline name.
    If the flight was found, returns a list with a single record.
    """
    params = {'AIRLINE': f"%{airline}%"}
    return execute_query(QUERY_DELAYED_FLIGHTS_BY_AIRLINE, params)
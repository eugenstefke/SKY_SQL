import csv

def csv_export(file_name, flight_data):
    """
    Check if is the flight_data a list object and is data in flight_data
    Where yes format the flight_data to a dict-object and write the data to a csv file
    """
    if not isinstance(flight_data, list):
        flight_data = [flight_data]

    if not flight_data:
        print("No Data to export.")
        return

    fieldnames = list(flight_data[0].keys())

    with open(f"{file_name}.csv", "w", encoding="utf-8", newline="") as csvobj:
        writer = csv.DictWriter(csvobj, fieldnames=fieldnames)
        writer.writeheader()
        for row in flight_data:
            writer.writerow(dict(row))
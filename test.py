import csv

inventory_file = "ghcnd-inventory.txt"
stations_file = "ghcnd-stations.txt"

stations = {}

with open(stations_file, "r") as file:
    for line in file:
        station_id = line[0:11].strip()
        station_name = line[38:68].strip()
        stations[station_id] = station_name



with open("prcp_output.csv", "w", newline="") as csvfile:

    writer = csv.writer(csvfile)

   
    writer.writerow(["station_name", "station_id", "variable", "start_year", "end_year"])

  
    with open(inventory_file, "r") as file:
        for line in file:

            station_id = line[0:11].strip()
            variable = line[31:35].strip()
            start_year = line[36:40].strip()
            end_year = line[41:45].strip()

            if variable == "PRCP":

                station_name = stations.get(station_id, "UNKNOWN")

                writer.writerow([
                    station_name,
                    station_id,
                    variable,
                    start_year,
                    end_year
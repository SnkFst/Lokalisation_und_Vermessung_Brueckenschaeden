import csv
from datetime import datetime

def convert_csv(csv_file, start_timestamp, end_timestamp):
    data = []

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cts = float(row['cts'])
            timestamp = datetime.fromisoformat(row['date']).timestamp()
            lat = float(row['GPS (Lat.) [deg]'])
            lon = float(row['GPS (Long.) [deg]'])
            alt = float(row['GPS (Alt.) [m]'])

            data.append({
                'timestamp': timestamp,
                'p_RS_R_x [m]': lat,
                'p_RS_R_y [m]': lon,
                'p_RS_R_z [m]': alt
            })

    interpolated_data = []
    for timestamp in range(int(start_timestamp), int(end_timestamp) + 1):
        interpolated_data.append({
            'timestamp': timestamp,
            'p_RS_R_x [m]': None,
            'p_RS_R_y [m]': None,
            'p_RS_R_z [m]': None
        })

    for row in data:
        timestamp = row['timestamp']
        if start_timestamp <= timestamp <= end_timestamp:
            index = int(timestamp - start_timestamp)
            interpolated_data[index]['p_RS_R_x [m]'] = row['p_RS_R_x [m]']
            interpolated_data[index]['p_RS_R_y [m]'] = row['p_RS_R_y [m]']
            interpolated_data[index]['p_RS_R_z [m]'] = row['p_RS_R_z [m]']

    return interpolated_data

# Provide the path to your CSV file
csv_file_path = 'D:/Masterarbeit/Brücke11/GH010142_HERO8 Black-GPS5.csv'

# Set the desired start and end timestamps for interpolation
start_timestamp = 1683226060.1099999
end_timestamp = 1683226087.1252823

# Call the function to convert and interpolate the data
interpolated_data = convert_csv(csv_file_path, start_timestamp, end_timestamp)

# Write the interpolated data to a new CSV file with the desired headers
output_file_path = 'D:/Masterarbeit/Brücke11/interpolated_data.csv'

fieldnames = ['timestamp', 'p_RS_R_x [m]', 'p_RS_R_y [m]', 'p_RS_R_z [m]']
with open(output_file_path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(interpolated_data)

print("Data converted and written to", output_file_path)
import os
import csv

image_directory = r"D:\Masterarbeit\Brücke11\GH03014\images_selbst_extrahiert"
imu_csv_file = r"D:\Masterarbeit\Brücke11\GH03014\mav0\imu0\data.csv"
output_file = r"D:\Masterarbeit\Brücke11\GH03014\new_timestamps.txt"

# Lese die IMU-Zeitstempel aus der CSV-Datei
imu_timestamps = []
with open(imu_csv_file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Überspringe Header-Zeile
    for row in csv_reader:
        imu_timestamps.append(row[0])

# Sortiere die IMU-Zeitstempel aufsteigend
imu_timestamps.sort()

# Gehe durch alle Bilder im Verzeichnis und passe die Zeitstempel an
for i, filename in enumerate(os.listdir(image_directory)):
    if filename.endswith(".png"):
        image_path = os.path.join(image_directory, filename)
        new_timestamp = imu_timestamps[i*10]  # Benutze den 10., 20., 30. usw. IMU-Zeitstempel
        new_filename = str(new_timestamp) + ".png"
        new_image_path = os.path.join(image_directory, new_filename)
        os.rename(image_path, new_image_path)

        # Schreibe den neuen Zeitstempel in die Ausgabedatei
        with open(output_file, 'a') as outfile:
            outfile.write(str(new_timestamp) + "\n")

print("Die Zeitstempel der Bilder wurden erfolgreich angepasst und die neuen Zeitstempel wurden in der Datei 'new_timestamps.txt' gespeichert.")




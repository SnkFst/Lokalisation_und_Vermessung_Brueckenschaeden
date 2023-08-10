import os

# Pfad zum Verzeichnis mit den Bildern
image_directory = r"D:\Masterarbeit\Brücke11\GH03014\mav0\cam0\data"

# Time Offset (Timeoffset ausrechnen ( IMU Timestamp - IMAGES Timestamp))
time_offset = 441000

#Hier wird von jedem Bild die timeoffset abgezogen

# Lese die Dateinamen der Bilder im Verzeichnis
image_filenames = os.listdir(image_directory)

# Erstelle eine neue Textdatei für die neuen Zeitstempel
output_file = os.path.join(image_directory, "image_timestamps.txt")

with open(output_file, 'w') as f:
    for image_filename in image_filenames:
        # Extrahiere den aktuellen Zeitstempel aus dem Dateinamen
        current_timestamp = int(os.path.splitext(image_filename)[0])

        # Berechne den neuen Zeitstempel mit dem Time Offset
        new_timestamp = current_timestamp + time_offset

        # Passe den Dateinamen mit dem neuen Zeitstempel an
        new_filename = os.path.join(image_directory, f"{new_timestamp}.png")
        os.rename(os.path.join(image_directory, image_filename), new_filename)

        # Schreibe den neuen Zeitstempel in die Textdatei
        f.write(f"{new_timestamp}\n")

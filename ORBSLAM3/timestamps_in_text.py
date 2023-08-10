import csv

def extract_timestamps(input_file, output_file):
    with open(input_file, 'r') as f_input, open(output_file, 'w') as f_output:
        csv_reader = csv.reader(f_input)
        next(csv_reader)  # Überspringe die Header-Zeile

        for row in csv_reader:
            timestamp = row[0].strip()  # Extrahiere den Timestamp (erster Wert)
            f_output.write(timestamp + '\n')  # Schreibe den Timestamp in die Ausgabedatei

# Beispielaufruf der Funktion
input_filename = 'D:/Masterarbeit/Brücke11/GH03014/mav0/cam0/data.csv'  # Name der Eingabedatei
output_filename = 'D:/Masterarbeit/Brücke11/timestamps_gopro.txt'  # Name der Ausgabedatei

extract_timestamps(input_filename, output_filename)

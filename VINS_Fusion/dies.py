# -*- coding: utf-8 -*-import rosbag
import csv

input_file = "datenGPSGoPro.csv"
output_file = "datenGPSGoProRichtig.csv"


# Öffne die Eingabe- und Ausgabedateien
with open(input_file, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    with open(output_file, "wb") as output_csv:
        csv_writer = csv.writer(output_csv)

        # Schreibe die Spaltenüberschriften in die Ausgabedatei
        header = next(csv_reader)
        csv_writer.writerow(header)

        # Iteriere über die Datenzeilen in der Eingabedatei
        for row in csv_reader:
            # Passe die Zahlenlänge an
            timestamp = "{:.7f}".format(float(row[0]))
            p_RS_R_x = "{:.15f}".format(float(row[1]))
            p_RS_R_y = "{:.15f}".format(float(row[2]))
            p_RS_R_z = "{:.15f}".format(float(row[3]))

            # Schreibe die angepasste Zeile in die Ausgabedatei
            csv_writer.writerow([timestamp, p_RS_R_x, p_RS_R_y, p_RS_R_z])

print("Die CSV-Datei wurde erfolgreich angepasst.")





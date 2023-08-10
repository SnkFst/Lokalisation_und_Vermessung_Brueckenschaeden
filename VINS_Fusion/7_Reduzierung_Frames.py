# -*- coding: utf-8 -*-
import rosbag
from sensor_msgs.msg import Image
from geometry_msgs.msg import PointStamped

input_bag = "final2.bag"
output_bag = "reduced_data.bag"
target_frame_rate = 20
target_measurement_rate = 20

# Öffne die Eingabe-Bag-Datei
input_bag = rosbag.Bag(input_bag, "r")

# Ermittle die Gesamtdauer der Aufnahme
start_time = input_bag.get_start_time()
end_time = input_bag.get_end_time()
duration = end_time - start_time

# Zähle die Anzahl der Bilder und Messungen im Eingabe-Bag-Datei
frame_count = 0
measurement_count = 0
for topic, msg, t in input_bag.read_messages():
    if topic == "/cam0/image_raw":
        frame_count += 1
    elif topic == "/leica/position":
        measurement_count += 1

# Berechne die Anzahl der Bilder und Messungen für die gewünschten Raten
target_frame_count = int(target_frame_rate * duration)
target_measurement_count = int(target_measurement_rate * duration)

# Berechne die Schrittweiten
frame_step = int(frame_count / target_frame_count)
measurement_step = int(measurement_count / target_measurement_count)

# Öffne die Ausgabe-Bag-Datei zum Schreiben
output_bag = rosbag.Bag(output_bag, "w")

# Iteriere über die Nachrichten in der Eingabe-Bag-Datei
frame_index = 0
measurement_index = 0
for topic, msg, t in input_bag.read_messages():
    if topic == "/cam0/image_raw":
        # Schreibe das Bild nur, wenn der aktuelle Index ein Vielfaches der Schrittweite ist
        if frame_index % frame_step == 0:
            output_bag.write(topic, msg, t)
        frame_index += 1
    elif topic == "/leica/position":
        # Schreibe die Messung nur, wenn der aktuelle Index ein Vielfaches der Schrittweite ist
        if measurement_index % measurement_step == 0:
            output_bag.write(topic, msg, t)
        measurement_index += 1
    else:
        # Schreibe alle anderen Topics unverändert in die Ausgabe-Bag-Datei
        output_bag.write(topic, msg, t)

# Schließe die Eingabe- und Ausgabe-Bag-Dateien
input_bag.close()
output_bag.close()

print("Reduzierte Bildrate: Ziel = {}, Anzahl der Bilder = {}, Schrittweite = {}".format(target_frame_rate, frame_count, frame_step))
print("Reduzierte Messrate: Ziel = {} Messungen pro Sekunde, Anzahl der Messungen = {}, Schrittweite = {}".format(target_measurement_rate, measurement_count, measurement_step))

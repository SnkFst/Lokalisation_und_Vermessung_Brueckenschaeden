# -*- coding: utf-8 -*-import rosbag
import rosbag
import csv
from std_msgs.msg import Header
from geometry_msgs.msg import PointStamped
import rospy


bag_file = 'new.bag'
new_bag_file = 'final.bag'
csv_file = 'interpolated_data.csv'

# Öffne die Bag-Dateien
bag = rosbag.Bag(bag_file, 'r')
new_bag = rosbag.Bag(new_bag_file, 'w')

# Lese die Daten aus der indexierten Bag-Datei und schreibe sie in die neue Bag-Datei
for topic, msg, t in bag.read_messages():
    new_bag.write(topic, msg, t)

# Schließe die indexierte Bag-Datei
bag.close()

# Füge die CSV-Daten zur neuen Bag-Datei hinzu
with open(csv_file, 'r') as file:
    csv_data = list(csv.reader(file))
    csv_data = csv_data[1:]  # Überspringe die Header-Zeile der CSV-Datei

    # Berechne die Schrittweite für die Timestamps
    start_time = 1683226060.11
    end_time = 1683226087.13
    num_messages = len(csv_data)
    duration = end_time - start_time
    step = duration / num_messages

    # Erstelle eine Nachricht für den neuen PointStamped-Typ
    point_msg = PointStamped()
    point_msg.header = Header()
    point_msg.header.frame_id = 'world'

    # Iteriere über die CSV-Daten und füge sie zur neuen Bag-Datei hinzu
    timestamp = start_time
    for row in csv_data:
        # Aktualisiere den Timestamp in der PointStamped-Nachricht
        point_msg.header.stamp = rospy.Time.from_sec(timestamp)

        # Extrahiere die relevanten Daten aus der CSV-Datei und aktualisiere die PointStamped-Nachricht
        point_msg.point.x = float(row[1])
        point_msg.point.y = float(row[2])
        point_msg.point.z = float(row[3])

        # Schreibe die Nachricht in die neue Bag-Datei
        new_bag.write('/leica/position', point_msg, rospy.Time.from_sec(timestamp))

        # Aktualisiere den Timestamp für die nächste Nachricht
        timestamp += step

# Schließe die neue Bag-Datei
new_bag.close()

print("Die Daten wurden erfolgreich zur neuen Bag-Datei hinzugefügt.")






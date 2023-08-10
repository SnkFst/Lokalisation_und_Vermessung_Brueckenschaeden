# -*- coding: utf-8 -*-
import rosbag
from sensor_msgs.msg import Image

bag_path = 'reduced_data.bag'
image_topic = '/cam0/image_raw'

def get_first_image_timestamp(bag_file, topic):
    with rosbag.Bag(bag_file, 'r') as bag:
        for topic, msg, t in bag.read_messages(topics=[topic]):
            if isinstance(msg, Image):
                return t.to_sec()
    return None

first_timestamp = get_first_image_timestamp(bag_path, image_topic)

if first_timestamp is not None:
    print("Der erste Zeitstempel des ersten Bildes ist:", first_timestamp)
else:
    print("Es wurde kein Bild mit dem angegebenen Topic gefunden.")







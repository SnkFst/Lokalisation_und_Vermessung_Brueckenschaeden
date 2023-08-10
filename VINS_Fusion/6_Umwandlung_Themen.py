# -*- coding: utf-8 -*-import rosbag
import rosbag
from sensor_msgs.msg import CompressedImage, Image, Imu
from cv_bridge import CvBridge

old_bag_filename = 'output.bag'
new_bag_filename = 'new.bag'

bridge = CvBridge()

with rosbag.Bag(new_bag_filename, 'w') as new_bag:
    for topic, msg, t in rosbag.Bag(old_bag_filename).read_messages():
        if topic == '/gopro/image_raw/compressed':
            # Konvertiere die komprimierte Bildnachricht in eine normale Bildnachricht
            image_cv = bridge.compressed_imgmsg_to_cv2(msg)
            image_msg = bridge.cv2_to_imgmsg(image_cv, encoding="bgr8")
            new_bag.write('/cam0/image_raw', image_msg, t)
        elif topic == '/gopro/imu':
            # Schreibe die IMU-Nachricht unverändert in die neue Bag-Datei
            new_bag.write('/imu0', msg, t)
        else:
            # Schreibe andere Nachrichten unverändert in die neue Bag-Datei
            new_bag.write(topic, msg, t)






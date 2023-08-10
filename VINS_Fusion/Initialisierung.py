# -*- coding: utf-8 -*-import rosbag
import rospy
import rosbag
from sensor_msgs.msg import Image, Imu
from geometry_msgs.msg import PointStamped

def process_bag_file(bag_file):
    # Initialisierung des ROS-Nodes
    rospy.init_node('bag_file_initializer')

    # Öffnen der Bag-Datei zum Lesen
    bag = rosbag.Bag(bag_file)

    # Extrahieren und veröffentlichen der IMU-Daten
    imu_publisher = rospy.Publisher('/imu0', Imu, queue_size=10)
    for topic, msg, t in bag.read_messages(topics=['/imu0']):
        imu_publisher.publish(msg)

    # Extrahieren und veröffentlichen der Bildnachrichten
    image_publisher = rospy.Publisher('/cam0/image_raw', Image, queue_size=10)
    for topic, msg, t in bag.read_messages(topics=['/cam0/image_raw']):
        image_publisher.publish(msg)

    # Extrahieren und veröffentlichen der Positionsnachrichten
    position_publisher = rospy.Publisher('/leica/position', PointStamped, queue_size=10)
    for topic, msg, t in bag.read_messages(topics=['/leica/position']):
        position_publisher.publish(msg)

    # Schließen der Bag-Datei
    bag.close()

    # Warten, um sicherzustellen, dass alle Nachrichten veröffentlicht wurden
    rospy.sleep(1)

    # Abschluss der Initialisierung
    rospy.loginfo("Bag-Datei wurde erfolgreich initialisiert.")

if __name__ == '__main__':
    # Pfad zur Bag-Datei
    bag_file_path = 'reduced_data.bag'

    # Aufruf der Funktion zur Verarbeitung der Bag-Datei
    process_bag_file(bag_file_path)






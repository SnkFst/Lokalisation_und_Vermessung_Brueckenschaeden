# -*- coding: utf-8 -*-
import rosbag

input_bag_file = 'reduced_data.bag'
output_bag_file = 'output.bag'

def trim_bag_file(input_file, output_file):
    with rosbag.Bag(output_file, 'w') as output_bag:
        skipped_image_count = 0
        skipped_imu_count = 0

        for topic, msg, t in rosbag.Bag(input_file).read_messages():
            if topic == '/cam0/image_raw' and skipped_image_count < 300:
                skipped_image_count += 1
                continue

            if topic == '/imu0' and skipped_imu_count < 2000:
                skipped_imu_count += 1
                continue

            output_bag.write(topic, msg, t)

    print('Die Bag-Datei wurde gekürzt und als ' + output_bag_file + ' gespeichert.')

trim_bag_file(input_bag_file, output_bag_file)
























import math

# Gegebene Rauschparameter und Gyroskop-Werte
velocity_random_walk_x = 0.00131  # \
velocity_random_walk_y = 0.00146  # m/s/sqrt(s)
velocity_random_walk_z = 0.00195  # m/s/sqrt(s)

bias_instability_x = 0.00057  # m/s^2
bias_instability_y = 0.00055  # m/s^2
bias_instability_z = 0.00089  # m/s^2

accel_random_walk_x = 0.00007  # m/s^2/sqrt(s)
accel_random_walk_y = 0.00024  # m/s^2/sqrt(s)
accel_random_walk_z = 0.00015  # m/s^2/sqrt(s)

angle_random_walk_x = 0.00792  # deg/sqrt(s)
angle_random_walk_y = 0.00618  # deg/sqrt(s)
angle_random_walk_z = 0.00776  # deg/sqrt(s)

gyro_bias_instability_x = 0.00344  # deg/s
gyro_bias_instability_y = 0.00254  # deg/s
gyro_bias_instability_z = 0.00335  # deg/s

gyro_rate_random_walk_x = 0.00159  # deg/s/sqrt(s)
gyro_rate_random_walk_y = 0.00081  # deg/s/sqrt(s)
gyro_rate_random_walk_z = 0.00252  # deg/s/sqrt(s)

# Berechnung des Durchschnitts für X, Y und Z
average_velocity_random_walk = (velocity_random_walk_x + velocity_random_walk_y + velocity_random_walk_z) / 3
average_bias_instability = (bias_instability_x + bias_instability_y + bias_instability_z) / 3
average_accel_random_walk = (accel_random_walk_x + accel_random_walk_y + accel_random_walk_z) / 3
average_angle_random_walk = (angle_random_walk_x + angle_random_walk_y + angle_random_walk_z) / 3
average_gyro_bias_instability = (gyro_bias_instability_x + gyro_bias_instability_y + gyro_bias_instability_z) / 3
average_gyro_rate_random_walk = (gyro_rate_random_walk_x + gyro_rate_random_walk_y + gyro_rate_random_walk_z) / 3

# Umrechnungsfaktoren
seconds_per_hour = 3600
sqrt_seconds_per_hour = math.sqrt(seconds_per_hour)

# Umwandlung der Durchschnittswerte in ROS-Einheiten
IMU_NoiseAcc = (average_bias_instability * seconds_per_hour) / sqrt_seconds_per_hour
IMU_NoiseGyro = (average_gyro_bias_instability * math.pi / 180) / sqrt_seconds_per_hour
IMU_AccWalk = average_accel_random_walk / math.sqrt(sqrt_seconds_per_hour)
IMU_GyroWalk = (average_gyro_rate_random_walk * math.pi / 180) / sqrt_seconds_per_hour

# Ausgabe der Ergebnisse
print("IMU.NoiseAcc:", IMU_NoiseAcc, "# m/s^1.5")
print("IMU.NoiseGyro:", IMU_NoiseGyro, "# rad/s^0.5")
print("IMU.AccWalk:", IMU_AccWalk, "# m/s^2.5")
print("IMU.GyroWalk:", IMU_GyroWalk, "# rad/s^1.5")
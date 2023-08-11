import numpy as np

# Quaternionen aus der Kalibrierung
qx = 0.003484125007881594
qy = 0.7043054668106147
qz = -0.7098874977116727
qw = 0.0011878073377416855

# Gyroskopische Bias-Werte aus der Kalibrierung
tx = -0.0008331068404345478
ty = -0.012470440869083898
tz = 0.0008100328367966275

# Berechnung der Rotationsmatrix
R = np.array([
    [1 - 2*qy**2 - 2*qz**2,    2*qx*qy - 2*qz*qw,     2*qx*qz + 2*qy*qw],
    [2*qx*qy + 2*qz*qw,        1 - 2*qx**2 - 2*qz**2, 2*qy*qz - 2*qx*qw],
    [2*qx*qz - 2*qy*qw,        2*qy*qz + 2*qx*qw,     1 - 2*qx**2 - 2*qy**2]
])

# Berechnung der Translationsmatrix
T = np.array([[tx], [ty], [tz]])

# Berechnung der gesamten Transformationsmatrix
T_cam_to_imu = np.vstack([np.hstack([R, T]), [0, 0, 0, 1]])

# Ausgabe der Transformationsmatrix
print("Transformationsmatrix von Kamera zu IMU im Body Frame:")
print(T_cam_to_imu)

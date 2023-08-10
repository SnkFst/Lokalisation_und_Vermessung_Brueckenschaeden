import numpy as np

# Quaternionen aus der Kalibrierung
qx = 0.0003685587265907647
qy = 0.7050372074026968
qz = -0.7091682269186822
qw = -0.0016811517730929806

# Gyroskopische Bias-Werte aus der Kalibrierung
tx = -0.00013513784741976117
ty = 0.0008855327534372195
tz = -2.356882418094822e-05

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

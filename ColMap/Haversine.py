import math

def haversine(lat1, lon1, lat2, lon2):
    # Konvertiere Breiten- und Längengrade von Grad in Radiant
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Differenzen der Breiten- und Längengrade
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Haversine-Formel
    a = math.sin(delta_lat/2) * math.sin(delta_lat/2) + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon/2) * math.sin(delta_lon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    # Radius der Erde (ca. 6371 km)
    R = 6371

    # Entfernung in Kilometern
    distance_km = R * c

    return distance_km

def haversine_with_altitude(lat1, lon1, alt1, lat2, lon2, alt2):
    # Berechne die Entfernung auf der Erdoberfläche in Kilometern
    distance_km = haversine(lat1, lon1, lat2, lon2)

    # Umrechnung der Höhenkomponente in Meter
    altitude_diff_m = abs(alt2 - alt1)

    # Gesamte Entfernung mit Höhenkomponente in Metern
    distance_m = distance_km * 1000 + altitude_diff_m

    return distance_m

# Beispielaufruf
lat1 = 48.9033415
lon1 = 11.9122401
alt1 = 339.401
lat2 = 48.9033496
lon2 = 11.912239
alt2 = 339.521

distance_meters = haversine_with_altitude(lat1, lon1, alt1, lat2, lon2, alt2)
print(f"Die Entfernung beträgt: {distance_meters:.3f} Meter")


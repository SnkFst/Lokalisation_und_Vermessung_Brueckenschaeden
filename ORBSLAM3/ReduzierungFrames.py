import os

# Pfad zum Verzeichnis mit den Bildern
image_directory = r"D:\Masterarbeit\Brücke11\GH03014\mav0\cam0\data"

# Lese die Dateinamen der Bilder im Verzeichnis
image_filenames = sorted(os.listdir(image_directory))

# Anzahl der Bilder
image_count = len(image_filenames)

# Index des ersten behaltenen Bildes
kept_index = 0

# Anzahl der zu löschenden Bilder pro Muster
delete_count = 2

deleted_count = 0

for i in range(image_count):
    # Behalte das Bild, wenn der Index dem Muster entspricht
    if i % (delete_count + 1) == kept_index:
        continue
    # Lösche das Bild, wenn der Index nicht dem Muster entspricht
    else:
        os.remove(os.path.join(image_directory, image_filenames[i]))
        deleted_count += 1

print(f"{deleted_count} Bilder wurden gelöscht.")


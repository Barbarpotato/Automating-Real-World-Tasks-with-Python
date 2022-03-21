from PIL import Image
from glob import glob
import os

# Note: put this script in images folder
# Iterate through each file in the folder
for file in glob("ic_*"):  # ignore hidden file (images/.DS_Store) from iteration
    image = Image.open(file).convert("RGB")
    path, filename = os.path.split(file)
    filename = os.path.splitext(filename)[0]
    image.rotate(270).resize((128, 128)).save("/opt/icons/{}.jpeg".format(filename))

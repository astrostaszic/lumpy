import datetime
from PIL import Image
import imagehash
import pygame
from lumpy.img.sources.camera import Camera
import time
import csv

screen = pygame.display.set_mode((640, 480))

csvfile = open('names.csv', 'w', newline='')
fieldnames = ['hash', 'datetime']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

try:
    with Camera() as cam:
        while True:
            img = cam.get_image()
            pil_string_image = pygame.image.tostring(img, "RGBA")
            im = Image.frombytes("RGBA", img.get_size(), pil_string_image)
            img_hash = imagehash.average_hash(im, 24)
            date = datetime.datetime.utcnow()
            screen.blit(img, (0, 0))
            pygame.display.flip()
            writer.writerow({'hash': img_hash, 'datetime': date})
            time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    csvfile.close()

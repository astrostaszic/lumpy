import datetime
from PIL import Image
import imagehash
import pygame
from lumpy.img.sources.pygame_camera import PygameCamera
import time
import csv


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __getitem__(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y
        else:
            raise IndexError

    def __repr__(self):
        return str((self.x, self.y))


class GeoPoint(Point):
    """
    GeoPoint has his coordinates order swap, to correspond geographic order
    longitude(W, E) means x
    latitude(N, S) means y
    """

    def __init__(self, lat: float, lon: float):
        super().__init__(lon, lat)
        self.lon = lon
        self.lat = lat


def get_iss_beneath_point():
    """Geographic point beneath satellite"""

    import ephem

    """Always get the latest ISS TLE data from:
    http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html"""
    iss = ephem.readtle('ISS',
                        '1 25544U 98067A   17320.55793759  .00016717  00000-0  10270-3 0  9011',
                        '2 25544  51.6410 358.7368 0004235 119.9366 240.2207 15.54143010  5442',
                        )

    iss.compute()
    return GeoPoint(iss.sublat, iss.sublong)


def main():
    screen = pygame.display.set_mode((640, 640))

    csvfile = open('names.csv', 'w', newline='')
    fieldnames = ['hash', 'datetime', 'lat', 'lon']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    try:
        with PygameCamera(0) as cam:
            while True:
                img = cam.get_image()
                pil_string_image = pygame.image.tostring(img, "RGB")
                im = Image.frombytes("RGB", img.get_size(), pil_string_image)
                img_hash = imagehash.average_hash(im, 24)
                date = datetime.datetime.utcnow()
                location = get_iss_beneath_point()
                screen.blit(img, (0, 0))
                pygame.display.flip()
                im.save('img/{},{},{}.jpg'.format(date, location.lat, location.lon))
                writer.writerow({'hash': img_hash, 'datetime': date, 'lat': location.lat, 'lon': location.lon})
                time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        csvfile.close()

import os
import pygame as pg


def load_images(path, scale=1):
    images = {}
    files = [file for file in os.listdir(path) if file.endswith(".png")]
    for image_name in files:
        name = os.path.splitext(image_name)[0]
        image = pg.image.load(os.path.join(path, image_name)).convert_alpha()
        if scale > 1:
            size = [i * scale for i in image.get_size()]
            image = pg.transform.smoothscale(image, size)
        images[name] = image
    return images


# PATHS
GAME_DIR = os.path.abspath(os.getcwd())
ASSETS_DIR = os.path.join(GAME_DIR, "assets")
MOON_DIR = os.path.join(ASSETS_DIR, "Moon")


# IMAGES
#MOON_IMAGES = load_images(MOON_DIR)
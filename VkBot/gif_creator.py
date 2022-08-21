import glob
import time

from PIL import Image


def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.png")]
    frame_one = frames[0]
    frame_one.save("new.gif", format="GIF", append_images=frames,
                   save_all=True, duration=2000, loop=0, )


if __name__ == "__main__":
    make_gif(r"C:\Users\nonse\PycharmProjects\PetProjects\google_images")


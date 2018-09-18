import os
import glob
from PIL import Image
from PIL.ExifTags import TAGS
import time
import datetime
from preg_weeks_calc import get_weeks
from datetime import datetime
import argparse

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

def process(files):
    for file in files:
        print(file)
        time = get_exif(file)["DateTimeOriginal"]

        time = time.replace(":", "/")
        complex_date = time.split(" ")
        time = time.replace(" ", "_")
        date = complex_date[0]
        date = datetime.strptime(date, "%Y/%m/%d").strftime("%m/%d/%Y")
        weeks = get_weeks(args.last_period,date)
        number = 0
        new_name = weeks+".jpg"
        if new_name == file:
            print(new_name, "already ok")
            continue
        while os.path.exists(new_name):
            number += 1
            new_name = weeks+"_"+str(number)+".jpg"
        os.rename(file, new_name)


if __name__ == "__main__":
    # read command line arguments
    parser = argparse.ArgumentParser(description='This program expects a folder path\
                                                  with photos of pregnancy (belly shots)\
                                                  and calculates how many weeks the person\
                                                  has in those photos renaming the photos with\
                                                  weeks number.')
    parser.add_argument('last_period', help='The date of the first day of your\
                                             last menstruation in MM/DD/YYYY format.')
    parser.add_argument('photos_path', help='Path to folder with pregnant photos that\
                                             you want to rename with weeks of pregancy.')

    args = parser.parse_args()

    os.chdir(args.photos_path)

    files = glob.glob("*.jpg") #TO DO: accept other, e.g. .gif, .png, etc
    process(files)
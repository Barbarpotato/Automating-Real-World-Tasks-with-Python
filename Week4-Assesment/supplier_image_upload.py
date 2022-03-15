import requests
from os import listdir
import platform


def define_platform():
    """calling the nname of the system.if not windows than return false"""
    system_name = platform.system()
    if system_name == "Windows":
        return False


def custom_path(path_file, image):
    if define_platform() == False:
        return path_file + "\\" + image
    else:
        return path_file + "/" + image


def sent_images(url, path_file):
    """received 2 arguments, arg1 is request the url link to posting the file
    second argument is the path file image that we want to post"""
    list_image = listdir(path_file)
    list_filter_img = []

    for img in list_image:
        if img[-4:] == "jpeg":
            list_filter_img.append(img)

    for image in list_filter_img:
        with open(custom_path(path_file, image), "rb") as opened:
            response = requests.post(url, files={"file": opened})

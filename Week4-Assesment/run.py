import json
import os
import requests
import platform


def define_platform():
    """calling the nname of the system.if not windows than return false"""
    system_name = platform.system()
    if system_name == "Windows":
        return False


def custom_path(desc_path, desc):
    if define_platform() == False:
        return desc_path + "\\" + desc
    else:
        return desc_path + "/" + desc


def upload_description(desc_path, img_path, url):
    """received 3 arguments ,arg 1 is to get the path of the description,
    and the second argument is to get the img path file,
    after that we convert all that data to Python object. and sent it to the webserver.
    which is required the url link from arg 3."""
    data = {}
    list_desc = os.listdir(desc_path)
    list_img = os.listdir(img_path)
    list_filter_img = []

    for img in list_img:
        if img[-4:] == "jpeg":
            list_filter_img.append(img)

    for desc, img in zip(list_desc, list_filter_img):
        with open(custom_path(desc_path, desc), "r") as file:
            content = file.read()
            list_content = content.split("\n")[0:3]
            list_content[1] = int(list_content[1].split(" ")[0])
            list_content[2] = list_content[2].replace("Â\xa0", "")
            data["name"] = list_content[0]
            data["weight"] = list_content[1]
            data["description"] = list_content[2]
            data["image_name"] = img
        response = requests.post(url, json=data)

from PIL import Image
from os import listdir
import platform


def define_platform():
    """calling the nname of the system.if not windows than return false"""
    system_name = platform.system()
    if system_name == "Windows":
        return False


def path_custom(img, path_file):
    """customize the directory format, if not windows that use linux format"""
    if define_platform() == False:
        return path_file + "\\" + img
    else:
        return path_file + "/" + img


def path_save(save_path, change_format):
    """Customize the directory format for the save placement."""
    if define_platform() == False:
        return save_path + "\\" + change_format + ".jpeg"
    else:
        return save_path + "/" + change_format + ".jpeg"


def format_image(path_file, save_path):
    """received 2 argument, arg 1 is where the image file comes from,
    arg2 is where the formatted images will be save."""

    list_image = listdir(path_file)
    list_filter_image = []

    for img in list_image:
        if img[-4:] == "tiff":
            list_filter_image.append(img)

    for img in list_filter_image:
        # path_content = path_file + "\\" + img\
        path_content = path_custom(img, path_file)
        image = Image.open(path_content).convert("RGB")
        new_im = image.resize((600, 400))
        change_format = img.split(".")[0]
        # new_im.save(save_path + "\\" + change_format + ".jpeg")
        new_im.save(path_save(save_path, change_format))

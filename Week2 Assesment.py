import os
import requests


def create_dic(list):
    """this function get the list as an argument and return it to dictionary"""
    dic_data = dict()
    key_list = ["title", "name", "date", "feedback"]
    for index in range(0, len(key_list)):
        key_name = key_list[index]
        dic_data[key_name] = list[index]
    return dic_data


def sent_file(dictionary):
    """Post the dictionary in to the website that we need, change the <corpweb-external-IP>
    to the external IP address that have been given."""
    response = requests.post("http://34.136.140.48/feedback/", json=dictionary)
    get_status = response.status_code
    print("Success!") if get_status == 201 else print("The request Not been fulfilled!")


def main():
    """catch the .txt file, and create a list from each file and pass it to create_dic function,
    after pass it to the create function  will form dictionary and this dic will be passed to
    the senf_file functions"""
    path = "/data/feedback"
    list_files = os.listdir(path)
    for num in range(0, len(list_files)):
        file_path = path + "/" + list_files[num]
        with open(file_path, "r") as text:
            data = text.read().rstrip()
            list_data = data.split("\n")
        dic = create_dic(list_data)
        sent_file(dic)


# main()

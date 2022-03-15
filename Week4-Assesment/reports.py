import os
from datetime import date
import platform
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate


def define_platform():
    """calling the nname of the system.if not windows than return false"""
    system_name = platform.system()
    if system_name == "Windows":
        return False


def custom_path(file_path, desc):
    """determine what the os is, if windows that use \\
        otherwise if linux use /"""
    if define_platform() == False:
        return file_path + "\\" + desc
    else:
        return file_path + "/" + desc


def generate_report(save_path, filename, body):
    """build pdf file that needs 3 argument"""
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(custom_path(save_path, filename))
    today = date.today()
    current_date = today.strftime("%B %d, %Y")
    report_title = Paragraph(
        "Processed Update on {}".format(current_date), styles["h1"]
    )
    report_body = Paragraph(body, styles["BodyText"])
    report.build([report_title, report_body])


def main(file_path, save_path, filename):
    """build the body of the pdf and passed it to generate report arguments
    and calling the generate_report function"""
    report_body = ""
    list_desc = os.listdir(file_path)
    for desc in list_desc:
        with open(custom_path(file_path, desc), "r") as file:
            text = file.read()
            list_text = text.split("\n")
            list_text[2] = list_text[2].replace("Â\xa0", "")
            report_body += "<br/><br/>" + "name: {}".format(list_text[0])
            report_body += "<br/>weight: {}".format(list_text[1])
    generate_report(save_path, filename, report_body)


if __name__ == "__main__":
    file_path = "C:\\Users\\Darmawan\\OneDrive\\Documents\\Python\\Files\\Python-Automation\\Week4 Assesment\\descriptions"
    save_path = "C:\\Users\\Darmawan\\Downloads\\img"
    filename = "test.pdf"
    main(file_path, save_path, filename)

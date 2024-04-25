import csv
from reportlab.lib import colors
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4, inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import glob
import collections


def convert(doc_name, url_file, number, year_path, month_path, day_path):
    all = {}
    file_name = glob.glob("database/" + "*.csv")
    with open(file_name[0], encoding="utf8") as worker:
        for item in csv.DictReader(worker, delimiter=','):
            idworker = item["ID сотрудника"]
            name = item["Имя"] + "_" + item["Фамилия"] + "_" + item["Имя отдела"]
            all[idworker] = name
    allworkers = collections.OrderedDict(sorted(all.items()))

    with open('database/' + year_path + "_late/" + month_path + "/report_" + number + ".csv",
              encoding="utf8") as csvfile:
        alldata = []
        for row in csv.DictReader(csvfile, delimiter=','):
            if row['Имя устройства'] == "КПП Кириш 2" or row['Имя устройства'] == "КПП Кириш 1":
                kirishchiqish = 'enter'
            else:
                kirishchiqish = 'exit'
            alldata.append(row["ID сотрудника"] + kirishchiqish)
            alldata.append(row['Время'])

    styles = getSampleStyleSheet()

    def StringGuy(text):
        return f'<font name="DejaVuSerif">{text}</font>'

    def ParagGuy(text, style=styles['Normal']):
        return Paragraph(StringGuy(text), styles['Normal'])

    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'config/DejaVuSerif.ttf', 'UTF-8'))
    document = SimpleDocTemplate("../../Desktop/Kechikish_" + doc_name + ".pdf", pagesize=A4, title=doc_name,
                                 author='kadr')
    base_document = SimpleDocTemplate(url_file + doc_name + ".pdf", pagesize=A4, title=doc_name, author='kadr')
    base_story_info = []
    story_info = []
    url_logo = "config/logo.png"
    image = Image(url_logo, 1 * inch, 1 * inch)
    story_info.append(image)
    base_story_info.append(image)
    story_info.append(ParagGuy(f"{day_path}.{month_path}.{year_path}  {number[8:10]}:{number[10:12]} ҳолатига кўра"))
    base_story_info.append(ParagGuy(f"{day_path}.{month_path}.{year_path}  {number[8:10]}:{number[10:12]} ҳолатига кўра"))
    pdf_table = []

    title = [ParagGuy("Т/р"), ParagGuy("Исм,Фамилия"), ParagGuy("Келган вақти"), ParagGuy("Бўлими"),
             ParagGuy("Тасдиқланди")]
    pdf_table.append(title)

    k = 1
    for key in allworkers:
        data = []
        data.append(allworkers[key])
        for item in range(0, len(alldata), 2):
            if key + "enter" == alldata[item]:
                data.append(alldata[item + 1])
        l = len(data)
        if l > 1:
            hour = int(data[l - 1][11]) * 10 + int(data[l - 1][12])
            minute = int(data[l - 1][14]) * 10 + int(data[l - 1][15])
            if minute < 10:
                minute = "0" + str(minute)
            if (hour == 8 and int(minute) > 0) or (hour > 8):
                person_data = str(data[0])
                person_list = person_data.rsplit('_')
                row = [ParagGuy(k), ParagGuy(f"{person_list[1]} {person_list[0]}"), ParagGuy(f"{hour}:{minute}"),
                       ParagGuy(person_list[2]),
                       ParagGuy("Юз билан")]
                pdf_table.append(row)
                k += 1

    table = Table(pdf_table)

    table.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                               ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                               ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                               ]))
    story_info.append(table)
    base_story_info.append(table)
    base_document.build(base_story_info)
    document.build(story_info)


def convertAbsent(doc_name, url_file, number, year_path, month_path, day_path):
    all = {}
    file_name = glob.glob("database/" + "*.csv")
    with open(file_name[0], encoding="utf8") as worker:
        for item in csv.DictReader(worker, delimiter=','):
            idworker = item["ID сотрудника"]
            name = item["Имя"] + "_" + item["Фамилия"] + "_" + item["Имя отдела"]
            all[idworker] = name
    allworkers = collections.OrderedDict(sorted(all.items()))

    with open('database/' + year_path + "_late/" + month_path + "/report_" + number + ".csv",
              encoding="utf8") as csvfile:
        alldata = []
        for row in csv.DictReader(csvfile, delimiter=','):
            if row['Имя устройства'] == "КПП Кириш 2" or row['Имя устройства'] == "КПП Кириш 1":
                kirishchiqish = 'enter'
            else:
                kirishchiqish = 'exit'
            alldata.append(row["ID сотрудника"] + kirishchiqish)
            alldata.append(row['Время'])

    styles = getSampleStyleSheet()

    def StringGuy(text):
        return f'<font name="DejaVuSerif">{text}</font>'

    def ParagGuy(text, style=styles['Normal']):
        return Paragraph(StringGuy(text), styles['Normal'])

    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'config/DejaVuSerif.ttf', 'UTF-8'))
    document = SimpleDocTemplate("../../Desktop/Kelmadi_" + doc_name + ".pdf", pagesize=A4, title=doc_name,
                                 author='kadr')
    base_document = SimpleDocTemplate(url_file + doc_name + ".pdf", pagesize=A4, title=doc_name, author='kadr')
    base_story_info = []
    story_info = []
    url_logo = "config/logo.png"
    image = Image(url_logo, 1 * inch, 1 * inch)
    story_info.append(image)
    base_story_info.append(image)
    story_info.append(ParagGuy(f"{day_path}.{month_path}.{year_path}  {number[8:10]}:{number[10:12]} ҳолатига кўра"))
    base_story_info.append(ParagGuy(f"{day_path}.{month_path}.{year_path}  {number[8:10]}:{number[10:12]} ҳолатига кўра"))
    pdf_table = []
    title = [ParagGuy("Т/р"), ParagGuy("Исм,Фамилия"), ParagGuy("Бўлими"), ParagGuy("Келган вақти"), ParagGuy("Имзо")]
    pdf_table.append(title)

    k = 1
    for key in allworkers:
        data = []
        data.append(allworkers[key])
        for item in range(0, len(alldata), 2):
            if key + "enter" == alldata[item]:
                data.append(alldata[item + 1])
        l = len(data)
        if l == 1:
            person_data = str(data[0])
            person_list = person_data.rsplit('_')
            row = [ParagGuy(k), ParagGuy(f"{person_list[1]} {person_list[0]}"), ParagGuy(person_list[2])]
            pdf_table.append(row)
            k += 1
    table = Table(pdf_table)
    table.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                               ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                               ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                               ]))
    story_info.append(table)
    base_story_info.append(table)
    base_document.build(base_story_info)
    document.build(story_info)


def convertOntime(doc_name, url_file, number, year_path, month_path, day_path):
    all = {}
    file_name = glob.glob("database/" + "*.csv")
    with open(file_name[0], encoding="utf8") as worker:
        for item in csv.DictReader(worker, delimiter=','):
            idworker = item["ID сотрудника"]
            name = item["Имя"] + "_" + item["Фамилия"] + "_" + item["Имя отдела"]
            all[idworker] = name
    allworkers = collections.OrderedDict(sorted(all.items()))

    with open('database/' + year_path + "_late/" + month_path + "/report_" + number + ".csv",
              encoding="utf8") as csvfile:
        alldata = []
        for row in csv.DictReader(csvfile, delimiter=','):
            if row['Имя устройства'] == "КПП Кириш 2" or row['Имя устройства'] == "КПП Кириш 1":
                kirishchiqish = 'enter'
            else:
                kirishchiqish = 'exit'
            alldata.append(row["ID сотрудника"] + kirishchiqish)
            alldata.append(row['Время'])

    styles = getSampleStyleSheet()

    def StringGuy(text):
        return f'<font name="DejaVuSerif">{text}</font>'

    def ParagGuy(text, style=styles['Normal']):
        return Paragraph(StringGuy(text), styles['Normal'])

    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'config/DejaVuSerif.ttf', 'UTF-8'))
    document = SimpleDocTemplate("../../Desktop/VaqtidaKelish_" + doc_name + ".pdf", pagesize=A4, title=doc_name,
                                 author='kadr')
    base_document = SimpleDocTemplate(url_file + doc_name + ".pdf", pagesize=A4, title=doc_name, author='kadr')
    base_story_info = []
    story_info = []
    url_logo = "config/logo.png"
    image = Image(url_logo, 1 * inch, 1 * inch)
    story_info.append(image)
    base_story_info.append(image)
    story_info.append(ParagGuy(f"{day_path}.{month_path}.{year_path}  {number[8:10]}:{number[10:12]} ҳолатига кўра"))
    base_story_info.append(ParagGuy(f"{day_path}.{month_path}.{year_path}  {number[8:10]}:{number[10:12]} ҳолатига кўра"))
    pdf_table = []

    title = [ParagGuy("Т/р"), ParagGuy("Исм,Фамилия"), ParagGuy("Келган вақти"), ParagGuy("Бўлими"),
             ParagGuy("Тасдикланди")]
    pdf_table.append(title)

    k = 1
    for key in allworkers:
        data = []
        data.append(allworkers[key])
        for item in range(0, len(alldata), 2):
            if key + "enter" == alldata[item]:
                data.append(alldata[item + 1])
        l = len(data)
        if l > 1:
            hour = int(data[l - 1][11]) * 10 + int(data[l - 1][12])
            minute = int(data[l - 1][14]) * 10 + int(data[l - 1][15])
            if minute < 10:
                minute = "0" + str(minute)
            if (hour == 8 and int(minute) == 0) or (hour < 8):
                person_data = str(data[0])
                person_list = person_data.rsplit('_')
                row = [ParagGuy(k), ParagGuy(f"{person_list[1]} {person_list[0]}"), ParagGuy(f"{hour}:{minute}"),
                       ParagGuy(person_list[2]),
                       ParagGuy("Юз билан")]
                pdf_table.append(row)
                k += 1

    table = Table(pdf_table)

    table.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                               ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                               ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                               ]))
    story_info.append(table)
    base_story_info.append(table)
    base_document.build(base_story_info)
    document.build(story_info)

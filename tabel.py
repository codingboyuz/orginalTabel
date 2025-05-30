import calendar
import csv
from reportlab.lib import colors
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4, inch, landscape, A3, A1
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import glob
import collections
import datetime
import os

desktop = os.path.expanduser('~/Desktop')


def tabel(year_path, month_path, number):
    all = {}
    file_name = glob.glob("database/" + "*.csv")
    with open(file_name[0], encoding="utf8") as worker:
        for item in csv.DictReader(worker, delimiter=','):
            idworker = item["ID сотрудника"]

            name = item["Имя"] + " " + item["Фамилия"]
            # + "_" + item["Имя отдела"]
            all[idworker] = name
    allworkers = collections.OrderedDict(sorted(all.items()))

    with open('database/' + year_path + "/" + month_path + "/allreport_" + number + ".csv",
              encoding="utf8") as csvfile:
        alldata = []
        for row in csv.DictReader(csvfile, delimiter=','):
            if (row['Имя устройства'] == "КПП Кириш 2" or row['Имя устройства'] == "КПП Кириш 1") and row[
                'Описание события'] == "Открытие по верификации":
                # kirishchiqish = 'enter'
                alldata.append(row["ID сотрудника"] + 'enter')
                alldata.append(row['Время'])
            elif (row['Имя устройства'] == "КПП Чиқиш 2" or row['Имя устройства'] == "КПП Чиқиш 1") and row[
                'Описание события'] == "Открытие по верификации":
                # kirishchiqish = 'exit'
                alldata.append(row["ID сотрудника"] + 'exit')
                alldata.append(row['Время'])
            # alldata.append(row["ID сотрудника"] + kirishchiqish)
            # alldata.append(row['Время'])
    # print(calendar.weekday(2022,6,6))
    styles = getSampleStyleSheet()

    def StringGuy(text):
        return f'<font name="DejaVuSerif">{text}</font>'

    def ParagGuy(text, style=styles['Normal']):
        return Paragraph(StringGuy(text), styles['Normal'])

    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'config/DejaVuSerif.ttf', 'UTF-8'))
    print("=====================================================================================")
    print(f"{desktop}/Tabel" + ".pdf", )
    document = SimpleDocTemplate(f"{desktop}/Tabel" + ".pdf", pagesize=landscape(A3), title="Tabel", author='kadr')
    print(document)
    # base_document = SimpleDocTemplate(url_file + doc_name + ".pdf", pagesize=A4, title=doc_name, author='kadr')
    # base_story_info = []
    story_info = []
    # url_logo = "config/logo.png"
    # image = Image(url_logo, 1 * inch, 1 * inch)
    # story_info.append(image)
    # base_story_info.append(image)
    # story_info.append(ParagGuy(f"{day_path}.{month_path}.{year_path}  {number[8:10]}:{number[10:12]} ҳолатига кўра"))
    # base_story_info.append(ParagGuy(f"{day_path}.{month_path}.{year_path}  {number[8:10]}:{number[10:12]} ҳолатига кўра"))
    pdf_table = []

    title = [ParagGuy("Т/р"), ParagGuy("Исм,Фамилия"),
             ParagGuy("1"),
             ParagGuy("2"),
             ParagGuy("3"),
             ParagGuy("4"),
             ParagGuy("5"),
             ParagGuy("6"),
             ParagGuy("7"),
             ParagGuy("8"),
             ParagGuy("9"),
             ParagGuy("10"),
             ParagGuy("11"),
             ParagGuy("12"),
             ParagGuy("13"),
             ParagGuy("14"),
             ParagGuy("15"),
             ParagGuy("16"),
             ParagGuy("17"),
             ParagGuy("18"),
             ParagGuy("19"),
             ParagGuy("20"),
             ParagGuy("21"),
             ParagGuy("22"),
             ParagGuy("23"),
             ParagGuy("24"),
             ParagGuy("25"),
             ParagGuy("26"),
             ParagGuy("27"),
             ParagGuy("28"),
             ParagGuy("29"),
             ParagGuy("30"),
             # ParagGuy("31")
             ]

    # sanashni esingdan chiqardingmi

    pdf_table.append(title)

    k = 1
    for key in allworkers:
        dataEnter = []
        dataExit = []
        row = []
        dataEnter.append(allworkers[key])
        dataExit.append(allworkers[key])
        for item in range(0, len(alldata), 2):
            if key + "enter" == alldata[item]:
                dataEnter.append(alldata[item + 1])
                # print(alldata[item + 1][11:20])
                # print(alldata[item + 1][0:10])
            if key + "exit" == alldata[item]:
                dataExit.append(alldata[item + 1])
        print(dataEnter)
        print(dataExit)
        row.append(ParagGuy(k))
        row.append(ParagGuy(allworkers[key]))
        for day in range(1, 31):  # aytilgan sanadan bir kun ko'p olasan
            error = 1
            week = datetime.date(2025, 5, day).weekday()  # oy bu
            # if week == 5 or week == 6:
            #     error = 0
            cometime = "23:59:59"
            outtime = "00:00:01"
            if day < 10:
                d = "0" + str(day)
            else:
                d = str(day)
            validDate = "2025-05-" + d  # bu ham oy
            comecounter = 0
            outcounter = 0
            for search in dataEnter:

                time = search[11:19]
                if search[0:10] == validDate and time < cometime:
                    cometime = time
                    comecounter = comecounter + 1
            for search1 in dataExit:

                time1 = search1[11:19]
                if search1[0:10] == validDate and time1 > outtime:
                    outtime = time1
                    outcounter = outcounter + 1

            if cometime == "23:59:59":
                cometime = "-"
            if outtime == "00:00:01":
                outtime = "-"

            if cometime == '-' and outtime != '-':
                delta = 0
                if int(outtime[0:2]) > 8:
                    delta = int(outtime[0:2]) - 8
                if int(outtime[0:2]) >= 8 and int(outtime[3:5]) > 39:
                    delta = delta + 1

            elif cometime != '-' and outtime == '-':
                delta = 17 - int(cometime[0:2])

            elif cometime != '-' and outtime != '-':

                if (int(outtime[0:2]) < int(cometime[0:2])) or \
                        (int(outtime[0:2]) == int(cometime[0:2]) and int(outtime[3:5]) < int(cometime[3:5])) or \
                        (int(outtime[0:2]) == int(cometime[0:2]) and int(outtime[3:5]) == int(cometime[3:5]) and int(
                            outtime[6:8]) < int(cometime[6:8])):
                    delta = 9
                else:
                    delta = int(outtime[0:2]) - int(cometime[0:2])
                    if int(cometime[3:5]) > 10 and int(cometime[0:2]) >= 8:
                        delta = delta - 1

                    if (int(outtime[3:5])) > 38 and int(outtime[0:2]) - int(cometime[0:2]) != 0:
                        delta = delta + 1


            elif cometime == '-' and outtime == '-':
                delta = 0

            if outtime != '-':
                if comecounter - outcounter >= 1 and comecounter != 1 and int(outtime[0:2]) < 17:
                    delta = 9

                # # bera kimga yordam qilsang kiritasan
                # if allworkers[key] == "" and (
                #         3 <= day <= 7 or 10 <= day <= 14 or 17 <= day <= 20 or 25 <= day <= 28):
                # delta = 9
                # if allworkers[key] == "Илёс Омаров" and (
                #         3 <= day <= 7 or 10 <= day <= 14 or 17 <= day <= 20 or 25 <= day <= 28):
                #     delta = 9
                # if allworkers[key] == "Инъом Аскаров" and (
                #         3 <= day <= 7 or 10 <= day <= 14 or 17 <= day <= 20 or 25 <= day <= 28):
                #     delta = 9
                # if allworkers[key] == "Исломали Қурбонов" and (
                #         3 <= day <= 7 or 10 <= day <= 14 or 17 <= day <= 20 or 25 <= day <= 28):
                #     delta = 9
                # if allworkers[key] == "Манзура Расулова" and (
                #          3 <= day <= 7 or 10 <= day <= 14 or 17 <= day <= 20 or 25 <= day <= 28):
                #      delta = 9
                # if allworkers[key] == "Ҳулкарой Қурбонова" and (
                #          3 <= day <= 7 or 10 <= day <= 14 or 17 <= day <= 20 or 25 <= day <= 28):
                #      delta = 9
                # if allworkers[key] == "Холида Курчиева" and (
                #          3 <= day <= 7 or 10 <= day <= 14 or 17 <= day <= 20 or 25 <= day <= 28):
                #      delta = 9
                # if allworkers[key] == "Орифжон Садиков" and (
                #         3 <= day <= 7 or 10 <= day <= 14 or 17 <= day <= 20 or 25 <= day <= 28):
                #     delta = 9
                # if allworkers[key] == "Ўктам Самиев" and (
                #         3 <= day <= 7 or 10 <= day <= 14 or 17 <= day <= 20 or 25 <= day <= 28):
                #     delta = 9
                # if allworkers[key] == "Каримжон Хатамов" and (
                #         3 <= day <= 7 or 10 <= day <= 14 or 17 <= day <= 20 or 25 <= day <= 28):
                #     delta = 9
                # if allworkers[key] == "Илёс Омаров" and (
                #         3 <= day <= 7 or 10 <= day <= 14 or 17 <= day <= 20 or 25 <= day <= 28):
                #     delta = 9

            if delta > 1:
                delta = int(delta) - 1
                if (delta > 8):
                    delta = 8
            if int(delta) <= 0:
                delta = '-'
            if error == 0:
                delta = '-'
            row.append(ParagGuy(str(delta)))
        pdf_table.append(row)
        k += 1

    table = Table(pdf_table)
    #
    table.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                               ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                               ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                               ]))
    story_info.append(table)

    # base_story_info.append(table)
    # base_document.build(base_story_info)
    document.build(story_info)

import csv
import glob
import os
import shutil
import sys
from PyQt5.QtWidgets import *
import control
from PyQt5 import QtGui
import analiz
import appHoliday
import appMain
import appMonth
import appOtpustBsBalnichniy
import tabel
from romove_folder import remove_folder

path = os.path.expanduser('~/Downloads')  # Yoki kerakli yo'lni kiriting

class DialogApp(QWidget):
    def __init__(self):
        # super().__init__()
        QWidget.__init__(self)
        width = 500
        heigth = 500
        self.setFixedSize(width, heigth)
        self.resize(500, 500)
        self.setWindowIcon(QtGui.QIcon('config/logo.png'))
        self.setWindowTitle("Innovatsiya texnologiyalar markazi MChJ")
        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(50, 50, 50, 50)

        self.refreshWorkers = QPushButton("Ишчиларни янгилаш")
        self.refreshWorkers.clicked.connect(self.get_new_workers)

        self.checkLate = QPushButton("Кеч қолганлар (pdf)")
        self.checkLate.clicked.connect(self.get_checked_late)

        self.checkCome = QPushButton("Келмаганлар (pdf)")
        self.checkCome.clicked.connect(self.get_checked_come)

        self.timeCome = QPushButton("Вақтида келганлар (pdf)")
        self.timeCome.clicked.connect(self.get_checked_timecome)

        self.tabel = QPushButton("Табелни шакллантириш")
        self.tabel.clicked.connect(self.gotonewapplication)
        # self.tabel.clicked.connect(function.runMonth(appMonth.QApplication))



        layout = QVBoxLayout()
        layout.addWidget(self.refreshWorkers)
        layout.addWidget(self.calendar)
        layout.addWidget(self.checkLate)
        layout.addWidget(self.checkCome)
        layout.addWidget(self.timeCome)
        layout.addWidget(self.tabel)
        self.setLayout(layout)

    def run_window(self):
        w = tabel.Window()
        w.show()


    def gotonewapplication(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Tabelni shakllantirish")
        msg.setWindowTitle("Tabelni shakllantirish")
        msg.setWindowIcon(QtGui.QIcon('config/logo.png'))
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        if msg.exec_() == QMessageBox.Ok:
            download_all_files = []

            # Fayllarni olish
            # path = os.path.expanduser('~/Downloads')
            csv_files = glob.glob(os.path.join(path, "*.csv"))
            print(f"csv_file: {csv_files}")

            for file in csv_files:
                file = os.path.normpath(file)
                if os.path.basename(file).startswith("Все события _"):
                    download_all_files.append(file)
                    print(f"download_all_files: {download_all_files}")

                    dir_year = file[29:33]
                    dir_month = file[33:35]
                    path_for_exists = os.path.join("database", dir_year, dir_month)

                    if not os.path.exists(path_for_exists):
                        os.makedirs(path_for_exists)

            for file in download_all_files:
                year = file[29:33]
                month = file[33:35]
                number = file[29:43]

                self.year = year
                self.month = month
                self.number = number

                path_for_saving = os.path.join("database", year, month)
                read_csv_file = os.path.basename(file)
                save_csv_file = f"allreport_{number}.csv"

                if len(os.listdir(path_for_saving)) == 0:
                    with open(os.path.join(path, read_csv_file), 'r', encoding="utf8") as read_file:
                        with open(os.path.join(path_for_saving, save_csv_file), 'w', encoding="utf8") as write_file:
                            next(read_file)
                            for line in read_file:
                                write_file.write(line)
                else:
                    old_csv_files = glob.glob(os.path.join(path_for_saving, "*.csv"))
                    check = True
                    for old_file in old_csv_files:
                        old_file = os.path.basename(old_file)
                        old_year = old_file[27:31]
                        old_month = old_file[31:33]
                        old_number = old_file[27:41]

                        if old_month == month and int(old_number) < int(number):
                            check = False
                            with open(os.path.join(path, read_csv_file), 'r', encoding="utf8") as read_file:
                                with open(os.path.join(path_for_saving, save_csv_file), 'w',
                                          encoding="utf8") as write_file:
                                    next(read_file)
                                    for line in read_file:
                                        write_file.write(line)
                            os.remove(os.path.join(path_for_saving, f"allreport_{old_number}.csv"))
                    if check:
                        with open(os.path.join(path, read_csv_file), 'r', encoding="utf8") as read_file:
                            with open(os.path.join(path_for_saving, save_csv_file), 'w', encoding="utf8") as write_file:
                                next(read_file)
                                for line in read_file:
                                    write_file.write(line)

            # Qo'shimcha funksiya chaqiriladi
            tabel.tabel(self.year, self.month, self.number)


    def get_checked_late(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Kech qolganlar pdf shaklga berilsinmi?")
        msg.setWindowTitle("Kechikish")
        msg.setWindowIcon(QtGui.QIcon('config/logo.png'))
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if (msg.exec_() == 1024):
            download_all_files = []

            csv_files = glob.glob(path + "/*.csv")
            for file in csv_files:
                if file[16:34] == "События за сегодня":
                    download_all_files.append(file)
                    dir_year = file[35:39]
                    dir_month = file[39:41]
                    path_for_exists = "database/" + dir_year + "_late/" + dir_month
                    if not os.path.exists(path_for_exists):
                        os.makedirs(path_for_exists)
            for file in download_all_files:
                year = file[35:39]
                month = file[39:41]
                day = file[41:43]
                number = file[35:49]

                path_for_saving = "database/" + year + "_late/" + month + "/"

                path_for_pdf = "database/pdf_late/" + year + "/" + month + "/"

                read_csv_file = "События за сегодня_" + number + ".csv"

                save_csv_file = "report_" + number + ".csv"

                if (len(os.listdir(path_for_saving)) == 0):
                    with open(path + read_csv_file, 'rb', encoding="utf8") as read_file:
                        with open(path_for_saving + save_csv_file, 'wb', encoding="utf8") as write_file:
                            next(read_file)
                            for line in read_file:
                                write_file.write(line)

                else:
                    old_csv_files = glob.glob(path_for_saving + "*.csv")
                    check = True
                    for old_file in old_csv_files:
                        old_year = old_file[29:33]
                        old_month = old_file[33:35]
                        old_day = old_file[35:37]
                        old_number = old_file[29:43]

                        if old_day == day and int(old_number) < int(number):
                            check = False
                            with open(path + read_csv_file, 'r', encoding="utf8") as read_file:
                                with open(path_for_saving + save_csv_file, 'w', encoding="utf8") as write_file:
                                    next(read_file)
                                    for line in read_file:
                                        write_file.write(line)
                            os.remove(path_for_saving + "report_" + old_number + ".csv")
                            if os.path.exists(path_for_pdf + "pdf_" + old_number + ".pdf"):
                                os.remove(path_for_pdf + "pdf_" + old_number + ".pdf")
                            if os.path.exists(
                                    "database/pdf_absent/" + year + "/" + month + "/pdf_" + old_number + ".pdf"):
                                os.remove("database/pdf_absent/" + year + "/" + month + "/pdf_" + old_number + ".pdf")
                            if os.path.exists(
                                    "database/pdf_ontime/" + year + "/" + month + "/pdf_" + old_number + ".pdf"):
                                os.remove("database/pdf_ontime/" + year + "/" + month + "/pdf_" + old_number + ".pdf")

                    if check:
                        with open(path + read_csv_file, 'r', encoding="utf8") as read_file:
                            with open(path_for_saving + save_csv_file, 'w', encoding="utf8") as write_file:
                                next(read_file)
                                print(read_file)
                                for line in read_file:
                                    write_file.write(line)

            date = self.calendar.selectedDate()
            r_year = date.year()
            r_month = date.month()
            r_day = date.day()
            report_year = str(r_year)
            if len(str(r_month)) == 1:
                report_month = "0" + str(r_month)
            else:
                report_month = str(r_month)
            if len(str(r_day)) == 1:
                report_day = "0" + str(r_day)
            else:
                report_day = str(r_day)

            if os.path.exists("database/" + report_year + "_late") and os.path.exists(
                    "database/" + report_year + "_late/" + report_month):
                report_files = glob.glob("database/" + report_year + "_late/" + report_month + "/*.csv")
                checker = True

                for file in report_files:
                    data_year = file[29:33]
                    data_month = file[33:35]
                    data_day = file[35:37]
                    data_number = file[29:43]
                    if report_year == data_year and report_month == data_month and report_day == data_day:
                        checker = False
                        # print("PDF and save database begin")
                        file_name = "pdf_" + data_number
                        if not os.path.exists("database/pdf_late/" + report_year + "/" + report_month):
                            os.makedirs("database/pdf_late/" + report_year + "/" + report_month)
                        url_file = "database/pdf_late/" + report_year + "/" + report_month + "/"
                        analiz.convert(file_name, url_file, data_number, data_year, data_month, data_day)
                        # print("PDF and save database end")

                if checker:
                    self.message("Ushbu kun uchun ma'lumotlar topilmadi", "Info", QMessageBox.Ok)
            else:
                self.message("Ushbu kun uchun ma'lumotlar topilmadi", "Info", QMessageBox.Ok)

    def get_checked_come(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Kelmaganlar ro'yxati pdf shaklga berilsinmi?")
        msg.setWindowTitle("Kelmaslik")
        msg.setWindowIcon(QtGui.QIcon('config/logo.png'))
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if (msg.exec_() == 1024):
            date = self.calendar.selectedDate()
            r_year = date.year()
            r_month = date.month()
            r_day = date.day()
            report_year = str(r_year)
            if len(str(r_month)) == 1:
                report_month = "0" + str(r_month)
            else:
                report_month = str(r_month)
            if len(str(r_day)) == 1:
                report_day = "0" + str(r_day)
            else:
                report_day = str(r_day)

            if os.path.exists("database/" + report_year + "_late") and os.path.exists(
                    "database/" + report_year + "_late/" + report_month):
                report_files = glob.glob("database/" + report_year + "_late/" + report_month + "/*.csv")
                checker = True

                for file in report_files:
                    data_year = file[29:33]
                    data_month = file[33:35]
                    data_day = file[35:37]
                    data_number = file[29:43]
                    if report_year == data_year and report_month == data_month and report_day == data_day:
                        checker = False
                        # print("PDF and save database nocome begin")
                        file_name = "pdf_" + data_number
                        if not os.path.exists("database/pdf_absent/" + report_year + "/" + report_month):
                            os.makedirs("database/pdf_absent/" + report_year + "/" + report_month)
                        url_file = "database/pdf_absent/" + report_year + "/" + report_month + "/"
                        analiz.convertAbsent(file_name, url_file, data_number, data_year, data_month, data_day)
                        # print("PDF and save database nocome end")

                if checker:
                    self.message("Ushbu kun uchun ma'lumotlar topilmadi", "Info", QMessageBox.Ok)
            else:
                self.message("Ushbu kun uchun ma'lumotlar topilmadi", "Info", QMessageBox.Ok)

    def get_checked_timecome(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Vaqtida kelganlar ro'yxati pdf shaklga berilsinmi?")
        msg.setWindowTitle("Vaqtida kelganlar")
        msg.setWindowIcon(QtGui.QIcon('config/logo.png'))
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if (msg.exec_() == 1024):
            date = self.calendar.selectedDate()
            r_year = date.year()
            r_month = date.month()
            r_day = date.day()
            report_year = str(r_year)
            if len(str(r_month)) == 1:
                report_month = "0" + str(r_month)
            else:
                report_month = str(r_month)
            if len(str(r_day)) == 1:
                report_day = "0" + str(r_day)
            else:
                report_day = str(r_day)

            if os.path.exists("database/" + report_year + "_late") and os.path.exists(
                    "database/" + report_year + "_late/" + report_month):
                report_files = glob.glob("database/" + report_year + "_late/" + report_month + "/*.csv")
                checker = True

                for file in report_files:
                    data_year = file[29:33]
                    data_month = file[33:35]
                    data_day = file[35:37]
                    data_number = file[29:43]
                    if report_year == data_year and report_month == data_month and report_day == data_day:
                        checker = False
                        # print("PDF and save database ontime begin")
                        file_name = "pdf_" + data_number
                        if not os.path.exists("database/pdf_ontime/" + report_year + "/" + report_month):
                            os.makedirs("database/pdf_ontime/" + report_year + "/" + report_month)
                        url_file = "database/pdf_ontime/" + report_year + "/" + report_month + "/"
                        analiz.convertOntime(file_name, url_file, data_number, data_year, data_month, data_day)
                        # print("PDF and save database ontime end")

                if checker:
                    self.message("Ushbu kun uchun ma'lumotlar topilmadi", "Info", QMessageBox.Ok)
            else:
                self.message("Ushbu kun uchun ma'lumotlar topilmadi", "Info", QMessageBox.Ok)

    def get_new_workers(self):
        remove_folder()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Ишчилар рўйхатини янгилайсизми?")
        msg.setWindowTitle("Yangilash")
        msg.setWindowIcon(QtGui.QIcon('config/logo.png'))
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        if (msg.exec_() == QMessageBox.Ok):
            old_path = os.path.join(os.getcwd(), 'database')  # Database yo'lini olish
            old_csv_file = glob.glob(os.path.join(old_path, "*.csv"))
            max_csv = None

            if old_csv_file:
                # Using regular expression to extract only the numeric part
                import re
                max_csv_match = re.search(r'(\d+)', old_csv_file[0])
                if max_csv_match:
                    max_csv = max_csv_match.group()

            path = os.path.expanduser('~/Downloads')  # Foydalanuvchi yuklamalar papkasi
            csv_files = glob.glob(os.path.join(path, "Сотрудник_*.csv"))
            print(f"Downloads papkasidagi CSV fayllar: {csv_files}")

            if not csv_files:
                self.message("Downloads papkasida ham hech qanday 'Сотрудник_*.csv' fayli topilmadi.", "Xato",
                             QMessageBox.Ok)
                return

            for file_name in csv_files:
                files_name = os.path.basename(file_name).split("_")
                if len(files_name) > 1:
                    new_file_number = files_name[1][:14]
                    print(f"Yangi fayl raqami: {new_file_number}")
                    if not max_csv or int(max_csv) < int(new_file_number):
                        max_csv = new_file_number

            if max_csv and old_csv_file and max_csv == old_csv_file[0][17:31]:
                self.message("Ishchilar ro'yxati yangilanmadi. Yangi ro'yxatni yuklang.", "Info", QMessageBox.Ok)
            elif max_csv:
                new_file_name = f"Сотрудник_{max_csv}.csv"
                print(f"Tanlangan yangi fayl: {new_file_name}")

                # Eski faylni o'chirish agar mavjud bo'lsa
                if old_csv_file:
                    delete_file_name = f"workers_{old_csv_file[0][17:31]}.csv"
                    os.remove(os.path.join(old_path, delete_file_name))

                # Yangi faylni saqlash
                update_file_name = f"workers_{max_csv}.csv"
                with open(os.path.join(path, new_file_name), 'r', encoding="utf8") as new_file:
                    with open(os.path.join(old_path, update_file_name), 'w', encoding="utf8") as update_file:
                        next(new_file)  # Birinchi qatorni tashlab o'tkazadi
                        for line in new_file:
                            update_file.write(line)

                self.message("Ishchilar ro'yxati muvaffaqiyatli yangilandi!", "Muvaffaqiyat", QMessageBox.Ok)
            else:
                self.message("Hech qanday mos keluvchi fayl topilmadi.", "Xato", QMessageBox.Ok)

    def message(self, txt, title, button):
        msgInfo = QMessageBox()
        msgInfo.setIcon(QMessageBox.Information)
        msgInfo.setText(txt)
        msgInfo.setWindowTitle(title)
        msgInfo.setWindowIcon(QtGui.QIcon('config/logo.png'))
        msgInfo.setStandardButtons(button)
        msgInfo.exec()


# 90 144 72 24



# def main():
#     app = QApplication(sys.argv)
#     controller = control.Controller()
#     controller.show_main()
#     sys.exit(app.exec_())

if __name__ == '__main__':
    # main()



    # for file in os.listdir(folder_path):
    #     file_path = os.path.join(folder_path, file)
    #
    #     if os.path.isfile(file_path):
    #         os.remove(file_path)  # Faylni o‘chirish
    app = QApplication(sys.argv)
    mainApp = DialogApp()
    mainApp.show()
    app.exec_()

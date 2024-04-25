import MessageBox
import analiz
import appMain
import os, glob


def get_checked_late():
    title = "Kechikish"
    logo_path = "config/logo.png"
    text = "Kech qolganlar pdf shaklga berilsinmi?"
    result = MessageBox.warning(title, text, logo_path).exec_()

    if (result == 1024):
        download_all_files = []
        download_path = '../../Downloads'
        csv_files = glob.glob(download_path + "/*.csv")
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
                with open("../../Downloads/" + read_csv_file, 'rb', encoding="utf8") as read_file:
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
                        with open("../../Downloads/" + read_csv_file, 'r', encoding="utf8") as read_file:
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
                    with open("../../Downloads/" + read_csv_file, 'r', encoding="utf8") as read_file:
                        with open(path_for_saving + save_csv_file, 'w', encoding="utf8") as write_file:
                            next(read_file)
                            for line in read_file:
                                write_file.write(line)

        #muammo boshqa kunlarni belgilasa ham birinchi run qilingan kunni qaytaryapdi
        date = appMain.DialogApp().selectDate()

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
                MessageBox.info("Info", "Ushbu kun uchun ma'lumotlar topilmadi", "config/logo.png")
        else:
            MessageBox.info("Info", "Ushbu kun uchun ma'lumotlar topilmadi", "config/logo.png")

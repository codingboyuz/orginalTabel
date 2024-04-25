import MessageBox
import analiz
import appMain
import os, glob


def get_checked_timecome(self):
    title = "Vaqtida kelganlar"
    logo_path = "config/logo.png"
    text = "Vaqtida kelganlar ro'yxati pdf shaklga berilsinmi?"
    result = MessageBox.warning(title, text, logo_path).exec_()
    if (result == 1024):
        # muammo boshqa kunlarni belgilasa ham birinchi run qilingan kunni qaytaryapdi
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
                    # print("PDF and save database ontime begin")
                    file_name = "pdf_" + data_number
                    if not os.path.exists("database/pdf_ontime/" + report_year + "/" + report_month):
                        os.makedirs("database/pdf_ontime/" + report_year + "/" + report_month)
                    url_file = "database/pdf_ontime/" + report_year + "/" + report_month + "/"
                    analiz.convertOntime(file_name, url_file, data_number, data_year, data_month, data_day)
                    # print("PDF and save database ontime end")

            if checker:
                MessageBox.info("Info", "Ushbu kun uchun ma'lumotlar topilmadi", "config/logo.png")
        else:
            MessageBox.info("Info", "Ushbu kun uchun ma'lumotlar topilmadi", "config/logo.png")

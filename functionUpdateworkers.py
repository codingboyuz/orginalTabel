import MessageBox
import os, glob

def get_new_workers(self):
    title = "Yangilash"
    logo_path = "config/logo.png"
    text = "Ишчилар рўйхатини янгилайсизми?"
    result = MessageBox.warning(title, text, logo_path).exec_()

    if (result == 1024):
        old_path = 'database'
        old_csv_file = glob.glob(old_path + "/*.csv")
        max_csv = old_csv_file[0][17:31]
        path = '../../Downloads'
        csv_files = glob.glob(path + "/*.csv")
        for file_name in csv_files:
            files_name = file_name.rsplit("\\")
            if (files_name[1][:9] == "Сотрудник"):
                new_file_number = files_name[1][10:24]
                if int(max_csv) < int(new_file_number):
                    max_csv = new_file_number
        if (max_csv == old_csv_file[0][17:31]):
            MessageBox.info("Info", "Ishchilar ro'yxati yangilanmadi. Yangi ro'yxatni yuklang.", "config/logo.png")
        else:
            new_file_name = "Сотрудник_" + max_csv + ".csv"
            delete_file_name = "workers_" + old_csv_file[0][17:31] + ".csv"
            os.remove("database/" + delete_file_name)
            update_file_name = "workers_" + max_csv + ".csv"
            with open("../../Downloads/" + new_file_name, 'r', encoding="utf8") as new_file:
                with open("database/" + update_file_name, 'w', encoding="utf8") as update_file:
                    next(new_file)
                    for line in new_file:
                        update_file.write(line)

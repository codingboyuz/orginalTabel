import os, glob

import appMonth

import tabel


def gotonewapplication():
    # Loading progress
    download_all_files = []
    download_path = '../../Downloads'
    csv_files = glob.glob(download_path + "/*.csv")
    for file in csv_files:
        if file[16:29] == "Все события _":
            download_all_files.append(file)
            dir_year = file[29:33]
            dir_month = file[33:35]
            path_for_exists = "database/" + dir_year + "/" + dir_month
            if not os.path.exists(path_for_exists):
                os.makedirs(path_for_exists)

    for file in download_all_files:
        year = file[29:33]
        month = file[33:35]
        number = file[29:43]
        path_for_saving = "database/" + year + "/" + month + "/"
        read_csv_file = "Все события _" + number + ".csv"
        save_csv_file = "allreport_" + number + ".csv"
        if (len(os.listdir(path_for_saving)) == 0):
            with open("../../Downloads/" + read_csv_file, 'r', encoding="utf8") as read_file:
                with open(path_for_saving + save_csv_file, 'w', encoding="utf8") as write_file:
                    next(read_file)
                    for line in read_file:
                        write_file.write(line)
        else:
            old_csv_files = glob.glob(path_for_saving + "*.csv")
            check = True
            for old_file in old_csv_files:
                old_year = old_file[27:31]
                old_month = old_file[31:33]
                old_number = old_file[27:41]

                if old_month == month and int(old_number) < int(number):
                    check = False
                    with open("../../Downloads/" + read_csv_file, 'r', encoding="utf8") as read_file:
                        with open(path_for_saving + save_csv_file, 'w', encoding="utf8") as write_file:
                            next(read_file)
                            for line in read_file:
                                write_file.write(line)
                    os.remove(path_for_saving + "allreport_" + old_number + ".csv")
            if check:
                with open("../../Downloads/" + read_csv_file, 'r', encoding="utf8") as read_file:
                    with open(path_for_saving + save_csv_file, 'w', encoding="utf8") as write_file:
                        next(read_file)
                        for line in read_file:
                            write_file.write(line)
    # print(appMonth.monthApp())
    # print(year)
    # tabel.tabel(year, month, number)
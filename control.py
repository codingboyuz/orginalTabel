import appMonth, appMain, appHoliday, appOtpustBsBalnichniy

class Controller:
    def __int__(self):
        pass
    def show_main(self):
        self.main = appMain.DialogApp()
        self.main.switch_window.connect(self.show_month)
        self.main.show()
    def show_month(self):
        self.month = appMonth.monthApp()
        self.month.switch_window.connect(self.show_holiday)
        self.main.close()
        self.month.show()
    def show_holiday(self, text):
        self.holiday = appHoliday.holidayApp(text)
        self.month.close()
        self.holiday.switch_window.connect(self.show_istisno)
        self.holiday.show()
    def show_istisno(self):
        self.istisno = appOtpustBsBalnichniy.appNocome()
        self.holiday.close()
        self.istisno.switch_window.connect(self.show_main)
        self.istisno.show()
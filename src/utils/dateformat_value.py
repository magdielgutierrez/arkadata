from datetime import datetime

# receive a date and return  date format dd/mm/yyyy 
class DateFormat():
    @classmethod
    def convert_date(self,date):
        return datetime.strftime(date,'%d/%m/%Y')
import datetime

def happy_end(soda):
    print(soda)

def feel_lucky(soda):
    print(soda)
    
    
if datetime.date.today().year < 2019:
    year = happy_end(2018)
else:
    year = feel_lucky(2019)
print(year)
















import datetime

def getDate():
    """Geting date with datetime module"""
    now = datetime.datetime.now()
    print("Now:" + str(now))
    print("Day:" + str(now.day))
    print("Month:" + str(now.month))
    print("Year:" + str(now.year))
    print("Hour:" + str(now.hour))
    print("Minute:" + str(now.minute))
    print("Second:" + str(now.second))
    print("Microsecond:" + str(now.microsecond))
    

getDate()
help(getDate)
import datetime


now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y %H:%M")

if __name__ == '__main__':
    print(date)


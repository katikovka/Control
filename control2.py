# 11. Магическая дата

date = input()


def magic_date(date):
    day = int(date.split(".")[0])
    month = int(date.split(".")[1])
    ear = int(date.split(".")[2])

    if day * month == (ear % 100):
        print("Это магическая дата!")
    else:
        print("Это не магическая дата :(")


magic_date(date)

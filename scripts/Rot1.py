import datetime
import calendar


# from datetime import date, timedelta, datetime

# Получить информацию от пользователя
# Определить день недели для первого числа месяца
# def get_next_dez(dez_week1, dez_week2):
#    return dez


# TODO
# Создать анти-enum для средств

# Создали класс хранения дез.средств
class Dez:
    # Test = "abcd"
    # реализация блокировки повторной инициализации глобальных св-в класса
    # блокировка рекурсивного вызова конструктора
    # dez_inits = False

    # almadez = Dez("almadez", "2.5%", "7%")

    def __init__(self, name, conc_regular, conc_general):
        self.name = name
        self.conc_regular = conc_regular
        self.conc_general = conc_general
        # if not Dez.dez_inits:
        #     Dez.dez_inits = True # блокируем повторный заход на строчку ниже
        # almadez = Dez("almadez", "1.5%", "2.5%")
        # teflex = Dez("teflex", "1%", "2%")
        # peroxide = Dez("peroxide", "3%", "6%")

    # def dezinfectants(self):
    #     Dez.almadez = Dez("almadez", "1.5%", "2.5%")
    #     Dez.teflex = Dez("teflex", "1%", "2%")
    #     Dez.peroxide = Dez("peroxide", "3%", "6%")

    # Дописать остальные средства и концентрации


# d = Dez("Test", "1.5%", "5%")
# alm = Dez.almadez
# s = Dez.Test
# Dez.Test = "xyz"
almadez = Dez("Алмадез", "1.5%", "2.5%")
teflex = Dez("Тефлекс", "1%", "2%")
peroxide = Dez("Перекись водорода + Прогресс", "3%", "6%")

dict_dez = {"a": almadez, "t": teflex, "p": peroxide}


# print(almadez.conc_general)

# i = 1


def get_next(prev, cur):
    if prev == almadez and cur == peroxide:
        return teflex
    elif prev == teflex and cur == peroxide:
        return almadez
    elif prev == peroxide and (cur == teflex or cur == almadez):
        return peroxide


# x = get_next(almadez, b)
# y = get_next(x, a)

def get_week_day(year_cur, cur_month, day):
    # workdate = datetime.datetime.strptime(str(cur_date), "%Y-%m-%d").date()
    # day = calendar.day_name[workdate.weekday()]  # return number!
    return calendar.weekday(year_cur, cur_month, day)


# def days_cur_month():
#     m = datetime.now().month
#     y = datetime.now().year
#     ndays = (date(y, m + 1, 1) - date(y, m, 1)).days
#     d1 = date(y, m, 1)
#     d2 = date(y, m, ndays)
#     delta = d2 - d1
#
#     return [(d1 + timedelta(days=i)).strftime('%d.%m.%Y') for i in range(delta.days + 1)]

def days_cur_month(year_cur, cur_month):
    # сделать автоматический рассчет last_day
    last_day = calendar.monthrange(year_cur, cur_month)[1]
    d1 = datetime.date(year_cur, cur_month, 1)
    d2 = datetime.date(year_cur, cur_month, last_day)
    days = [d1 + datetime.timedelta(days=x) for x in range((d2 - d1).days + 1)]

    # all_days_mounth = []

    # for day in days:
    #    all_days_mounth.append(day.strftime('%d.%m.%Y'))

    return days  # all_days_mounth


def generate_dez_list(all_days, prev, cur):
    # цикл по всем дням из days (обходим все дни месяца)
    for day in all_days:
        # определяем день недели для текущего дня
        temp_day = get_week_day(int(day.strftime('%Y')), int(day.strftime('%m')), int(day.strftime('%d')))
        # Если день недели - понедельник:
        if temp_day == 0:
            # меняем средство cur
            temp_dez = get_next(prev, cur)
            # а то, которое было cur, переносим в prev
            prev = cur
            cur = temp_dez

            print(day.strftime('%d.%m.%Y') + "\t " + cur.name + "\t " + cur.conc_general)
        else:
            print(day.strftime('%d.%m.%Y') + "\t " + cur.name + "\t " + "\t " + cur.conc_regular)


all_days = days_cur_month(year_cur=int(input()), cur_month=int(input()))

# вызвать функцию
generate_dez_list(all_days, prev=dict_dez[input()], cur=dict_dez[input()])

# temp_dez = get_next(prev=dict[input()], cur=dict[input()])
# temp_day = get_week_day(cur_date=input())
# list_of_date = list()
# list_of_date.append(temp_dez.name)
# list_of_date.append(temp_day)
# print(list_of_date)
# i = 100
# for day in all_days:
#     #    all_days_mounth.append(day.strftime('%d.%m.%Y'))
#     print(day.strftime('%d.%m.%Y')+" "+str(i))

# -*- coding: utf-8 -*-
__date__ = '2020/2/22 15:51'

# codeup1928

def is_leap(year):
    return ((year%4==0 and year%100!=0) or (year%400==0))

months = [
    [0, 0],
    [31, 31], [28, 29],[31, 31], [30, 30],[31, 31], [30, 30],
    [31, 31], [31, 31],[30, 30] ,[31, 31], [30, 30],[31, 31]
]

while True:
    try:
        time1 = input()
        time2 = input()
        if int(time1) > int(time2):
            time1, time2 = time2, time1
        year1, month1, day1 = int(time1[:4]), int(time1[4:6]), int(time1[6:])
        year2, month2, day2 = int(time2[:4]), int(time2[4:6]), int(time2[6:])
        ans = 1

        while year1<year2 or month1<month2 or day1<day2:
            ans+=1
            day1+=1
            if day1 == months[month1][is_leap(year1)]+1:
                day1=1
                month1+=1
            if month1 == 13:
                month1 = 1
                year1 += 1
        print("相差{}天".format(str(ans)))

    except:
        break
    pass
year=int(input("enter the year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("yes,the year is leap year")
        else:
            ("no,this is not leap year")
    else:
        ("yes,the year is leap year")
else:
    ("this is not leap year")
age=int(input("enter the age"))
sex=input("enter the sex")
if sex=="female" and age>=20 and age<=60:
    print("work only in urban areas")
elif sex=="male" and age>=20 and age<=40:
    print("work in anywhere")
elif sex=="male" and age>=40 and age<=60:
    print("urban areas only")
else:
    print("error")
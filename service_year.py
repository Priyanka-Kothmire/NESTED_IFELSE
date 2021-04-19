salery=int(input("enter the salery"))
service=int(input("enter the year of service"))
bonus=0
if service>5:
    bonus=5/100*salery
    print("net bonus",bonus)
else:
    print("no bonus")


sat= float(input("Saturday's Temp: "))
sun= float(input("Sunday's Temp: "))
mon= float(input("Monday's Temp: "))
tues= float(input("Tuesday's Temp: "))
wed= float(input("Wednesday's Temp: "))
thu= float(input("Thursday's Temp: "))
fri= float(input("Friday's Temp: "))

total=sat+sun+mon+tues+wed+thu+fri
avg=total/7

max_temp=sat
max_day="Saturday"

min_temp=sat
min_day="Saturday"

hotest=0
coldest=0

if sat >=25:
    hotest+=1
elif sat <=10:
    coldest+=1

if sun >=25:
    hotest+=1
elif sun <=10:
    coldest+=1

if mon >=25:
    hotest+=1
elif mon <=10:
    coldest+=1

if tues >=25:
    hotest+=1
elif tues <=10:
    coldest+=1

if wed >=25:
    hotest+=1
elif wed <=10:
    coldest+=1

if thu >=25:
    hotest+=1
elif thu <=10:
    coldest+=1

if fri >=25:
    hotest+=1
elif fri <=10:
    coldest+=1


if max_temp< sun:
    max_temp=sun
    max_day="Sunday"
if max_temp<mon:
    max_temp=mon
    max_day="Monday"
if max_temp<tues:
    max_temp=tues
    max_day="Tuesday"
if max_temp<wed:
    max_temp=wed
    max_day="Wednesday"
if max_temp<thu:
    max_temp=thu
    max_day="Thuresday"
if max_temp<fri:
    max_temp=fri
    max_day="Friday"
    

if min_temp> sun:
    min_temp=sun
    min_day="Sunday"
if min_temp>mon:
    min_temp=mon
    min_day="Monday"
if min_temp>tues:
    min_temp=tues
    min_day="Tuesday"
if min_temp>wed:
    min_temp=wed
    min_day="Wednesday"
if min_temp>thu:
    min_temp=thu
    min_day="Thuresday"
if min_temp>fri:
    min_temp=fri
    min_day="Friday"
    
print("******************************************")
print(f"the avarge temp this week is: {avg}")
print(f"the max temp is: {max_temp} on: {max_day}")
print(f"the min temp is: {min_temp} on: {min_day}")
print(f"number of hot days: {hotest}")
print(f"number of cold days: {coldest}")
print("******************************************")
x= int(input("enter number between 1-99: "))
n1=" "
n2=" "

if 1>x or x>99:
    print("رقم خاطيء")

else:    
    while x!=0:
        if 1<=x<=99 : 
            if x>=90:
                print("90")
                x-=90
                n2="تسعون"
            elif x>=80:
                print("80")
                x-=80
                n2="ثمانون"
            elif x>=70:
                print("70")
                x-=70
                n2="سبعون"
            elif x>=60:
                print("60")
                x-=60
                n2="ستون"
            elif x>=50:
                print("50")
                x-=50
                n2="خمسون"
            elif x>=40:
                print("40")
                x-=40
                n2="اربعون"
            elif x>=30:
                print("30")
                x-=30
                n2="ثلاثون"
            elif x>=20:
                print("20")
                x-=20
                n2="عشرون"
            elif x>=10:
                print("10")
                x-=10
                n2="عشر"
            else:
                if x==9:
                    print("9")
                    x-=9
                    n1="تسعة"
                elif x==8:
                    print("8")
                    x-=8
                    n1="ثمانية"
                elif x==7:
                    print("7")
                    x-=7
                    n1="سبعة"
                elif x==6:
                    print("6")
                    x-=6
                    n1="ستة"
                elif x==5:
                    print("5")
                    x-=5
                    n1="خمسة"
                elif x==4:
                    print("4")
                    x-=4
                    n1="اربعة"
                elif x==3:
                    print("3")
                    x-=3
                    n1="ثلاثة"
                elif x==2:
                    print("2")
                    x-=2
                    n1="اثنان"
                elif x==1:
                    print("1")
                    x-=1
                    n1="واحد"
                             
          
    print(f"الرقم هو: {n2}و{n1}")
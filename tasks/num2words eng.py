while True:
    print("**********************************************************")
    x= int(input("enter number between 1-99, (0 for exit) :"))
    n1=""
    n2=""

    if 0>x or x>99:
        print("wrong number")
    else: 
        if x==0:
            break
        else:   
            while x!=0:
                if 1<=x<=99 : 
                    if x>=90:
                        x-=90
                        n2="Ninety"
                    elif x>=80:
                        x-=80
                        n2="Eighty"
                    elif x>=70:
                        x-=70
                        n2="Seventy"
                    elif x>=60:
                        x-=60
                        n2="Sixty"
                    elif x>=50:
                        x-=50
                        n2="Fifty"
                    elif x>=40:
                        x-=40
                        n2="Forty"
                    elif x>=30:
                        x-=30
                        n2="Thirty"
                    elif x>=20:
                        x-=20
                        n2="Twenty"
                    elif x==19:
                        x-=19
                        n2="Nineteen"
                    elif x==18:
                        x-=18
                        n2="Eighteen"
                    elif x==17:
                        x-=17
                        n2="Seventeen"
                    elif x==16:
                        x-=16
                        n2="Sixteen"
                    elif x==15:
                        x-=15
                        n2="Fifeteen"
                    elif x==14:
                        x-=14
                        n2="Fourteen"
                    elif x==13:
                        x-=13
                        n2="Thirteen"
                    elif x==12:
                        x-=12
                        n2="Twelve"
                    elif x==11:
                        x-=11
                        n2="Eleven"
                    elif x==10:
                        x-=10
                        n2="Ten"
                    else:
                        if x==9:
                            x-=9
                            n1="Nine"
                        elif x==8:
                            x-=8
                            n1="Eight"
                        elif x==7:
                            x-=7
                            n1="Seven"
                        elif x==6:
                            x-=6
                            n1="Six"
                        elif x==5:
                            x-=5
                            n1="Five"
                        elif x==4:
                            x-=4
                            n1="Four"
                        elif x==3:
                            x-=3
                            n1="Three"
                        elif x==2:
                            x-=2
                            n1="Two"
                        elif x==1:
                            x-=1
                            n1="One"
            print(f"your number is: {n2} {n1}")

print("**********************************************************")                                    
print("Thank You :)")
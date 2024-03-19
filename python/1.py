a=int(input("Enter the   first subject mark  :"))
b=int(input("Enter the  second subject mark  :"))
c=int(input("Enter the  third subjectn mark"))
d=int(input("Enter the  fourth subject mark"))
e=a+b+c+d
print(e,"Sum   :")
f=e/4
print(f,"Average  :")
g=e*100/400
print(g,"Percentage  :")
if a>=80:
    print("Grade A")
elif b>=60:
    print("Grade B")
elif c>=40:
    print(" Grade C")
else:
    print("Failed")

name=input("Enter the name of employee:")
salary=eval(input("Enter salary :"))
if salary<=500000:
    tax=0.05*salary
elif salary<=600000:
    tax=0.07*salary
elif salary<=700000:
    tax=0.08*salary
else:
    tax=0.10*salary
print("Name:",name,"salary:",salary,"Tax:",tax)
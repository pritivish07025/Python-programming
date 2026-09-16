# taking user input and print its absolute value 
num=eval(input("Enter number :"))
print('|',num,'| =',(-num if num<0 else num),sep='') 
print("1. Calculate area of a square:")
print("2. Calculate area of ractangle :")
choice=int(input("Enter your choice (1 or 2):"))
if(choice==1):
  side=(float(input("Enter side of square :")))
  square_area=side*side
  print("Area of the square is :",square_area)
else:
  length=float(input("Enter length :"))
  breadth=float(input("Enter breadth:"))
  ractangle_area=length*breadth
  print("Area of the rectangle is :", ractangle_area)
  

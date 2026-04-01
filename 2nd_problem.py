##Write a Python program that takes the coordinates (x, y) of a point as input and prints out
##  which quadrant it belongs to (1st, 2nd, 3rd, or 4th).

x=int(input("Enter x coordinate:"))
y= int(input("Enter the y coordinate: "))

if x>0 and y>0:
    print("The point is in the 1st quadrant.")
elif x<0 and y>0:   
    print("The point is in the 2nd quadrant.")
elif x<0 and y<0:
    print("The point is in the 3rd quadrant.")
elif x>0 and y<0:
    print("The point is in the 4th quadrant.")
    
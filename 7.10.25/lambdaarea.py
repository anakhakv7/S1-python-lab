area_square = lambda side : side * side
area_rectangle = lambda length,width : length * width
area_triangle = lambda base,height : 1/2*(base*height)
a=int(input("Enter the side length of the square:"))
b=int(input("Enter the length of the rectangle:"))
c=int(input("Enter the width of the rectangle:"))
d=int(input("Enter the base length of the triangle:"))
e=int(input("Enter the height of the triangle:"))
print("Area of square= ",area_square(a))
print("Area of rectangle= ",area_rectangle(b,c))
print("Area of triangle= ",area_triangle(d,e))   


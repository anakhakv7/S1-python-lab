from graphics.rectangle import area, perimeter
from graphics.circle import area as circle_area, perimeter as circle_perimeter
from graphics.threeD_graphics.cuboid import surface_area, volume
from graphics.threeD_graphics.sphere import surface_area as sphere_area, volume as sphere_volume

print("Rectangle area:", area(8, 4))
print("Rectangle perimeter:", perimeter(8, 4))

print("Circle area:", circle_area(6))
print("Circle perimeter:", circle_perimeter(6))

print("Cuboid surface area:", surface_area(2, 3, 4))
print("Cuboid volume:", volume(2, 3, 4))

print("Sphere surface area:", sphere_area(5))
print("Sphere volume:", sphere_volume(5))

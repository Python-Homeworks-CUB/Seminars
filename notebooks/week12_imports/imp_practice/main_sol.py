# Importing pi and function from math_utils
# Note: importing pi is unnecessary, and it won't save us
from utils.math import pi, area_of_circle

# Importing only the function from science_utils
from utils.science import volume_of_sphere


# Calculate the area of a circle with radius 3
circle_area = area_of_circle(3)

# Calculate the volume of a sphere with radius 3
sphere_volume = volume_of_sphere(3)

print(f"Area of circle: {circle_area}")
print(f"Volume of sphere: {sphere_volume}")

import math


def areaTriangle(num1, num2):
    area = 0.5 * num1 * num2
    return area


def areaCircle(num1):
    area = math.pi * (num1) ** 2
    return area


def volumeCone(num1, num2):
    volume = 0.33333333 * math.pi * num1**2 * num2
    return volume


def volumeSphere(num1):
    volume = 1.33333333 * math.pi * (num1) ** 2
    return volume


def volumeCuboid(num1, num2, num3):
    volume = num1 * num2 * num3
    return volume


baseTriangle = float(raw_input("Enter the base of triangle: "))
heightTriangle = float(raw_input("Enter the height triangle: "))
radiusCone = float(raw_input("Enter the radius of cone: "))
heightCone = float(raw_input("Enter the height of cone: "))
radiusSphere = float(raw_input("Enter the radius of sphere: "))
lengthCuboid = float(raw_input("Enter the length of cuboid: "))
breadthCuboid = float(raw_input("Enter the breadth of cuboid: "))
heightCuboid = float(raw_input("Enter the height of cuboid: "))
radiusCircle = float(raw_input("Enter the radius of circle: "))


areaTriangle = areaTriangle(baseTriangle, heightTriangle)
areaCircle = areaCircle(radiusCircle)
volumeCone = volumeCone(radiusCone, heightCone)
volumeSphere = volumeSphere(radiusSphere)
volumeCuboid = volumeCuboid(lengthCuboid, breadthCuboid, heightCuboid)

print("The area of the triangle is: ", areaTriangle)
print("The area of the circle is: ", areaCircle)
print("The volume of the cone is: ", volumeCone)
print("The volume of the sphere is: ", volumeSphere)
print("The volume of the cuboid is: ", volumeCuboid)

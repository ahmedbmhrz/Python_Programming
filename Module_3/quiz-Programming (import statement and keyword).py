import math

x = float(input("Enter an angle in degrees >"))

AngleDegrees= math.radians(x)

SineValue = math.sin(AngleDegrees)

print(f"The sin of {x} degrees is {SineValue}")
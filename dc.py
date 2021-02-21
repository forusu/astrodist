import math
arcsecs = float(input("Measured angle: "))
star = str(input("Name of the star: "))

AU = 0.000015813           # One astronomical unit in lightyears
def pc (arcsecs):
    pc = 1 / arcsecs
    return pc;

def ly ():
    ly = pc(arcsecs) * 3.261563777
    return ly;


print(star, "is", pc(arcsecs), "parsecs away, or", ly(), "lightyears away")

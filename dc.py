import math
import json

command = []
output = {}
while "n" not in command:

    command = input("Add new stars to index? (y/n): ")
    
    if "y" in command:
            arcsecs = float(input("Measured angle: "))
            star = str(input("Name of the star: "))

            AU = 0.000015813                                        # One astronomical unit in lightyears
            def pc (arcsecs):
                pc = 1 / arcsecs
                return pc;

            def ly ():
                ly = pc(arcsecs) * 3.261563777
                return ly;

            def mt ():
                mt = pc (arcsecs) * 3.085677581e+16
                return mt;

            
            output[star] = []
            output[star].append({
                'star': star,
                'parsecs': pc(arcsecs),
                'lightyears': ly(),
                'meters': mt(),
            })

            print(star, "is", pc(arcsecs), "parsecs away, or", ly(), "lightyears away, or", mt(), "meters away")

            with open("output.json", 'w') as outfile:
                    json.dump(output, outfile, indent=5)


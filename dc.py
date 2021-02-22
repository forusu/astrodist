import math
import json

command = [] # used to mitigate some funky wunky json problems I encountered
output = {} # used for the json dict

while "n" not in command:

    command = input("Add new stars to index? (y/n): ")
    
    if "y" in command:
            print("--------------------------------------------------------")
            arcsecs = float(input("Measured angle: "))
            star = str(input("Name of the star: "))
            
            

            # AU = 0.000015813  Should've been used but not needed with the simpler calculations
            def pc (arcsecs):
                pc = 1 / arcsecs
                return pc;

            # 1 parsec = 3.2 lightyears
            # [*]---* 
            # for each parsec use -
            # for 10 parsecs use =
            def visual ():
                vis = ["(*)"]
                ps = "-"
                ps10 = "="
                star = "*"
                
                parsecs = int(pc(arcsecs))
                if parsecs < 10:
                    for i in range(parsecs):
                        vis.append(ps)
                if parsecs >= 10:
                    for j in range (int(parsecs / 10)):
                        vis.append(ps10)

                vis.append(star)
                s = ''.join(vis)
                return s;

            def ly ():
                ly = pc(arcsecs) * 3.2
                return ly;

            def mt ():
                mt = pc(arcsecs) * 3.085677581e+16
                return mt;

            # Setting up the dictionary for the json output
            output[star] = []
            output[star].append({
                'star': star,
                'parsecs': pc(arcsecs),
                'lightyears': ly(),
                'meters': mt(),
                'visual': visual()
            })
            
            print("--------------------------------------------------------")
            print(star, "is", pc(arcsecs), "parsecs away, or", ly(), "lightyears away, or", mt(), "meters away")
            print("--------------------------------------------------------")
            print("Visualisation: ", visual())

            with open("output.json", 'w') as outfile:
                    json.dump(output, outfile, indent=5)

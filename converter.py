import math

command = []

while "exit" not in command:

    command = input("Which units do you want to convert to arcseconds? (dg/am/mas/mias/exit): ")
    print("--------------------------------------------------------")

    if "dg" in command:

        ui = float(input("Enter amount of degrees you want to convert: "))
        arcs = ui / 3600
        print("--------------------------------------------------------")
        print(ui, "degrees is", arcs, "arcseconds")

    if "am" in command:

        ui = float(input("Enter amount of arcminutes you want to convert: "))
        arcs = ui / 60
        print("--------------------------------------------------------")
        print(ui, "arcminutes is", arcs, "arcseconds")

    if "mas" in command:

        ui = float(input("Enter amount of miliarcseconds you want to convert: "))
        arcs = ui * 0.001
        print("--------------------------------------------------------")
        print(ui, "miliarcseconds is", arcs, "arcseconds")    

    if "mias" in command:

        ui = float(input("Enter amount of microarcseconds you want to convert: "))
        arcs = ui * 0.000001
        print("--------------------------------------------------------")
        print(ui, "degrees is", arcs, "arcseconds")       
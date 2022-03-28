#introducerar progrsmmets funktion samt frågar efter sidorna på rektangeln.
print("Denna aplikation gör ett antal beräkningar på en rektangel/rätblock.")
tidigare_beräkningar = []

#gör en funktion för att lätt kunna loopa tills användaren väljer att sluta
def scen1():
    sida1 = int(input("Ange rektangelns ena sida:"))
    sida2 = int(input("Ange rektangelns andra sida:"))
    #variable som används i while loopen
    x = 1
    #uträkning för att få fram arean på rektangeln som sedan skrivs ut
    area = sida1 * sida2
    print("Rektangeln har sidorna {0} och {1} vilket gör att arean är {2}.".format(sida1, sida2, area))
    #lägger till informationen i en lista
    tidigare_beräkningar.append("Rektangeln har sidorna {0} och {1} vilket gör att arean är {2}".format(sida1, sida2, area))
    tidigare_beräkningar.append("Höjden    |    Volymen")
    tidigare_beräkningar.append("------------------------")

    if sida1 == sida2:
        print("Eftersom bägge sidorna är lika långa så är denna rektangel en kvadrat.")
    else:
        print("eftersom sidorna inte är lika långa är det ett raätblock.")

    #här räknas volymen ut och skrivs ut.
    while True:
        höjd = int(input("vilka höjder vill du ha med 1-10?"))
        if höjd > 11:
            höjd = 11
            break
        elif höjd < 0:
            höjd = 2
            break
        else:
            höjd = höjd + 1
            break

    print("Höjden    |    Volymen")
    print("------------------------")

    while x < höjd:
        volym = x * area
        print("{0:9} | {1:11}".format(x, volym))
        tidigare_beräkningar.append("{0:9} | {1:11}".format(x, volym))
        alla_beräkningar = "\n".join(tidigare_beräkningar)
        x = x + 1

    #Frågar om användaren vill köra igen
    y = input("Vill du köra igen? ja/nej")
    y = y.lower()
    if y == "ja":
        scen1()
    else:
        print("Här är dina tidigare beräkningar")
        print(alla_beräkningar)

scen1()

#introducerar progrsmmets funktion samt frågar efter sidorna på rektangeln.
print("Denna aplikation gör ett antal beräkningar på en rektangel/rätblock.")
sida1 = int(input("Ange rektangelns ena sida:"))
sida2 = int(input("Ange rektangelns andra sida:"))
#variable som används i while loopen
x = 1
#uträkning för att få fram arean på rektangeln som sedan skrivs ut
area = sida1 * sida2
print("Rektangeln har sidorna {0} och {1} vilket gör att arean är {2}.".format(sida1, sida2, area))
if sida1 == sida2:
    print("Eftersom bägge sidorna är lika långa så är denna rektangel en kvadrat.")
else:
    print("eftersom sidorna inte är lika långa är denna ett rätblock")
print("Höjden    |    Volymen")
print("------------------------")
#här räknas volymen ut och skrivs ut.
while x < 11:
    volym = x * area
    print("{0:9} | {1:11}".format(x, volym))
    x = x +1

bruttolön = float(input("Vad är din bruttolön i hela kronor?\n"))

årslön = bruttolön * 12

if årslön < 19247:
    print("{0:20} {1:12}kr (årslön: {2}kr)".format("månadslön", round(bruttolön), round(årslön)))
    print("{0:20} {1:12}kr".format("kvar efter skatt", round(bruttolön)))
    print("Eftersom du tjänar under brytpunkten betalar du ingen skatt")

elif 19247 < årslön < 468700:
    grundlön = bruttolön - 1604
    komunalskatt = grundlön * 0.2136
    landstingsskatt = grundlön * 0.1148
    nettolön = bruttolön - landstingsskatt - komunalskatt
    print("{0:20} {1:12}kr (årslön: {2}kr)".format("månadslön", round(bruttolön), round(årslön)))
    print("{0:20} {1:12}kr".format("Komunalskatt", round(komunalskatt)))
    print("{0:20} {1:12}kr".format("Landstingsskatt", round(landstingsskatt)))
    print("{0:20} {1:12}kr".format("Nettolön", round(nettolön)))

elif 468700 < årslön < 675700:
    grundlön = bruttolön - 1604
    komunalskatt = grundlön * 0.2136
    landstingsskatt = grundlön * 0.1148
    statligskatt = årslön - 468700
    statligskatt = statligskatt * 0.2
    statligskattpermånad = statligskatt / 12
    nettolön = bruttolön - landstingsskatt - komunalskatt - statligskattpermånad
    print("{0:20} {1:12}kr (årslön: {2}kr)".format("månadslön", round(bruttolön), round(årslön)))
    print("{0:20} {1:12}kr".format("Komunalskatt", round(komunalskatt)))
    print("{0:20} {1:12}kr".format("Landstingsskatt", round(landstingsskatt)))
    print("{0:20} {1:12}kr".format("Statligskatt", round(statligskattpermånad)))
    print("{0:20} {1:12}kr".format("Nettolön", round(nettolön)))
else: 
    grundlön = bruttolön - 1604
    komunalskatt = grundlön * 0.2136
    landstingsskatt = grundlön * 0.1148
    statligskatt = årslön - 468700
    statligskatt = statligskatt * 0.2
    statligskattpermånad = statligskatt / 12
    värnskatt = årslön - 675700
    värnskatt = värnskatt * 0.05
    värnskattpermånad = värnskatt / 12
    statligskattpermånad += värnskattpermånad
    nettolön = bruttolön - landstingsskatt - komunalskatt - statligskattpermånad
    print("{0:20} {1:12}kr (årslön: {2}kr)".format("månadslön", round(bruttolön), round(årslön)))
    print("{0:20} {1:12}kr".format("Komunalskatt", round(komunalskatt)))
    print("{0:20} {1:12}kr".format("Landstingsskatt", round(landstingsskatt)))
    print("{0:20} {1:12}kr".format("Statligskatt", round(statligskattpermånad)))
    print("{0:20} {1:12}kr".format("Nettolön", round(nettolön)))

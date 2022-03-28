bruttolön = float(input("Vad är din bruttolön i hela kronor?"))

årslön = bruttolön * 12

if årslön < 19247:
    print("{0:20} {1:12}kr (årslön: {2}kr)".format("månadslön", round(bruttolön), round(årslön)))
    print("{0:20} {1:12}kr".format("kvar efter skatt", round(bruttolön)))
    print("Eftersom du tjänar under brytpunkten betalar du ingen skatt")
else:
    komunalskatt = bruttolön * 0.2136
    landstingsskatt = bruttolön * 0.1148
    nettolön = bruttolön - landstingsskatt - komunalskatt
    print("{0:20} {1:12}kr (årslön: {2}kr)".format("månadslön", round(bruttolön), round(årslön)))
    print("{0:20} {1:12}kr".format("Komunalskatt", round(komunalskatt)))
    print("{0:20} {1:12}kr".format("Landstingsskatt", round(landstingsskatt)))
    print("{0:20} {1:12}kr".format("Nettolön", round(nettolön)))

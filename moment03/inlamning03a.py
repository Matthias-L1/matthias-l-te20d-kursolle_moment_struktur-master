bruttolön = float(input("Vad är din bruttolön i hela kronor?"))

komunalskatt = bruttolön * 0.2136
landstingsskatt = bruttolön * 0.1148
nettolön = bruttolön - landstingsskatt - komunalskatt

print("{0:20} {1:12}kr".format("månadslön", round(bruttolön)))
print("{0:20} {1:12}kr".format("Komunalskatt", round(komunalskatt)))
print("{0:20} {1:12}kr".format("Landstingsskatt", round(landstingsskatt)))
print("{0:20} {1:12}kr".format("Nettolön", round(nettolön)))

print("{0:20}|{1:20}|{2:20}|{3:20}|{4:20}|{5:20}|{6:20}|{7:20}".format("Årsinkomst", "Månadsinkomst" , "Total skatt", "Netto / månad", "Komunal skatt", "Landtings skatt", "Statlig skatt", "Total skatt i %"))
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")


löner =  [1500, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000]

for bruttolön in löner:
    if bruttolön < 1604:
        årslön = bruttolön * 12
        grundlön = bruttolön - 1604
        nettolön = bruttolön 
        totalskatt = bruttolön - nettolön
        statligskattpermånad = 0
        landstingsskatt = 0
        komunalskatt = 0
        totalskattprocent = 0
        print("{0:17}kr |{1:17}kr |{2:17}kr |{3:17}kr |{4:17}kr |{5:17}kr |{6:17}kr |{7:17}%".format(round(årslön), round(bruttolön), round(totalskatt), round(nettolön), round(komunalskatt), round(landstingsskatt), round(statligskattpermånad), round(totalskattprocent,2)))

    elif 1604 < bruttolön < 39058:
        årslön = bruttolön * 12
        grundlön = bruttolön - 1604
        komunalskatt = grundlön * 0.2136
        landstingsskatt = grundlön * 0.1148
        nettolön = bruttolön - landstingsskatt - komunalskatt
        totalskatt = bruttolön - nettolön
        totalskattprocent = totalskatt / bruttolön
        totalskattprocent *= 100
        statligskattpermånad = 0
        print("{0:17}kr |{1:17}kr |{2:17}kr |{3:17}kr |{4:17}kr |{5:17}kr |{6:17}kr |{7:17}%".format(round(årslön), round(bruttolön), round(totalskatt), round(nettolön), round(komunalskatt), round(landstingsskatt), round(statligskattpermånad), round(totalskattprocent,2)))

    elif 39058 < bruttolön < 56308:
        årslön = bruttolön * 12
        grundlön = bruttolön - 1604
        komunalskatt = grundlön * 0.2136
        landstingsskatt = grundlön * 0.1148
        statligskatt = årslön - 468700
        statligskatt = statligskatt * 0.2
        statligskattpermånad = statligskatt / 12
        nettolön = bruttolön - landstingsskatt - komunalskatt - statligskattpermånad
        totalskatt = bruttolön - nettolön
        totalskattprocent = totalskatt / bruttolön
        totalskattprocent *= 100
        print("{0:17}kr |{1:17}kr |{2:17}kr |{3:17}kr |{4:17}kr |{5:17}kr |{6:17}kr |{7:17}%".format(round(årslön), round(bruttolön), round(totalskatt), round(nettolön), round(komunalskatt), round(landstingsskatt), round(statligskattpermånad), round(totalskattprocent,2)))

    else: 
        årslön = bruttolön * 12
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
        totalskatt = bruttolön - nettolön
        totalskattprocent = totalskatt / bruttolön
        totalskattprocent *= 100
        print("{0:17}kr |{1:17}kr |{2:17}kr |{3:17}kr |{4:17}kr |{5:17}kr |{6:17}kr |{7:17}%".format(round(årslön), round(bruttolön), round(totalskatt), round(nettolön), round(komunalskatt), round(landstingsskatt), round(statligskattpermånad), round(totalskattprocent,2)))
    
    
    



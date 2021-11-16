#variabler
antal_pennor = 3
Kostnad_pennor = 4
total_kostnad_pennor = antal_pennor * Kostnad_pennor

vikt_äpple = 200
antal_äpple = 1
pris_per_kg_äpple = 19
total_kostnad_äpple = antal_äpple * vikt_äpple/1000 * pris_per_kg_äpple
#utskrift med kommatecken
print("jag handlade", antal_pennor, "pennor för", total_kostnad_pennor,"kr och", antal_äpple, "äpple för", total_kostnad_äpple,
total_kostnad_äpple, "kr vilket totalt blev", total_kostnad_äpple+total_kostnad_pennor, "kr.")
#utskrift med plustecken
print("jag handlade "+ str(antal_pennor) + " pennor för " + str(total_kostnad_pennor) + " kr och " + str(antal_äpple) + " äpple för "+ str(total_kostnad_äpple) +
str(total_kostnad_äpple) +  " kr vilket totalt blev "+ str(total_kostnad_äpple+total_kostnad_pennor) + "kr.")
#Utskrift genom att sträng byggs upp före utskrift.
s = "jag handlade " + str(antal_pennor) + " pennor för " + str(total_kostnad_pennor)
s += " kr och " + str(antal_äpple) + " äpple för " + str(total_kostnad_äpple) + str(total_kostnad_äpple)
s += " kr vilket blev totalt " + str(total_kostnad_pennor + total_kostnad_äpple) + "kr"
print(s)
#Utskrift med öppen print() utan radbrytning.
print("jag handlade " + str(antal_pennor) + " pennor för " + str(total_kostnad_pennor), end="")
print(" kr och " + str(antal_äpple) + " äpple för " + str(total_kostnad_äpple) + str(total_kostnad_äpple), end="" )
print(" kr vilket blev totalt" + str(total_kostnad_pennor + total_kostnad_äpple) + "kr")
#Utskrift med formatmetoden. 
print("jag handlade {0} pennor för {1} kr och {2} äpple för {3} kr vilket blev totalt {4} kr".format(antal_pennor, 
total_kostnad_pennor, antal_äpple, total_kostnad_äpple, total_kostnad_pennor + total_kostnad_äpple))
#Utskrift med f-stringmetoden.
print(f"jag handlade {antal_pennor} pennor för {total_kostnad_pennor} kr och {antal_äpple} äpple för {total_kostnad_äpple:.2f} vilket blev totalt {total_kostnad_pennor + total_kostnad_äpple:.2f}kr" )
#Kenny Ruan, TE20D, jag har löst uppgift m02u02, 2021-11-09
a = 9
b = 2
f = 4.0
namn = "Kenny Ruan"
#skriver ut talet och datatypen på a multiplicerat med b
print(a * b)
print(type(a * b))
#beräknar a multiplicerat med f och datatypen
print(a * f)
print(type(a * f))
#beräknar a dividerat med b och en datatyp. Datatypen blir float eftersom 9/2= 4.5, och float är till för siffror med kommatecken
print(a / b)
print(type(a / b))
#skriver ut datatypen och mitt namn
print(namn)
print(type(namn))
#beräknar heltalsdivitionen mellan a och b och samt datatypen. Svaret blir 4 eftersom det är heltalsdivision och därför blir datatypen 'int'. 'int' tar hand om heltal
print(a // b)
print(type(a // b))
#beräknar resten mellan a och b samt datatypen. det blir 1 eftersom det är resten. datatypen är 'int' eftersom den tar hand om heltal
print(a % b)
print(type(a % b))
#roten ur a. roten ur 9 = 3.0 och 'float' tar hand om tal med kommatecken
print(a ** 0.5)
print(type(a ** 0.5))
# kvadraten ur b. svaret blir 4 efter som 2 * 2 är 4, och 4 är ett heltal så datatypen är 'int'
print(b ** 2)
print(type(b ** 2))
#kvadraten ur f. det blir 16.0 eftersom 4.0 * 4.0 är 16.0. talet har ett kommatecken och därför blir datatypen 'float'
print(f ** 2)
print(type(f ** b))
#13
b += a
print(a)

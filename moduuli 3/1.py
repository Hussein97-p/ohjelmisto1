#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. 
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
#  montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, 
# jos sen pituus on alle 37 cm.

x = float(input("By Cm Enter The Fish Tall Here: "))
y = 37
G = y - x
l = "cm" 
if x >= y: print("Well Done 💫 you can keep it to your self")
else: print("your fish is",x,l,"It is missing about a",G.__round__ (2),l,"To keep it / please Return it to the lake")
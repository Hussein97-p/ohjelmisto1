#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) 
# ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
#  Tehtävässä on käytettävä if/elif/else-toistorakennetta.

# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
# C on ikkunaton hytti autokannen alapuolella.

print("Choose ONe Type OF Cabins That You Want  To Know About it : ")
print("Lux")
print("A")
print("B")
print("C")
Lux = ("Lux")
A = ("A")
B = ("B")
C = ("C")
print("Using The First Letter As Capital Letter")
X = str(input("The Cabin Is: "))

if X == Lux:
    print("LUX is a cabin with a balcony on the upper deck.")

elif X == A:
    print("A is a windowed cabin above the car deck.")

elif X == B:
    print("B is a windowless cabin above the car deck")

elif X == C:
    print("C is a windowless cabin below the car deck.")

else: 
    print("Invalid cabin class.")

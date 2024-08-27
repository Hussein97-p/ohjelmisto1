#  Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). 
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l./
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l./

print("Enter The First Letter With capital letter")
x = (input("HEllo ARE YOU A Man OR A Woman: "))
M = ("Man")
W = ("Woman")
if x == M:
    Y = int(input("How Much The HEmoglobin IN your Body: "))
    if Y <= 133:print("THE Hemoglobin in your Body is: low ")
    if Y >= 196:print("THE Hemoglobin in your Body is: High")
    if Y >= 134 <= 195:print("The Hemoglobin value is Nature")



elif x == W:
    Y =int(input("How Much The HEmoglabin IN your Body: "))
    if Y <= 116: print("THE Hemoglobin in your Body is: Low ")
    if Y >= 176: print("THE Hemoglobin in your Body is: High")
    if Y >= 117 <= 175:print("The Hemoglobin value is Nature")

else:print("wrong Enter")


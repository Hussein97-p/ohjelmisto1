
O = float(input("Anna leiviskät: "))
D = float(input("Anna naulat: "))
I = float(input("Anna luodit "))

x = O * 20 * 32 * 13.3 
y = D * 32 * 13.3
Z = I * 13.3 

G = (x + y + Z) 


N = int(G // 1000)
F = G % 1000
print("Massa nykymittojen mukaan:")
print(f"{N} kilogrammaa ja {F:.2f} grammaa.")
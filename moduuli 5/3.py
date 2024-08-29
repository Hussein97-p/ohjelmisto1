
while True:

    x = input("Put The Numbers Here:  ")

    if x == "":
        break 

    N_number = int(x)

    if N_number <= 1:
        print(N_number, "....This isn't a prime number")

    elif N_number == 2:
        print(N_number, "...This is a prime number")

    else:
        its_yes = True
        for i in range(2, N_number):
            if N_number % i == 0:
                its_yes = False
                break

        if its_yes:
            print(N_number, "...This is a prime number")
        else:
            print(N_number, "....This isn't a prime number")
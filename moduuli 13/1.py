from flask import Flask, jsonify
from colorama import init, Fore

init()

app = Flask(__name__)


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


@app.route('/prime/<int:number>', methods=['GET'])
def check_prime(number):

    is_prime_number = is_prime(number)
    

    return jsonify({"Number": number, "isPrime": is_prime_number})


if __name__ == '__main__':

    print(Fore.GREEN + "************************************************************")
    print(Fore.YELLOW + "Flask app is running!")
    print(Fore.CYAN + "To test a number, go to the following link:")
    print(Fore.MAGENTA + "http://127.0.0.1:3000/prime/<number>")
    print(Fore.GREEN + "Replace <number> with the number you want to check.")
    print(Fore.RED + "Example: http://127.0.0.1:3000/prime/31")
    print(Fore.GREEN + "************************************************************")
    

    app.run(port=3000)

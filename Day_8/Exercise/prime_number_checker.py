def prime_checker(number):
    its_prime = True
    for num in range(2, number): #remember that range(2, number) is actually (2, number - 1)....
        if n % num == 0:
            its_prime = False
    if its_prime:
        print("It's a prime number.")
    if not its_prime:
        print("It's not a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)

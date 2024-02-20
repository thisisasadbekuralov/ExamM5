
#2-masala 2- variant

def generate_primes(N):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for num in range(2, N + 1):
        if is_prime(num):
            yield num

N = int(input('enter the value for N: '))

prime_generator = generate_primes(N)
for prime in prime_generator:
    print(prime)

"""
UTA CSE 4381-001 Information Security II / Homework 3
Submission Date: 11.14.2023

Name: Hyeonjun An
Student ID: 1001342487
"""
import random

primeNums = set()

# A set of prime numbers using Sieve of Eratosthenes formula (< 1024)
def primecollector():
    sieve = [True] * 1024 #the limit is set to 1024 to create more variants of public keys.
    sieve[0] = False
    sieve[1] = False

    for i in range(2, 1024):
        for j in range(i*i, 1024, i):
            sieve[j] = False

    for i in range(len(sieve)):
        if sieve[i]:
            primeNums.add(i)
    
# A function to pick a random prime number.
def random_prime():
    global primeNums
    
    i = random.randint(0, len(primeNums)-1)

    while i < 100:
        i = random.randint(0, len(primeNums)-1)

    it = iter(primeNums)

    for _ in range(i):
        next(it)
    
    ret = next(it)
    primeNums.remove(ret)

    return ret
 
# Utility function to store prime
# factors of a number 
def findPrimefactors(s, n) :
 
    # Print the number of 2s that divide n 
    while (n % 2 == 0) :
        s.add(2) 
        n = n // 2
 
    # n must be odd at this point. So we can  
    # skip one element (Note i = i +2) 
    for i in range(3, int(n**.5), 2):
         
        # While i divides n, print i and divide n 
        while (n % i == 0) :
 
            s.add(i) 
            n = n // i 
         
    # This condition is to handle the case 
    # when n is a prime number greater than 2 
    if (n > 2) :
        s.add(n) 
 
# Function to find smallest primitive 
# root of n 
def findPrimitive(n) :
    s = set() 

    phi = n - 1
 
    # Find prime factors of phi and store in a set 
    findPrimefactors(s, phi) 
 
    # Check for every number from 2 to phi 
    for r in range(2, phi + 1): 
 
        # Iterate through all prime factors of phi. 
        # and check if we found a power with value 1 
        flag = False
        for it in s: 
 
            # Check if r^((phi)/primefactors)
            # mod n is 1 or not 
            if (power(r, phi // it, n) == 1): 
 
                flag = True
                break
             
        # If there was no power with value 1. 
        if (flag == False):
            return r 
 
    # If no primitive root found 
    return -1

# Find a gcd between two numbers (simplified)
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# Generate a key between 2 and the selected prime number
def gen_key(prime):
 
    key = random.randint(2, prime)
    while gcd(prime, key) != 1:
        key = random.randint(2, prime)
 
    return key

# Modulo exponentiation
def power(a, b, c):
    x = 1
    y = a
 
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c

def encrypt(msg, prime, h, root):
    # Check if M < p.
    if len(msg) >= prime:
        print("The length of plaintext must be shorter than the selected prime. \n")
        exit()
 
    ciphertext = []
 
    k = gen_key(prime) # private key for Bob
    s = power(h, k, prime)
    c1 = power(root, k, prime)
     
    for i in range(0, len(msg)):
        ciphertext.append(msg[i])
 
    for i in range(0, len(ciphertext)):
        ciphertext[i] = s * ord(ciphertext[i])
 
    return ciphertext, c1

def decrypt(ciphertext, p, key, prime):
 
    dr_msg = []
    h = power(p, key, prime)
    for i in range(0, len(ciphertext)):
        dr_msg.append(chr(int(ciphertext[i]/h)))
         
    return dr_msg

if __name__ == '__main__':

    primecollector()

    prime = random_prime()
    root = findPrimitive(prime)

    # No primitive root
    if root == -1:
        print("No primitive root has been found.\n")
        exit()

    print("large prime number p is: ", prime)
    print("the primitive root of p is: ", root, "\n")

    msg = input("Type in your plaintext: ")

    key = gen_key(prime) # Private key for Alice
    h = power(root, key, prime)
 
    ciphertext, p = encrypt(msg, prime, h, root)
    dr_msg = decrypt(ciphertext, p, key, prime)
    recovered = ''.join(dr_msg)
    print("Decrypted Message :", recovered)

"""
UTA CSE 4381-001 Information Security II / Homework 2
Submission Date: 10.17.2023

Name: Hyeonjun An
Student ID: 1001342487
"""

import random

primeNums = set()

public_key = None
private_key = None

n = int()

#Euclidean Extended Algorithm in a recursive function
def gcdExtended(a, b): 
    # Base Case 
    if a == 0 : 
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a) 
     
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y 

# A set of prime numbers using Sieve of Eratosthenes formula (< 256)
def primecollector():
    sieve = [True] * 256 #the limit is set to 256 to create more variants of public keys.
    sieve[0] = False
    sieve[1] = False

    for i in range(2, 256):
        for j in range(i*i, 256, i):
            sieve[j] = False

    for i in range(len(sieve)):
        if sieve[i]:
            primeNums.add(i)
    
# A function to pick a random prime number.
def random_prime():
    global primeNums

    i = random.randint(0, len(primeNums)-1)

    it = iter(primeNums)

    for _ in range(i):
        next(it)
    
    ret = next(it)
    primeNums.remove(ret)

    return ret

# Key generator with Euler Totient Funtion & Euclidean Extended Algorithm
def keysetter():
    global public_key, private_key, n

    prime_1 = random_prime()
    prime_2 = random_prime()

    n = prime_1 * prime_2
    phi = (prime_1 - 1) * (prime_2 - 1) # Φ(n) = Φ(p) * Φ(q) = (p-1) * (q-1)

    # Find e that is coprime to the calculated n
    for e in range(2, phi):
        gcd = gcdExtended(e, phi)
        if gcd[0] == 1:
            public_key = e
            break
    
    # d = (k*Φ(n) + 1) / e for some integer k
    d = 2
    while True:
        if (d * e) % phi == 1:
            break
        d += 1
 
    private_key = d

# Encryption & Decryption functions using ASCII value of the plaintext
# Encryption function
def encrypt(plaintext: str):
    global public_key, n
    
    e = public_key

    #print("public key: " + str(e))

    ciphertext = 1

    while e > 0:
        ciphertext *= plaintext
        ciphertext %= n
        e -= 1
    
    return ciphertext

# Decryption funtion
def decrypt(ciphertext: list):
    global private_key, n
    d = private_key

    #print("private key: " + str(d))
    plaintext = 1

    while d > 0:
        plaintext *= ciphertext
        plaintext %= n
        d -= 1

    return plaintext

# Put the strands of ciphertext into one list
def encoder(message: str):
    encoded = []
    # Calling the encrypting function in encoding function
    for letter in message:
        encoded.append(encrypt(ord(letter)))
    return encoded
 
# Decrypt the ciphertext generated
def decoder(encoded: str):
    s = ''
    # Calling the decrypting function decoding function
    for num in encoded:
        s += chr(decrypt(num))
    return s

if __name__ == '__main__':
    primecollector()
    
    usrInput = int()
    plaintext = str()

    while usrInput != 2:
        print("\n######################## RSA Simulation ########################")
        print("BY HYEONJUN AN, UTA BSCS, CSE 4381_Homework 2")
        print("Please choose one of the options below:")
        print("1. RSA Simulation")
        print("2. Exit")

        usrInput = int(input("Option: "))
        
        if usrInput == 1:
            print("\n################## Welcome to RSA Simulation ###################")
            plaintext = input("Please type in your plaintext to be encrypted: ")
            
            keysetter()

            encrypted_text = encoder(plaintext)
            decrypted_text = decoder(encrypted_text)

            print("\nYour Cipher Text is: ")
            print(''.join(str(p) for p in encrypted_text))
            print("\nYour Recovered Text is: " + decrypted_text)

        elif usrInput != 1 and usrInput != 2:
            print("Your Input should be either 1 or 2!")


#!/usr/bin/python3

import time

import sympy.ntheory as nt
from gmpy2 import mpz, digits, is_bpsw_prp

with open("./seb_bio_200x199.jpeg", "rb") as binfile:
    bits_from_disk = binfile.read()

prime_cand = int.from_bytes(bits_from_disk, "big", signed=False)

print(prime_cand)

a = mpz(prime_cand)

print("length (base 10) = ", a.num_digits(10))
print("length (base 2) = ", a.num_digits(2))

print("methode bpsw")

t0 = time.clock_gettime(time.CLOCK_MONOTONIC)

if is_bpsw_prp(a):
    print("is prime")
else:
    print("is not prime")

t1 = time.clock_gettime(time.CLOCK_MONOTONIC)

print("elapsed for bpsw = %.0fs" % ((int)(t1-t0)))

print("methode sympy.isprime")

t0 = time.clock_gettime(time.CLOCK_MONOTONIC)

if nt.isprime(prime_cand):
    print("is prime")
else:
    print("is not prime")

t1 = time.clock_gettime(time.CLOCK_MONOTONIC)

print("elapsed for sympy is prime = %.0fs" % ((int)(t1-t0)))

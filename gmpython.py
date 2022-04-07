#!/usr/bin/python3

import time
import os
import math

from gmpy2 import mpz, digits, is_bpsw_prp
from array import array

os.system("convert -resize 256x /home/seb/HP_data/seb_bio.jpg /home/seb/HP_data/seb_bio_vvsmall.jpg")
os.system("mogrify -strip /home/seb/HP_data/seb_bio_vvsmall.jpg")
os.system("exiftool -purejpg /home/seb/HP_data/seb_bio_vvsmall.jpg")

with open("/home/seb/HP_data/seb_bio_vvsmall.jpg", "rb") as binaryfile:
    origfile = binaryfile.read()

niceint = int.from_bytes(origfile, "big", signed=False)

a = mpz(niceint)

print("init length (2) = ", a.num_digits(2))

next_one = math.log(2, 10)*a.num_digits(2)
print("next prime in ~ log(2) * length = ", next)

# combien de zeros faudra t-il prefixer pour tomber sur des octets
if a.num_digits(2) % 8 != 0:
    zeroes = 8 - a.num_digits(2) % 8
else:
    zeroes = 0

print("je compte ajouter ", zeroes, "zero(s) au debut")

# on saute sur le premier impair suivant si necessaire
if a % 2 == 0:
    a = a + 1

print("candidate jpg 'number':", a)

print("init len(2)  = ", a.num_digits(2))
print("init len(10) = ", a.num_digits(10))

x = 0

t0 = time.clock_gettime_ns(time.CLOCK_MONOTONIC)

tot_time_small_div = 0
tot_time_mod_pow = 0
tot_processed_small_div = 0
tot_processed_mod_pow = 0
tot_processed_bpsw = 0
tot_time_bpsw = 0

while True:

    a = a + 2
    x = x + 1

    tnow = time.clock_gettime_ns(time.CLOCK_MONOTONIC)

    print("%.0fs: %.1f ms/candidate (#%d done bpsw %d = %.0f percent, next %.0f)" % ((int)(tnow-t0) /
                                                                                     1000000000.0, (tnow-t0)/x/1000000.0, x, tot_processed_bpsw, tot_processed_bpsw/x*100.0, next_one))

    print("%.0fs: %.1f ms/candidate (#%d done bpsw %d = %.0f percent, next %.0f)" % ((int)(tnow-t0) /
                                                                                     1000000000.0, (tnow-t0)/x/1000000.0, x, tot_processed_bpsw, tot_processed_bpsw/x*100.0, next_one))

    
    NMAX = 1
    # print("trying small divisors...")

    prime = True

    for small_div in range(1, NMAX):
        # print("trying ", small_div*2+1)
        if a % (small_div*2+1) == 0:
            # print("skipping since ", small_div*2+1, " is a divisor")
            prime = False
            break

    if prime is False:
        continue

    if not is_bpsw_prp(a):
        prime = False

    tot_processed_bpsw = tot_processed_bpsw + 1

    if prime is False:
        continue

    if pow(13, a - 1, a) == 1:
        print("success:", a)
        with open("/tmp/toto_out", "wb") as binaryfile:
            strprime = digits(a, 2)
            print(strprime)
            for pad in range(0, zeroes):
                strprime = "0" + strprime

            print("padded to initial bytes... = ", strprime)
            print("longueur = ", len(strprime))

            if len(strprime) % 8 != 0:
                print("erreur")
                exit

            num_bytes = len(strprime)/8

            print(int(strprime[0:8], 2))

            bin_array = array('B')
            for i in range(0, int(num_bytes)):
                bin_array.append(int(strprime[i*8:i*8+8], 2))
            bin_array.tofile(binaryfile)
        print("successfully dumped into /tmp/toto_out")
        break
    else:
        print("not prime at offset x = ", x * 2)
    tnow2 = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
    tot_processed_mod_pow = tot_processed_mod_pow + 1
    tot_time_mod_pow = tot_time_mod_pow + (int)(tnow2 - tnow)
    print((int)(tnow2-tnow), ":done modpow:", tot_time_mod_pow, " ",
          tot_time_mod_pow / tot_processed_mod_pow)

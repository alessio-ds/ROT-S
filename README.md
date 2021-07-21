# ROT-S
**ROT-S** is a letter substitution cipher that works similarly to ROT-13.
###### **S** stands for Scarlet, which is my nickname.

## How does it work?
- The first alphabetic character will be rotated to the next (**+1**) letter of the alphabet. 
- The second will be rotated to the previous two (**-2**).
- The third will be rotated to the third next (**+3**)
- The fourth to the previous four (**-4**) and so on.

"hello" will be ciphered into "icoht"

H + 1 = **I**

E - 2 = **C**

L + 3 = **O**

L - 4 = **H**

O + 5 = **T**

Differently from the "rotate by X places" ciphers, ROT-S **uses the space as the 27th character of the alphabet**.

The ROT-S alphabet looks like this: 
`alphabet = 'abcdefghijklmnopqrstuvwxyz '`

It will also rotate **numbers**:

123 -> 206

1 + 1 = **2**

2 - 2 = **0**

3 + 3 = **3**

**The punctuation is untouched.**

## Python

I coded 3 python files:
- ***encrypt.py*** allows you to get a quick encryption of any text you want
- ***decrypt.py*** allows you to get a quick decryption of any **ROT-S** encrypted text you want
- ***encrdecr.py*** allows you to either encrypt or decrypt a .txt file.

**Encrypting 250 bytes with 'encrdecr.py':**

![a](https://i.imgur.com/6IxaNN2.png)

#### I also took some speed tests:

**TIME TO ENCRYPT** 

100 bytes - 0.03s

250 bytes - 0.09s

500 bytes - 0.21s

1000 bytes - 0.41s

2500 bytes - 0.97s

10.000 bytes - 3.76s


**TIME TO DECRYPT**

100 bytes - 0.04s

250 bytes - 0.09s

500 bytes - 0.19s

1000 bytes - 0.40s

2500 bytes - 1.01s

10.000 bytes - 4.05s

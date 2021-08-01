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

3 + 3 = **6**

**The punctuation is untouched.**

## Python

I coded 3 python files:
- ***encrypt.py*** allows you to get a quick encryption of any text you want
- ***decrypt.py*** allows you to get a quick decryption of any **ROT-S** encrypted text you want
- ***encrdecr.py*** allows you to either encrypt or decrypt a .txt file.
- ***tests.py*** allows you to test how quick this method is by using different lenghts of .txt files, going from 100bytes to 100k bytes (you can use your own too). This is WAY quicker than encrdecr.py because it doesn't print every time it ciphers a byte.

## Downloads

You can either **download** each file or you can directly download the .zip with everything [**here**](https://github.com/alessio-ds/ROT-S/releases "here")

## Example

**Encrypting 250 bytes with 'encrdecr.py':**

![](https://i.imgur.com/6IxaNN2.png)

# Speed-tests:

![](https://i.imgur.com/XT1Srbe.png)
![](https://i.imgur.com/wkCxeh0.png)

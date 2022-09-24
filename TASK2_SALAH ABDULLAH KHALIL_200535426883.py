# NAME : SALAH ABDULLAH KHALIL ABDULRAHMAN
# NIM : 200535426883
# OFFER: C
a = input("print words that u want without vowels letters: ").strip().lower()
s = [char for char in a if char not in ('a', 'e', 'i', 'o', 'u')]
print(''.join(s))




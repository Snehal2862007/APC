text=input("enter message: ")
shift=int(input("Enter shift: "))
encrypted=""
for ch in text:
    if ch.isalpha():
        base=ord('A') if ch.isupper() else ord('a')
        encrypted+=chr((ord(ch)-base+shift)%26+base)
    else:
        encrypted+=ch
print("encrypted:", encrypted)
decrypted=""
for ch in encrypted:
    if ch.isalpha():
        base=ord('A') if ch.isupper() else ord('a')
        decrypted+=chr((ord(ch) - base - shift) % 26 + base)
    else:
        decrypted+=ch
print("decrypted:",decrypted)
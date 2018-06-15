from Crypto.Cipher import AES


counter = "^SdppLtD$."*16 # if you change the counter or key you can't decrypt something you had with a another key or counter
key = "^SdppLtD$."*32

def encrypt(message):
    encrypto = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
    return encrypto.encrypt(message)

def decrypt(message):
    decrypto = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
    return  decrypto.decrypt(message) 

print("-------------------------------------")
print("you can exit the program with: exit")
print("-------------------------------------")

a = input("what to decrypt or encrypt? > ")
if a == "decrypt":
    string = input("what message to decrypt\n")
    print("-------------------------------------")
    print("     output\n")

    output = decrypt( string )
    print(output)

if a == "encrypt":
    string = input("what message to encrypt\n")
    print("-------------------------------------")
    print("     output\n")

    output = encrypt( string )
    print(output)

if a == "exit"
    do = False

else:
    print("-------------------------------------")
    print("only encrypt decrypt or exit\n")
    print("-------------------------------------")

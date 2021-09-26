import random
class RSA():
    def __init__(self, p, q):
        self.privateKey = None
        self.publicKey = None
        self.p = p
        self.q = q
    def generate_keypair(self):
        n = self.p * self.q
        z = (self.p - 1) * (self.q - 1)
        e = random.randrange(1, n)
        g = self.gcd(e, z)
        while g != 1:
            e = random.randrange(1, n)
            g = self.gcd(e, z)

        d = self.multiplicative_inverse(e, z)
        self.publicKey = (e,n)
        self.privateKey = (d,n)
        return (e,n),(d,n)
    
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    def multiplicative_inverse(self, e, z):
        d = 0
        x1 = 0
        x2 = 1
        y1 = 1
        temp_z = z
        while e > 0:
            temp1 = temp_z // e
            temp2 = temp_z - temp1 * e
            temp_z = e
            e = temp2
            x = x2 - temp1 * x1
            y = d - temp1 * y1
            x2 = x1
            x1 = x
            d = y1
            y1 = y
        if temp_z == 1:
            return d + z

    def encrypt(self, key, plainText):
        e, n = key
        cipherText = ""
        for i in range(len(plainText)):
            cipherText += chr(((ord(plainText[i]) ** e) % n))
        return cipherText
    def decrypt(self, cipherText):
        d, n = self.privateKey
        plainText = ""
        for i in range(len(cipherText)):
            plainText += chr(((ord(cipherText[i]) ** d) % n))
        return plainText

tom = RSA(17, 11)
cate = RSA(3, 7)
print(tom.generate_keypair())
print(cate.generate_keypair())
print(tom.encrypt(cate.publicKey, "hi").encode("UTF-8"))
print(cate.decrypt(tom.encrypt(cate.publicKey, "hi")).encode("UTF-8"))
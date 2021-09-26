class DH_endpoint():
    def __init__(self, firstPub, secondPub, myPrivate):
        self.firstPub = firstPub
        self.secPub = secondPub
        self.private = myPrivate
        self.fullKey = 0
    def generatePartialKey(self):
        tmp = self.firstPub**self.private
        partialkey = tmp%self.secPub
        return partialkey
    def generateFullKey(self,otherPartial):
        tmp = otherPartial**self.private
        self.fullKey += tmp%self.secPub
        return self.fullKey


firstPublic = 197
firstPrivate = 199

secPublic = 151
secPrivate = 157

seb = DH_endpoint(firstPublic, secPublic, firstPrivate)
eron = DH_endpoint(firstPublic, secPublic, secPrivate)

print("Seb Partial Key = ")
print(seb.generatePartialKey()) #show seb partial key
print("eron Partial Key = ")
print(eron.generatePartialKey()) #show eron partial key

print("Seb full key")
print(seb.generateFullKey(eron.generatePartialKey())) #show seb full key
print("eron full key")
print(eron.generateFullKey(seb.generatePartialKey())) #show eron full key


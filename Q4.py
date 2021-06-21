#Knapsack Public-Key Crypto
#Steven Toub
#SE578-900

publicKey = [18,30,7,26]
m = 6
n = 47
privateKey = []

def encrypt(message,pubKey):

    messageList = [char for char in message]
    encryptedList = []
    encryptedMessage = 0

    b=0
    while(b < len(pubKey)):

        value = int(pubKey[b])*int(messageList[b])
        encryptedList.insert(b,value)

        b = b+1

    a=0
    while(a < len(encryptedList)):

        encryptedMessage = encryptedMessage + int(encryptedList[a])

        a = a+1

    return encryptedMessage


i=0
while(i < len(publicKey)):
        
    pkInt = int(publicKey[i])
    value = (pkInt/m) % n

    privateKey.insert(i,value)

    i = i+1

encrypted = encrypt('1101',publicKey)

print('Private Key: ',privateKey)
print('1101 encrypted is: ',encrypted)






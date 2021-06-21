#Simple Sub Quadgram Frequency Analysis
#Steven Toub SE578-900

import random
import re
from pycipher import SimpleSubstitution
from math import log10

#class that compares a decoded cipher with a potential key to the
#list of quadgrams to determine how closely the decoded cipher
#matches english quadgram frequencies
class quadgramFitness(object):

    def __init__(self,quadgramDb,delin=' '):

        self.quadgrams = {}

        for a in open(quadgramDb):
            key,count = a.split(delin)
            self.quadgrams[key] = int(count)

        self.keyLength = len(key)
        self.num = sum(self.quadgrams.values())

        for key in self.quadgrams.keys():
            self.quadgrams[key] = log10(float(self.quadgrams[key])/self.num)
        
        self.f = log10(0.01/self.num)

    def fitness(self,inp):

        fitnessScore = 0
        quadgrams = self.quadgrams.__getitem__
        
        for b in range(len(inp)-self.keyLength+1):

            if inp[b:b+self.keyLength] in self.quadgrams: 
                fitnessScore += quadgrams(inp[b:b+self.keyLength])
            else:
                fitnessScore += self.f

        return fitnessScore


#prompts user for cipher input and then attempts to find the key with the best quadgram fitness score
decodeFitness = quadgramFitness('english_quadgrams.txt')
    
print("Enter cipher: ")
cipherInput = input()
cipherInput = re.sub('[^A-Z]','',cipherInput.upper())

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
highestFit = -99e9
score,key = highestFit,alphabet[:]

c=0
while 1:

    c = c + 1
    random.shuffle(key)

    solveAttempt = SimpleSubstitution(key).decipher(cipherInput)
    score = decodeFitness.fitness(solveAttempt)

    d=0
    while d < 1000:

        alpha = random.randint(0,25)
        beta = random.randint(0,25)

        newKey = key[:]

        newKey[alpha],newKey[beta] = newKey[beta],newKey[alpha]

        solveAttempt = SimpleSubstitution(newKey).decipher(cipherInput)

        newScore = decodeFitness.fitness(solveAttempt)

        if newScore > score:

            score = newScore
            key = newKey[:]
            d=0

        d = d + 1

    if score > highestFit:

        highestFit,alphabet = score,key[:]

        print("Ctrl+C to halt deciphering...")
        print('Iteration: ', c)

        solved = SimpleSubstitution(alphabet)
        print('Key Attempt: '+''.join(alphabet))
        print('Deciphered Text: ' + solved.decipher(cipherInput))

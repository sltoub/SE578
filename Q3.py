#A5/1
#Steven Toub
#SE578-900

import copy

def majority(x,y,z):

    if((x+y+z) > 1):
        return 1
    else: return 0

def generateBit():

    xVal = Xreg[8]
    yVal = Yreg[10]
    zVal = Zreg[10]

    major = majority(xVal,yVal,zVal)

    #steps the x register
    if xVal == major : 

        Xnew = Xreg[13]^Xreg[16]^Xreg[17]^Xreg[18]
        tempXreg = copy.deepcopy(Xreg)

        a=1
        while(a < len(Xreg)):

            Xreg[a] = tempXreg[a-1]
            a = a + 1

        Xreg[0] = Xnew

    #steps the y register
    if yVal == major : 

        Ynew = Yreg[20]^Yreg[21]
        tempYreg = copy.deepcopy(Yreg)
        
        b=1
        while(b < len(Yreg)):

            Yreg[b] = tempYreg[b-1]
            b = b + 1

        Yreg[0] = Ynew

    #steps the z register
    if zVal == major : 

        Znew = Zreg[7]^Zreg[20]^Zreg[21]^Zreg[22]
        tempZreg = copy.deepcopy(Zreg)

        c=1
        while(c < len(Zreg)):

            Zreg[c] = tempZreg[c-1]
            c = c + 1

        Zreg[0] = Znew



Xreg = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
Yreg = [1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1]
Zreg = [1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0]

bitStream = []

#loops 32 times to generate next 32 bits in the stream for the given registers
for i in range(32):

    generateBit()

    streamBit = int(Xreg[18]^int(Yreg[21])^int(Zreg[22]))

    bitStream.insert(i, streamBit)

print('Next 32 bits in stream: ',(bitStream))

print('X register: ',(Xreg))
print('Y register: ',(Yreg))
print('Z register: ',(Zreg))
import random
from Tkinter import *
import Tkinter as tk
import math


def genName():     #Random Name Generator
    name = ''
    cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z','y']
    hCons = ['c','t','s','p']
    lCons = ['c','b','f','g','p','s']
    rCons = ['b','c','f','g','p','t','w']
    vowels = ['a','e','i','o','u']
    if random.randint(1,5) == 1:
        letter = random.choice(vowels)
    else:
        letter = random.choice(cons)
    name += letter
    for i in range(random.randint(4,7)):
        if name[-1] not in vowels:
            if name[-1] not in hCons:
                if name[-1] not in lCons:
                    if name[-1] not in rCons:
                        name += random.choice(vowels)
                    else:
                        if random.randint(1,5) == 1:    
                            name += 'r'
                        else:
                            name += random.choice(vowels)
                else:
                    if name[-1] in rCons:
                        if random.randint(1,5) == 1:
                            name += 'r'
                        elif random.randint(1,5) == 1:
                            name += 'l'
                        else:
                            name += random.choice(vowels)
                    else:
                        if random.randint(1,5) == 1:
                            name += 'l'
                        else:
                            name += random.choice(vowels)
            else:        
                if random.randint(1,5) == 1:
                    name += 'h'
                else:
                    if name[-1] in rCons:
                        if name[-1] in lCons:
                            if random.randint(1,5) == 1:
                                name += 'l'
                            else:
                                name += random.choice(vowels)
                        if random.randint(1,5) == 1:
                            name += 'r'
                        else:
                            name += random.choice(vowels)
                    else:
                        if name[-1] in lCons:
                            if random.randint(1,5) == 1:
                                name += 'l'
                            else:
                                name += random.choice(vowels)
        else:
            if name[-1] in 'eo':
                if name[-1] != name[-2]:
                    if random.randint(1,5) == 1:
                        name += name[-1]
                    else:
                        name += random.choice(cons)
            else:
                name += random.choice(cons)
    return name


def drawCreature(bodypartPos, bodypartStr, distances, width, bodyAnchor, window, bodyColor):
    for limbNum in range(len(bodypartPos)):
            if limbNum % 2 == 0 or limbNum == 0:
                limbAngle = (45*bodypartPos[limbNum]) - 45
                limbXAnchor = bodyAnchor[0] + ((distances[0])*(math.sin((math.pi/180)*limbAngle)))
                limbYAnchor = bodyAnchor[1] + ((distances[0])*(math.sin((math.pi/180)*(limbAngle - 90))))
                limbColor = '#%02x%02x%02x' % (bodypartStr[limbNum] * 2 + 55, 0, 0)
                window.create_line(bodyAnchor[0], bodyAnchor[1], limbXAnchor, limbYAnchor, width= width[0] + 1, fill= '#%02x%02x%02x' % (255,255,255))
                window.create_line(bodyAnchor[0], bodyAnchor[1], limbXAnchor, limbYAnchor, width= width[0] + 1, fill= limbColor)
            else:
                for appendageNum in range(len(bodypartPos[limbNum])):
                    if appendageNum % 2 == 0 or appendageNum == 0:
                        appendageAngle = ((45*bodypartPos[limbNum][appendageNum]) - 90) + limbAngle
                        appendageXAnchor = limbXAnchor + (distances[1]*(math.sin((math.pi/180)*(appendageAngle))))
                        appendageYAnchor = limbYAnchor + (distances[1]*(math.sin((math.pi/180)*(appendageAngle - 90))))
                        appendageColor = '#%02x%02x%02x' % (0, bodypartStr[limbNum][appendageNum] * 2 + 55, 0)
                        window.create_line(limbXAnchor,limbYAnchor,appendageXAnchor,appendageYAnchor,width= width[1] + 1, fill= '#%02x%02x%02x' % (255,255,255))
                        window.create_line(limbXAnchor,limbYAnchor,appendageXAnchor,appendageYAnchor,width= width[1] + 1, fill= appendageColor)
                    else:
                        for phalangeNum in range(len(bodypartPos[limbNum][appendageNum])):
                            phalangeAngle = ((45*bodypartPos[limbNum][appendageNum][phalangeNum]) - 135) + appendageAngle
                            phalangeXAnchor = appendageXAnchor + (distances[2]*(math.sin((math.pi/180)*(phalangeAngle))))
                            phalangeYAnchor = appendageYAnchor + (distances[2]*(math.sin((math.pi/180)*(phalangeAngle - 90))))
                            phalangeColor = '#%02x%02x%02x' % ((0, 0, bodypartStr[limbNum][appendageNum][phalangeNum] * 2 + 55))
                            window.create_line(appendageXAnchor,appendageYAnchor,phalangeXAnchor,phalangeYAnchor,width= width[2] + 1, fill= '#%02x%02x%02x' % (255,255,255))
                            window.create_line(appendageXAnchor,appendageYAnchor,phalangeXAnchor,phalangeYAnchor,width= width[2] + 1, fill= phalangeColor)
                            window.create_oval(phalangeXAnchor + (width[2]/2) - 1, phalangeYAnchor + (width[2]/2) - 1, phalangeXAnchor - (width[2]/2) + 1, phalangeYAnchor - (width[2]/2) + 1, fill= phalangeColor, outline= phalangeColor)
                        window.create_oval([appendageXAnchor + (width[1]/2)], [appendageYAnchor + (width[1]/2)], [appendageXAnchor - (width[1]/2)], [appendageYAnchor - (width[1]/2)], fill= appendageColor, outline= appendageColor)
                window.create_oval([limbXAnchor + (width[0]/2)], [limbYAnchor + (width[0]/2)], [limbXAnchor - (width[0]/2)], [limbYAnchor - (width[0]/2)], fill=  '#%02x%02x%02x' % (bodypartStr[limbNum - 1] * 2 + 55, 0, 0), outline= '#%02x%02x%02x' % (bodypartStr[limbNum - 1] * 2 + 55, 0, 0))
    avgColor = '#%02x%02x%02x' % ((sum(bodyColor[0])/(len(bodyColor[0]))), (sum(bodyColor[1])/(len(bodyColor[1]))), (sum(bodyColor[2])/(len(bodyColor[2]))))
    window.create_oval(bodyAnchor[0] + width[0] * 1.5, bodyAnchor[1] + width[0] * 1.5, bodyAnchor[0] - width[0] * 1.5, bodyAnchor[1] - width[0] * 1.5, fill= avgColor, outline= avgColor)
    
    
def drawMovedCreature(bodypartPos, bodypartStr, distances, width, bodyAnchor, window, bodyColor):
    for limbNum in range(len(bodypartPos)):
            if limbNum % 2 == 0 or limbNum == 0:
                limbAngle = (45*bodypartPos[limbNum]) - 45
                randomDistance = random.random()
                limbXAnchor = bodyAnchor[0] + ((distances[0] * randomDistance)*(math.sin((math.pi/180)*limbAngle)))
                limbYAnchor = bodyAnchor[1] + ((distances[0] * randomDistance)*(math.sin((math.pi/180)*(limbAngle - 90))))
                limbColor = '#%02x%02x%02x' % (bodypartStr[limbNum] * 2 + 55, 0, 0)
                window.create_line(bodyAnchor[0], bodyAnchor[1], limbXAnchor, limbYAnchor, width= width[0] + 1, fill= '#%02x%02x%02x' % (255,255,255))
                window.create_line(bodyAnchor[0], bodyAnchor[1], limbXAnchor, limbYAnchor, width= width[0] + 1, fill= limbColor)
            else:
                for appendageNum in range(len(bodypartPos[limbNum])):
                    if appendageNum % 2 == 0 or appendageNum == 0:
                        appendageAngle = random.randint(1,360)
                        appendageXAnchor = limbXAnchor + (distances[1]*(math.sin((math.pi/180)*(appendageAngle))))
                        appendageYAnchor = limbYAnchor + (distances[1]*(math.sin((math.pi/180)*(appendageAngle - 90))))
                        appendageColor = '#%02x%02x%02x' % (0, bodypartStr[limbNum][appendageNum] * 2 + 55, 0)
                        window.create_line(limbXAnchor,limbYAnchor,appendageXAnchor,appendageYAnchor,width= width[1] + 1, fill= '#%02x%02x%02x' % (255,255,255))
                        window.create_line(limbXAnchor,limbYAnchor,appendageXAnchor,appendageYAnchor,width= width[1] + 1, fill= appendageColor)
                    else:
                        for phalangeNum in range(len(bodypartPos[limbNum][appendageNum])):
                            phalangeAngle = random.randint(1,360)
                            phalangeXAnchor = appendageXAnchor + (distances[2]*(math.sin((math.pi/180)*(phalangeAngle))))
                            phalangeYAnchor = appendageYAnchor + (distances[2]*(math.sin((math.pi/180)*(phalangeAngle - 90))))
                            phalangeColor = '#%02x%02x%02x' % ((0, 0, bodypartStr[limbNum][appendageNum][phalangeNum] * 2 + 55))
                            window.create_line(appendageXAnchor,appendageYAnchor,phalangeXAnchor,phalangeYAnchor,width= width[2] + 1, fill= '#%02x%02x%02x' % (255,255,255))
                            window.create_line(appendageXAnchor,appendageYAnchor,phalangeXAnchor,phalangeYAnchor,width= width[2] + 1, fill= phalangeColor)
                            window.create_oval(phalangeXAnchor + (width[2]/2) - 1, phalangeYAnchor + (width[2]/2) - 1, phalangeXAnchor - (width[2]/2) + 1, phalangeYAnchor - (width[2]/2) + 1, fill= phalangeColor, outline= phalangeColor)
                        window.create_oval([appendageXAnchor + (width[1]/2)], [appendageYAnchor + (width[1]/2)], [appendageXAnchor - (width[1]/2)], [appendageYAnchor - (width[1]/2)], fill= appendageColor, outline= appendageColor)
                window.create_oval([limbXAnchor + (width[0]/2)], [limbYAnchor + (width[0]/2)], [limbXAnchor - (width[0]/2)], [limbYAnchor - (width[0]/2)], fill=  '#%02x%02x%02x' % (bodypartStr[limbNum - 1] * 2 + 55, 0, 0), outline= '#%02x%02x%02x' % (bodypartStr[limbNum - 1] * 2 + 55, 0, 0))
    avgColor = '#%02x%02x%02x' % ((sum(bodyColor[0])/(len(bodyColor[0]))), (sum(bodyColor[1])/(len(bodyColor[1]))), (sum(bodyColor[2])/(len(bodyColor[2]))))
    window.create_oval(bodyAnchor[0] + width[0] * 1.5, bodyAnchor[1] + width[0] * 1.5, bodyAnchor[0] - width[0] * 1.5, bodyAnchor[1] - width[0] * 1.5, fill= avgColor, outline= avgColor)


def collectCreatureNumber():
    try:
        creatureNum = int(raw_input('How many creatures do you want? '))
        if creatureNum < 0:
            print ('Your number needs to be greater than one, randomly selecting creature number')
            creatureNum = random.randint(10,1350)
    except:
        print ('There has been an error in your input, values will be randomly generated for you')
        creatureNum = random.randint(10,1350)
    return creatureNum


def collectLimbValues():
    try:
        minLimbStr = int(raw_input('Select a number between 1 and 100 for the minimum limb strength. '))
        maxLimbStr = int(raw_input('Select a number between ' + str(minLimbStr) + ' and 100 for the maximum limb strength. '))
        if maxLimbStr < minLimbStr:
            setter = minLimbStr
            minLimbStr = maxLimbStr
            maxLimbStr = setter
        if minLimbStr < 0 or maxLimbStr > 100:
            print('There has been an error in your input, values will be randomly generated for you')
            minLimbStr = random.randint(1,100)
            maxLimbStr = random.randint(minLimbStr,100)
        minLimb = int(raw_input('Select a number between 1 and 8 for the minimum number of limbs. '))
        maxLimb = int(raw_input('Select a number between ' + str(minLimb) + ' and 8 for the maximum number of limbs. '))
        if maxLimb < minLimb:
            setter = minLimb
            minLimb = maxLimb
            maxLimb = setter
        if minLimb < 0 or maxLimb > 8:
            print('There has been an error in your input, values will be randomly generated for you')
            minLimbStr = random.randint(1,8)
            maxLimbStr = random.randint(minLimbStr,8)
        if minLimb == maxLimb or minLimbStr == maxLimbStr:
            pro
    except:
        print ('There has been an error in your input, values will be randomly generated for you')
        minLimbStr = random.randint(1,100)
        maxLimbStr = random.randint(minLimbStr,100)
        minLimb = random.randint(1,8)
        maxLimb = random.randint(minLimb,8)
    limbValues = [minLimbStr, maxLimbStr, minLimb, maxLimb]
    return limbValues


def collectAppendageValues():
    try:
        minAppendageStr = int(raw_input('Select a number between 1 and 100 for the minimum appendage strength. '))
        maxAppendageStr = int(raw_input('Select a number between ' + str(minAppendageStr) + ' and 100 for the maximum appendage strength. '))
        if maxAppendageStr < minAppendageStr:
            setter = minAppendageStr
            minAppendageStr = maxAppendageStr
            maxAppendageStr = setter
        if minAppendageStr < 0 or maxAppendageStr > 100:
            print('There has been an error in your input, values will be randomly generated for you')
            minAppendageStr = random.randint(1,100)
            maxAppendageStr = random.randint(minAppendageStr,100)
        minAppendage = int(raw_input('Select a number between 1 and 3 for the minimum number of appendages. '))
        maxAppendage = int(raw_input('Select a number between ' + str(minAppendage) + ' and 3 for the maximum number of appendages. '))
        if maxAppendage < minAppendage:
            setter = minAppendage
            minAppendage = maxAppendage
            maxAppendage = setter
        if minAppendage < 0 or maxAppendage > 3:
            print('There has been an error in your input, values will be randomly generated for you')
            minAppendageStr = random.randint(1,3)
            maxAppendageStr = random.randint(minLimbStr,3)
    except:
        print ('There has been an error in your input, values will be randomly generated for you')
        minAppendageStr = random.randint(1,100)
        maxAppendageStr = random.randint(minAppendageStr,100)
        minAppendage = random.randint(1,3)
        maxAppendage = random.randint(minAppendage,3)
    appendageValues = [minAppendageStr, maxAppendageStr, minAppendage, maxAppendage]
    return appendageValues
    

def collectPhalangeValues():
    try:
        minPhalangeStr = int(raw_input('Select a number between 1 and 100 for the minimum phalange strength.'))
        maxPhalangeStr = int(raw_input('Select a number between ' + str(minPhalangeStr) + ' and 100 for the maximum phalange strength.'))
        if maxPhalangeStr < minPhalangeStr:
            setter = minPhalangeStr
            minPhalangeStr = maxPhalangeStr
            maxPhalangeStr = setter
        if minPhalangeStr < 0 or maxPhalangeStr > 100:
            print('There has been an error in your input, values will be randomly generated for you')
            minPhalangeStr = random.randint(1,100)
            maxPhalangeStr = random.randint(minPhalangeStr,100)
        minPhalange = int(raw_input('Select a number between 1 and 5 for the minimum number of phalanges.'))
        maxPhalange = int(raw_input('Select a number between ' + str(minPhalange) + ' and 5 for the maximum number of phalanges.'))
        if maxPhalange < minPhalange:
            setter = minPhalange
            minPhalange = maxPhalange
            maxPhalange = setter
        if minPhalange < 0 or maxPhalange > 5:
            print('There has been an error in your input, values will be randomly generated for you')
            minPhalangeStr = random.randint(1,5)
            maxPhalangeStr = random.randint(minPhalangeStr,5)
    except:
        print ('There has been an error in your input, values will be randomly generated for you')
        minPhalangeStr = random.randint(1,100)
        maxPhalangeStr = random.randint(minPhalangeStr,100)
        minPhalange = random.randint(1,5)
        maxPhalange = random.randint(minPhalange,5)
    phalangeValues = [minPhalangeStr, maxPhalangeStr, minPhalange, maxPhalange]
    return phalangeValues


def createCreature():
    limbValues = collectLimbValues()
    minLimbStr = limbValues[0]
    maxLimbStr = limbValues[1]
    minLimb = limbValues[2]
    maxLimb = limbValues[3]
    appendageValues = collectAppendageValues()
    minAppendageStr = appendageValues[0]
    maxAppendageStr = appendageValues[1]
    minAppendage = appendageValues[2]
    maxAppendage = appendageValues[3]
    phalangeValues = collectPhalangeValues()
    minPhalangeStr = phalangeValues[0]
    maxPhalangeStr = phalangeValues[1]
    minPhalange = phalangeValues[2]
    maxPhalange = phalangeValues[3]
    return (minLimbStr, maxLimbStr, minLimb, maxLimb, minAppendageStr, maxAppendageStr, minAppendage, maxAppendage, minPhalangeStr, maxPhalangeStr, minPhalange, maxPhalange)


def creatureCreation(minLimbStr, maxLimbStr, minLimb, maxLimb, minAppendageStr, maxAppendageStr, minAppendage, maxAppendage, minPhalangeStr, maxPhalangeStr, minPhalange, maxPhalange):
    limbColorAvg = []
    appendageColorAvg = []
    phalangeColorAvg = []
    limbList = []
    limbStrList = []
    availLimbPos = range(1, 9)
    for i in range(random.randint(minLimb,maxLimb)):     # Gathers Limb Positions and Limb Strengths
        str = random.randint(minLimbStr, maxLimbStr)
        pos = random.choice(availLimbPos)
        availLimbPos.remove(pos)
        limbList.append(pos)
        limbStrList.append(str)
        limbColorAvg.append(2.4 * str + 15)
        appendageList= []
        appendageStrList = []
        availAppendagePos = range(1, 4)
        for i in range(random.randint(minAppendage, maxAppendage)):   # Gathers Appendage Positions and Appendage Strengths
            str = random.randint(minAppendageStr, maxAppendageStr)
            pos = random.choice(availAppendagePos)
            availAppendagePos.remove(pos)
            appendageList.append(pos)
            appendageStrList.append(str)
            appendageColorAvg.append(2.4 * str + 5)
            phalangeList = []
            phalangeStrList = []
            availPhalangePos = range(1, 6)
            for i in range(random.randint(minPhalange, maxPhalange)):    # Gathers Phalange Positions and Phalange Strengths
                str = random.randint(minPhalangeStr, maxPhalangeStr)
                pos = random.choice(availPhalangePos)
                availPhalangePos.remove(pos)
                phalangeList.append(pos)
                phalangeStrList.append(str)
                phalangeColorAvg.append(2.4 * str + 5)
            appendageList.append(phalangeList)    # Adds phalanges inside of appendage list
            appendageStrList.append(phalangeStrList)    # Same for strengths
        limbList.append(appendageList)    # Adds appendages and phalanges inside of limb list
        limbStrList.append(appendageStrList)    # Same for strengths
    colorValues = (limbColorAvg, appendageColorAvg, phalangeColorAvg)
    return (limbList, limbStrList, colorValues)
            
            
class Creature():
    
    def __init__(self):
        print ('Welcome to the Creature Interface, commands can be found with Creature.help()')
        
    def help(self):
        print ('This is the help tab, list of commands and what they do can be found here')
        print "There are 3 commands, create(), createMoved(), and createMultiple()"
        
    def create(self):
        root = tk.Tk()
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight() - 50
        window = Canvas(Tk(), width= screenWidth, height= screenHeight,background= "black")
        window.pack()
        mover = screenWidth/2
        bodyXAnchor = screenWidth /2
        bodyYAnchor = screenHeight / 2
        limbDistance = mover/4
        appendageDistance = limbDistance/2
        phalangeDistance = limbDistance/6
        limbWidth = limbDistance/10
        appendageWidth = limbWidth/2
        phalangeWidth = appendageWidth/2
        if raw_input('Would You Like To Customize Limits? ') == 'Yes':
            maxMinValues = createCreature()
        else:
            maxMinValues = (0,100,1,8,0,100,1,3,0,100,1,5)
        values = creatureCreation(maxMinValues[0], maxMinValues[1], maxMinValues[2], maxMinValues[3], maxMinValues[4], maxMinValues[5], maxMinValues[6], maxMinValues[7], maxMinValues[8], maxMinValues[9], maxMinValues[10], maxMinValues[11],)
        limbList = values[0]
        limbStrList = values[1]
        bodyColor = values[2]
        drawCreature(limbList, limbStrList, (limbDistance, appendageDistance, phalangeDistance), (limbWidth, appendageWidth, phalangeWidth),(bodyXAnchor, bodyYAnchor), window, bodyColor)
        mainloop()
        
    def createMoved(self):
        root = tk.Tk()
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight() - 50
        window = Canvas(Tk(), width= screenWidth, height= screenHeight,background= "black")
        window.pack()
        mover = screenWidth/2
        bodyXAnchor = screenWidth /2
        bodyYAnchor = screenHeight / 2
        limbDistance = mover/4
        appendageDistance = limbDistance/2
        phalangeDistance = limbDistance/6
        limbWidth = limbDistance/10
        appendageWidth = limbWidth/2
        phalangeWidth = appendageWidth/2
        if raw_input('Would You Like To Customize Limits? ') == 'Yes':
            maxMinValues = createCreature()
        else:
            maxMinValues = (0,100,1,8,0,100,1,3,0,100,1,5)
        values = creatureCreation(maxMinValues[0], maxMinValues[1], maxMinValues[2], maxMinValues[3], maxMinValues[4], maxMinValues[5], maxMinValues[6], maxMinValues[7], maxMinValues[8], maxMinValues[9], maxMinValues[10], maxMinValues[11],)
        limbList = values[0]
        limbStrList = values[1]
        bodyColor = values[2]
        drawMovedCreature(limbList, limbStrList, (limbDistance, appendageDistance, phalangeDistance), (limbWidth, appendageWidth, phalangeWidth),(bodyXAnchor, bodyYAnchor), window, bodyColor)
        mainloop()
        
    def createMultiple(self):
        root = tk.Tk()
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight() - 50
        window = Canvas(Tk(), width= screenWidth, height= screenHeight,background= "black")
        window.pack()
        creatureNumber = collectCreatureNumber()
        mover = screenWidth/(creatureNumber*2)
        bodyXAnchor = mover
        bodyYAnchor = screenHeight - mover
        limbDistance = mover/4
        appendageDistance = limbDistance/2
        phalangeDistance = limbDistance/6
        limbWidth = limbDistance/10
        appendageWidth = limbWidth/2
        phalangeWidth = appendageWidth/2
        if raw_input('Would You Like To Customize Limits? ') == 'Yes':
            maxMinValues = createCreature()
        else:
            maxMinValues = (0,100,1,8,0,100,1,3,0,100,1,5)
        for i in range(creatureNumber):
            if bodyXAnchor + mover + limbDistance + appendageDistance + phalangeDistance < screenWidth:    # Changes x movement
                bodyXAnchor += mover
            else:                               # Changes y movement
                bodyXAnchor = mover
                bodyYAnchor += mover
            values = creatureCreation(maxMinValues[0], maxMinValues[1], maxMinValues[2], maxMinValues[3], maxMinValues[4], maxMinValues[5], maxMinValues[6], maxMinValues[7], maxMinValues[8], maxMinValues[9], maxMinValues[10], maxMinValues[11],)
            limbList = values[1]
            limbStrList = values[2]
            bodyColor = values[3]
            drawCreature(limbList, limbStrList, (limbDistance, appendageDistance, phalangeDistance), (limbWidth, appendageWidth, phalangeWidth),(bodyXAnchor, bodyYAnchor), window, bodyColor)
        mainloop()
print "Welcome to the evolution simulator, enter 'A Name' = Creature() to start"

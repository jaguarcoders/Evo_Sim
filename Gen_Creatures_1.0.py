import random
from Tkinter import *
import Tkinter as tk
import math
from collections import namedtuple

def gen_name():     #Random Name Generator
    NAME = ''
    cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z','y']
    h_cons = ['c','t','s','p']
    l_cons = ['c','b','f','g','p','s']
    r_cons = ['b','c','f','g','p','t','w']
    vowels = ['a','e','i','o','u']
    if random.randint(1,5) == 1:
        letter = random.choice(vowels)
    else:
        letter = random.choice(cons)
    NAME += letter
    for i in range(random.randint(4,7)):
        if NAME[-1] not in vowels:
            if NAME[-1] not in h_cons:
                if NAME[-1] not in l_cons:
                    if NAME[-1] not in r_cons:
                        NAME += random.choice(vowels)
                    else:
                        NAME += 'r'
                else:
                    if NAME[-1] in r_cons:
                        if random.randint(1,5) == 1:
                            NAME += 'r'
                        else:
                            NAME += 'l'
                    else:
                        if random.randint(1,5) == 1:
                            NAME += 'l'
                        else:
                            NAME += random.choice(vowels)
            else:        
                if random.randint(1,5) == 1:
                    NAME += 'h'
                else:
                    if NAME[-1] in r_cons:
                        if NAME[-1] in l_cons:
                            if random.randint(1,5) == 1:
                                NAME += 'l'
                            else:
                                NAME += random.choice(vowels)
                        if random.randint(1,5) == 1:
                            NAME += 'r'
                        else:
                            NAME += random.choice(vowels)
                    else:
                        if NAME[-1] in l_cons:
                            if random.randint(1,5) == 1:
                                NAME += 'l'
                            else:
                                NAME += random.choice(vowels)
        else:
            if NAME[-1] in ['eo']:
                if NAME[-1] != NAME[-2]:
                    if random.randint(1,5) == 1:
                        NAME += NAME[-1]
                    else:
                        NAME += random.choice(cons)
            else:
                NAME += random.choice(cons)
    return NAME

def draw_creature(bodypart_pos, bodypart_str, body_color, distances, width, body_anchor, window):
    limb_stepper = 0
    appendage_stepper = 0
    phalange_stepper = 0
    for i in range(len(bodypart_pos)):
            if limb_stepper % 2 == 0 or limb_stepper == 0:
                limb_angle = (45*bodypart_pos[limb_stepper]) - 45
                limb_x_anchor = body_anchor[0] + ((distances[0])*(math.sin((math.pi/180)*limb_angle)))
                limb_y_anchor = body_anchor[1] + ((distances[0])*(math.sin((math.pi/180)*(limb_angle - 90))))
                limb_color = '#%02x%02x%02x' % (bodypart_str[limb_stepper] + 155, 0, 0)
                window.create_line(body_anchor[0], body_anchor[1], limb_x_anchor, limb_y_anchor, width= width[0], fill= limb_color)
            else:
                for i in range(len(bodypart_pos[limb_stepper])):
                    if appendage_stepper % 2 == 0 or appendage_stepper == 0:
                        appendage_angle = ((45*bodypart_pos[limb_stepper][appendage_stepper]) - 90) + limb_angle
                        appendage_x_anchor = limb_x_anchor + (distances[1]*(math.sin((math.pi/180)*(appendage_angle))))
                        appendage_y_anchor = limb_y_anchor + (distances[1]*(math.sin((math.pi/180)*(appendage_angle - 90))))
                        appendage_color = '#%02x%02x%02x' % (0, bodypart_str[limb_stepper][appendage_stepper] + 155, 0)
                        window.create_line(limb_x_anchor,limb_y_anchor,appendage_x_anchor,appendage_y_anchor,width= width[1], fill= appendage_color)
                    else:
                        for i in range(len(bodypart_pos[limb_stepper][appendage_stepper])):
                            phalange_angle = ((45*bodypart_pos[limb_stepper][appendage_stepper][phalange_stepper]) - 135) + appendage_angle
                            phalange_x_anchor = appendage_x_anchor + (distances[2]*(math.sin((math.pi/180)*(phalange_angle))))
                            phalange_y_anchor = appendage_y_anchor + (distances[2]*(math.sin((math.pi/180)*(phalange_angle - 90))))
                            phalange_color = '#%02x%02x%02x' % ((0, 0, bodypart_str[limb_stepper][appendage_stepper][phalange_stepper] + 155))
                            window.create_line(appendage_x_anchor,appendage_y_anchor,phalange_x_anchor,phalange_y_anchor,width= width[2], fill= phalange_color)
                            window.create_oval(phalange_x_anchor + (width[2]/2) - 1, phalange_y_anchor + (width[2]/2) - 1, phalange_x_anchor - (width[2]/2) + 1, phalange_y_anchor - (width[2]/2) + 1, fill= phalange_color, outline= phalange_color)
                            phalange_stepper += 1
                        phalange_stepper = 0
                        window.create_oval([appendage_x_anchor + (width[1]/2)], [appendage_y_anchor + (width[1]/2)], [appendage_x_anchor - (width[1]/2)], [appendage_y_anchor - (width[1]/2)], fill= appendage_color, outline= appendage_color)
                    appendage_stepper += 1
                appendage_stepper = 0
                window.create_oval([limb_x_anchor + (width[0]/2)], [limb_y_anchor + (width[0]/2)], [limb_x_anchor - (width[0]/2)], [limb_y_anchor - (width[0]/2)], fill=  '#%02x%02x%02x' % (bodypart_str[limb_stepper - 1] + 155, 0, 0), outline= '#%02x%02x%02x' % (bodypart_str[limb_stepper - 1] + 155, 0, 0))
            limb_stepper += 1
    avg_color = '#%02x%02x%02x' % ((sum(body_color[0])/(len(body_color[0]))), (sum(body_color[1])/(len(body_color[1]))), (sum(body_color[2])/(len(body_color[2]))))
    window.create_oval(body_anchor[0] + width[0], body_anchor[1] + width[0], body_anchor[0] - width[0], body_anchor[1] - width[0], fill= avg_color, outline= avg_color)

Creature = namedtuple('Creature', ['Name', 'Id', 'Bodyparts', 'Strengths'])

def collect_creature_number():
    try:
        creatures = raw_input('Do you want creature size or creature number?')
        if creatures == 'size' or creatures == 'creature size':
            creature_size = raw_input('What size, S, M, or L?')
            if creature_size == 'S':
                creature_num = 1350
            elif creature_size == 'M':
                creature_num = 325
            elif creature_size == 'L':
                creature_num = 10
            else:
                print ('That was not a value from the list, value will be selected for you.')
                creature_num = random.choice(1350,325,10)
        elif creatures == 'number' or creatures == 'creature number':
            creature_number = int(raw_input('How many do you want?'))
            if creature_number < 0:
                print ('Your number needs to be greater than one, randomly selecting creature number')
                creature_num = random.randint(10,1350)
    except:
        print ('There has been an error in your input, values will be randomly generated for you')
        creature_num = random.randint(10,1350)
    return creature_num

def collect_limb_values():
    try:
        min_limb_str = int(raw_input('Select a number between 1 and 100 for the minimum limb strength.'))
    except:
        print ('There has been an error in your input, values will be randomly generated for you')
        min_limb_str = random.randint(1,100)
        max_limb_str = random.randint(min_limb_str,100)
        min_limb = random.randint(1,8)
        max_limb = random.randint(min_limb,8)

def create_creatures(creature_size, min_limb_str, max_limb_str, min_limb, max_limb, min_appendage_str, max_appendage_str, min_appendage, max_appendage, min_phalange_str, max_phalange_str, max_phalange, max_phalange, prnt):
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() - 50
    window = Canvas(Tk(), width= screen_width, height= screen_height,background= "black")
    window.pack()
    collect_creature_number()
    collect_limb_values()
    collect_appendage_values()
    collect_phalange_values()
    try:
        prnt = int(raw_input('Do you want to see body part values? 1 for yes, 0 for no.'))
    except:
        print ('Unknown error, values will not be given')
        prnt = 0
    mover = screen_width/(-16.82583717 + (8.53116841(math.log(creature_number))))
    creature_id = 0
    body_x_anchor = mover*-.5
    body_y_anchor = mover*.5
    limb_distance = mover/4
    appendage_distance = limb_distance/2
    phalange_distance = limb_distance/6
    limb_width = limb_distance/10
    appendage_width = limb_width/2
    phalange_width = appendage_width/2
    for i in range(creature_num):
        gen_name(0)
        creature_id += 1
        limb_color_avg = []
        appendage_color_avg = []
        phalange_color_avg = []
        limb_list = []
        limb_str_list = []
        avail_limb_pos = range(1, 9)
        if body_x_anchor + mover + limb_distance + appendage_distance + phalange_distance < screen_width:    # Changes x movement
            body_x_anchor += mover
        else:                               # Changes y movement
            body_x_anchor = mover/2
            body_y_anchor += mover
        for i in range(random.randint(1,max_limb)):     # Gathers Limb Positions and Limb Strengths
            str = random.randint(min_phalange_str, max_phalange_str)
            pos = random.choice(avail_limb_pos)
            avail_limb_pos.remove(pos)
            limb_list.append(pos)
            limb_str_list.append(str)
            limb_color_avg.append(str + 155)
            appendage_list= []
            appendage_str_list = []
            avail_appendage_pos = range(1, 4)
            for i in range(random.randint(1, max_appendage)):   # Gathers Appendage Positions and Appendage Strengths
                str = random.randint(min_phalange_str, max_phalange_str)
                pos = random.choice(avail_appendage_pos)
                avail_appendage_pos.remove(pos)
                appendage_list.append(pos)
                appendage_str_list.append(str)
                appendage_color_avg.append(str + 155)
                phalange_list = []
                phalange_str_list = []
                avail_phalange_pos = range(1, max_phalange + 1)
                for i in range(random.randint(1, max_phalange)):    # Gathers Phalange Positions and Phalange Strengths
                    str = random.randint(min_phalange_str, max_phalange_str)
                    pos = random.choice(avail_phalange_pos)
                    avail_phalange_pos.remove(pos)
                    phalange_list.append(pos)
                    phalange_str_list.append(str)
                    phalange_color_avg.append(str + 155)
                appendage_list.append(phalange_list)    # Adds phalanges inside of appendage list
                appendage_str_list.append(phalange_str_list)    # Same for strengths
            limb_list.append(appendage_list)    # Adds appendages and phalanges inside of limb list
            limb_str_list.append(appendage_str_list)    # Same for strengths
        if prnt == 1:
            print (Creature(NAME, creature_id, limb_list, limb_str_list))
        draw_creature(limb_list, limb_str_list, (limb_color_avg, appendage_color_avg, phalange_color_avg), (limb_distance, appendage_distance, phalange_distance), (limb_width, appendage_width, phalange_width), (body_x_anchor, body_y_anchor), window)
    mainloop()

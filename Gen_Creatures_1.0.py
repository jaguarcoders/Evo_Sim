import random
from Tkinter import *
import math
from collections import namedtuple
import matplotlib.colors as colors
NAME = ''
def gen_name(prnt):
    global NAME
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
                        NAME += random.choice(vowels)
            else:        
                NAME += 'h'
        else:
            if NAME[-1] in ['eo']:
                if NAME[-1] != NAME[-2]:
                    if random.randint(1,3) == 1:
                        NAME += NAME[-1]
            else:
                NAME += random.choice(cons)
    if prnt == 1:
        print NAME
Creature = namedtuple('Creature', ['Name', 'Id', 'Bodyparts', 'Strengths'])
def create_creatures(creature_number, min_limb_str, max_limb_str, max_limb, min_appendage_str, max_appendage_str,max_appendage, min_phalange_str, max_phalange_str, max_phalange):
    creature_id = 0
    w = Canvas(Tk(), width=1600, height=900, background= "black")
    w.pack()
    mover = 100
    body_x_anchor = -50
    body_y_anchor = 50
    for i in range(creature_number):
        gen_name(0)
        creature_id += 1
        limb_color_avg = []
        appendage_color_avg = []
        phalange_color_avg = []
        limb_list = []
        limb_str_list = []
        if body_x_anchor < 1600 - mover:
            body_x_anchor += mover
        else:
            body_y_anchor += mover
            body_x_anchor = 50
        avail_limb_pos = range(1, max_limb + 1)
        for i in range(random.randint(1,max_limb)):
            str = random.randint(min_phalange_str, max_phalange_str)
            pos = random.choice(avail_limb_pos)
            avail_limb_pos.remove(pos)
            limb_list.append(pos)
            limb_str_list.append(str)
            limb_color_avg.append(str + 155)
            appendage_list= []
            appendage_str_list = []
            limb_stepper = 0
            appendage_stepper = 0
            phalange_stepper = 0
            limb_distance = 100/4
            appendage_distance = 50/4
            phalange_distance = 20/4
            limb_width = 12/4
            appendage_width = 6/4
            phalange_width = 3/4
            avail_appendage_pos = range(1, max_appendage + 1)
            for i in range(random.randint(1, max_appendage)):
                str = random.randint(min_phalange_str, max_phalange_str)
                pos = random.choice(avail_appendage_pos)
                avail_appendage_pos.remove(pos)
                appendage_list.append(pos)
                appendage_str_list.append(str)
                appendage_color_avg.append(str + 155)
                phalange_list = []
                phalange_str_list = []
                avail_phalange_pos = range(1, max_phalange + 1)
                for i in range(random.randint(1, max_phalange)):
                    str = random.randint(min_phalange_str, max_phalange_str)
                    pos = random.choice(avail_phalange_pos)
                    avail_phalange_pos.remove(pos)
                    phalange_list.append(pos)
                    phalange_str_list.append(str)
                    phalange_color_avg.append(str + 155)
                appendage_list.append(phalange_list)
                appendage_str_list.append(phalange_str_list)
            limb_list.append(appendage_list)
            limb_str_list.append(appendage_str_list)
        print (Creature(NAME, creature_id, limb_list, limb_str_list))
        for i in range(len(limb_list)):
            if limb_stepper % 2 == 0 or limb_stepper == 0:
                limb_angle = (45*limb_list[limb_stepper]) - 45
                limb_x_anchor = body_x_anchor + (limb_distance*(math.sin((math.pi/180)*limb_angle)))
                limb_y_anchor = body_y_anchor + (limb_distance*(math.sin((math.pi/180)*(limb_angle - 90))))
                w.create_line(body_x_anchor, body_y_anchor, limb_x_anchor, limb_y_anchor, width= limb_width, fill=  '#%02x%02x%02x' % (limb_str_list[limb_stepper] + 155, 0, 0))
            else:
                for i in range(len(limb_list[limb_stepper])):
                    if appendage_stepper % 2 == 0 or appendage_stepper == 0:
                        appendage_angle = limb_angle + ((45*limb_list[limb_stepper][appendage_stepper]) - 90)
                        appendage_x_anchor = limb_x_anchor + (appendage_distance*(math.sin((math.pi/180)*(appendage_angle))))
                        appendage_y_anchor = limb_y_anchor + (appendage_distance*(math.sin((math.pi/180)*(appendage_angle - 90))))
                        w.create_line(limb_x_anchor,limb_y_anchor,appendage_x_anchor,appendage_y_anchor,width= appendage_width, fill=  '#%02x%02x%02x' % (0, limb_str_list[limb_stepper][appendage_stepper] + 155, 0))
                    else:
                        for i in range(len(limb_list[limb_stepper][appendage_stepper])):
                            phalange_angle = appendage_angle + ((45*limb_list[limb_stepper][appendage_stepper][phalange_stepper]) - 135)
                            phalange_x_anchor = appendage_x_anchor + (phalange_distance*(math.sin((math.pi/180)*(phalange_angle))))
                            phalange_y_anchor = appendage_y_anchor + (phalange_distance*(math.sin((math.pi/180)*(phalange_angle - 90))))
                            w.create_line(appendage_x_anchor,appendage_y_anchor,phalange_x_anchor,phalange_y_anchor,width= phalange_width, fill=  '#%02x%02x%02x' % (0, 0, limb_str_list[limb_stepper][appendage_stepper][phalange_stepper] + 155))
                            phalange_stepper += 1
                        phalange_stepper = 0
                    appendage_stepper += 1
                appendage_stepper = 0
            limb_stepper += 1
        limb_stepper = 0
        w.create_oval(body_x_anchor + limb_width, body_y_anchor + limb_width, body_x_anchor - limb_width, body_y_anchor - limb_width,fill= '#%02x%02x%02x' % ((sum(limb_color_avg)/(len(limb_color_avg))), (sum(appendage_color_avg)/(len(appendage_color_avg))), (sum(phalange_color_avg)/(len(phalange_color_avg)))), outline= '#%02x%02x%02x' % ((sum(limb_color_avg)/(len(limb_color_avg))), (sum(appendage_color_avg)/(len(appendage_color_avg))), (sum(phalange_color_avg)/(len(phalange_color_avg)))))
    mainloop()

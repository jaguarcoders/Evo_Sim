import random
from Tkinter import *
import Tkinter as tk
import math


def gen_name():     #Random Name Generator
    name = ''
    cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z','y']
    h_cons = ['c','t','s','p']
    l_cons = ['c','b','f','g','p','s']
    r_cons = ['b','c','f','g','p','t','w']
    vowels = ['a','e','i','o','u']
    if random.randint(1,5) == 1:
        letter = random.choice(vowels)
    else:
        letter = random.choice(cons)
    name += letter
    for i in range(random.randint(4,7)):
        if name[-1] not in vowels:
            if name[-1] not in h_cons:
                if name[-1] not in l_cons:
                    if name[-1] not in r_cons:
                        name += random.choice(vowels)
                    else:
                        if random.randint(1,5) == 1:    
                            name += 'r'
                        else:
                            name += random.choice(vowels)
                else:
                    if name[-1] in r_cons:
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
                    if name[-1] in r_cons:
                        if name[-1] in l_cons:
                            if random.randint(1,5) == 1:
                                name += 'l'
                            else:
                                name += random.choice(vowels)
                        if random.randint(1,5) == 1:
                            name += 'r'
                        else:
                            name += random.choice(vowels)
                    else:
                        if name[-1] in l_cons:
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


def draw_creature(bodypart_pos, bodypart_str, distances, width, body_anchor, window, body_color):
    for limb_num in range(len(bodypart_pos)):
            if limb_num % 2 == 0 or limb_num == 0:
                limb_angle = (45*bodypart_pos[limb_num]) - 45
                limb_x_anchor = body_anchor[0] + ((distances[0])*(math.sin((math.pi/180)*limb_angle)))
                limb_y_anchor = body_anchor[1] + ((distances[0])*(math.sin((math.pi/180)*(limb_angle - 90))))
                limb_color = '#%02x%02x%02x' % (bodypart_str[limb_num] + 155, 0, 0)
                window.create_line(body_anchor[0], body_anchor[1], limb_x_anchor, limb_y_anchor, width= width[0], fill= limb_color)
            else:
                for appendage_num in range(len(bodypart_pos[limb_num])):
                    if appendage_num % 2 == 0 or appendage_num == 0:
                        appendage_angle = ((45*bodypart_pos[limb_num][appendage_num]) - 90) + limb_angle
                        appendage_x_anchor = limb_x_anchor + (distances[1]*(math.sin((math.pi/180)*(appendage_angle))))
                        appendage_y_anchor = limb_y_anchor + (distances[1]*(math.sin((math.pi/180)*(appendage_angle - 90))))
                        appendage_color = '#%02x%02x%02x' % (0, bodypart_str[limb_num][appendage_num] + 155, 0)
                        window.create_line(limb_x_anchor,limb_y_anchor,appendage_x_anchor,appendage_y_anchor,width= width[1], fill= appendage_color)
                    else:
                        for phalange_num in range(len(bodypart_pos[limb_num][appendage_num])):
                            phalange_angle = ((45*bodypart_pos[limb_num][appendage_num][phalange_num]) - 135) + appendage_angle
                            phalange_x_anchor = appendage_x_anchor + (distances[2]*(math.sin((math.pi/180)*(phalange_angle))))
                            phalange_y_anchor = appendage_y_anchor + (distances[2]*(math.sin((math.pi/180)*(phalange_angle - 90))))
                            phalange_color = '#%02x%02x%02x' % ((0, 0, bodypart_str[limb_num][appendage_num][phalange_num] + 155))
                            window.create_line(appendage_x_anchor,appendage_y_anchor,phalange_x_anchor,phalange_y_anchor,width= width[2], fill= phalange_color)
                            window.create_oval(phalange_x_anchor + (width[2]/2) - 1, phalange_y_anchor + (width[2]/2) - 1, phalange_x_anchor - (width[2]/2) + 1, phalange_y_anchor - (width[2]/2) + 1, fill= phalange_color, outline= phalange_color)
                        window.create_oval([appendage_x_anchor + (width[1]/2)], [appendage_y_anchor + (width[1]/2)], [appendage_x_anchor - (width[1]/2)], [appendage_y_anchor - (width[1]/2)], fill= appendage_color, outline= appendage_color)
                window.create_oval([limb_x_anchor + (width[0]/2)], [limb_y_anchor + (width[0]/2)], [limb_x_anchor - (width[0]/2)], [limb_y_anchor - (width[0]/2)], fill=  '#%02x%02x%02x' % (bodypart_str[limb_num - 1] + 155, 0, 0), outline= '#%02x%02x%02x' % (bodypart_str[limb_num - 1] + 155, 0, 0))
    avg_color = '#%02x%02x%02x' % ((sum(body_color[0])/(len(body_color[0]))), (sum(body_color[1])/(len(body_color[1]))), (sum(body_color[2])/(len(body_color[2]))))
    window.create_oval(body_anchor[0] + width[0], body_anchor[1] + width[0], body_anchor[0] - width[0], body_anchor[1] - width[0], fill= avg_color, outline= avg_color)
    

def collect_creature_number():
    try:
        creature_num = int(raw_input('How many creatures do you want? '))
        if creature_num < 0:
            print ('Your number needs to be greater than one, randomly selecting creature number')
            creature_num = random.randint(10,1350)
    except:
        print ('There has been an error in your input, values will be randomly generated for you')
        creature_num = random.randint(10,1350)
    return creature_num


def collect_limb_values():
    try:
        min_limb_str = int(raw_input('Select a number between 1 and 100 for the minimum limb strength. '))
        max_limb_str = int(raw_input('Select a number between ' + str(min_limb_str) + ' and 100 for the maximum limb strength. '))
        if max_limb_str < min_limb_str:
            setter = min_limb_str
            min_limb_str = max_limb_str
            max_limb_str = setter
        if min_limb_str < 0 or max_limb_str > 100:
            print('There has been an error in your input, values will be randomly generated for you')
            min_limb_str = random.randint(1,100)
            max_limb_str = random.randint(min_limb_str,100)
        min_limb = int(raw_input('Select a number between 1 and 8 for the minimum number of limbs. '))
        max_limb = int(raw_input('Select a number between ' + str(min_limb) + ' and 8 for the maximum number of limbs. '))
        if max_limb < min_limb:
            setter = min_limb
            min_limb = max_limb
            max_limb = setter
        if min_limb < 0 or max_limb > 8:
            print('There has been an error in your input, values will be randomly generated for you')
            min_limb_str = random.randint(1,8)
            max_limb_str = random.randint(min_limb_str,8)
        if min_limb == max_limb or min_limb_str == max_limb_str:
            pro
    except:
        print ('There has been an error in your input, values will be randomly generated for you')
        min_limb_str = random.randint(1,100)
        max_limb_str = random.randint(min_limb_str,100)
        min_limb = random.randint(1,8)
        max_limb = random.randint(min_limb,8)
    limb_values = [min_limb_str, max_limb_str, min_limb, max_limb]
    return limb_values


def collect_appendage_values():
    try:
        min_appendage_str = int(raw_input('Select a number between 1 and 100 for the minimum appendage strength. '))
        max_appendage_str = int(raw_input('Select a number between ' + str(min_appendage_str) + ' and 100 for the maximum appendage strength. '))
        if max_appendage_str < min_appendage_str:
            setter = min_appendage_str
            min_appendage_str = max_appendage_str
            max_appendage_str = setter
        if min_appendage_str < 0 or max_appendage_str > 100:
            print('There has been an error in your input, values will be randomly generated for you')
            min_appendage_str = random.randint(1,100)
            max_appendage_str = random.randint(min_appendage_str,100)
        min_appendage = int(raw_input('Select a number between 1 and 3 for the minimum number of appendages. '))
        max_appendage = int(raw_input('Select a number between ' + str(min_appendage) + ' and 3 for the maximum number of appendages. '))
        if max_appendage < min_appendage:
            setter = min_appendage
            min_appendage = max_appendage
            max_appendage = setter
        if min_appendage < 0 or max_appendage > 3:
            print('There has been an error in your input, values will be randomly generated for you')
            min_appendage_str = random.randint(1,3)
            max_appendage_str = random.randint(min_limb_str,3)
    except:
        print ('There has been an error in your input, values will be randomly generated for you')
        min_appendage_str = random.randint(1,100)
        max_appendage_str = random.randint(min_appendage_str,100)
        min_appendage = random.randint(1,3)
        max_appendage = random.randint(min_appendage,3)
    appendage_values = [min_appendage_str, max_appendage_str, min_appendage, max_appendage]
    return appendage_values
    

def collect_phalange_values():
    try:
        min_phalange_str = int(raw_input('Select a number between 1 and 100 for the minimum phalange strength.'))
        max_phalange_str = int(raw_input('Select a number between ' + str(min_phalange_str) + ' and 100 for the maximum phalange strength.'))
        if max_phalange_str < min_phalange_str:
            setter = min_phalange_str
            min_phalange_str = max_phalange_str
            max_phalange_str = setter
        if min_phalange_str < 0 or max_phalange_str > 100:
            print('There has been an error in your input, values will be randomly generated for you')
            min_phalange_str = random.randint(1,100)
            max_phalange_str = random.randint(min_phalange_str,100)
        min_phalange = int(raw_input('Select a number between 1 and 5 for the minimum number of phalanges.'))
        max_phalange = int(raw_input('Select a number between ' + str(min_phalange) + ' and 5 for the maximum number of phalanges.'))
        if max_phalange < min_phalange:
            setter = min_phalange
            min_phalange = max_phalange
            max_phalange = setter
        if min_phalange < 0 or max_phalange > 5:
            print('There has been an error in your input, values will be randomly generated for you')
            min_phalange_str = random.randint(1,5)
            max_phalange_str = random.randint(min_phalange_str,5)
    except:
        print ('There has been an error in your input, values will be randomly generated for you')
        min_phalange_str = random.randint(1,100)
        max_phalange_str = random.randint(min_phalange_str,100)
        min_phalange = random.randint(1,5)
        max_phalange = random.randint(min_phalange,5)
    phalange_values = [min_phalange_str, max_phalange_str, min_phalange, max_phalange]
    return phalange_values


def create_creature():
    limb_values = collect_limb_values()
    min_limb_str = limb_values[0]
    max_limb_str = limb_values[1]
    min_limb = limb_values[2]
    max_limb = limb_values[3]
    appendage_values = collect_appendage_values()
    min_appendage_str = appendage_values[0]
    max_appendage_str = appendage_values[1]
    min_appendage = appendage_values[2]
    max_appendage = appendage_values[3]
    phalange_values = collect_phalange_values()
    min_phalange_str = phalange_values[0]
    max_phalange_str = phalange_values[1]
    min_phalange = phalange_values[2]
    max_phalange = phalange_values[3]
    return (min_limb_str, max_limb_str, min_limb, max_limb, min_appendage_str, max_appendage_str, min_appendage, max_appendage, min_phalange_str, max_phalange_str, min_phalange, max_phalange)


def creature_creation(min_limb_str, max_limb_str, min_limb, max_limb, min_appendage_str, max_appendage_str, min_appendage, max_appendage, min_phalange_str, max_phalange_str, min_phalange, max_phalange):
    limb_color_avg = []
    appendage_color_avg = []
    phalange_color_avg = []
    limb_list = []
    limb_str_list = []
    avail_limb_pos = range(1, 9)
    for i in range(random.randint(min_limb,max_limb)):     # Gathers Limb Positions and Limb Strengths
        str = random.randint(min_limb_str, max_limb_str)
        pos = random.choice(avail_limb_pos)
        avail_limb_pos.remove(pos)
        limb_list.append(pos)
        limb_str_list.append(str)
        limb_color_avg.append((.011 * (str**2)) + (.9*str))
        appendage_list= []
        appendage_str_list = []
        avail_appendage_pos = range(1, 4)
        for i in range(random.randint(min_appendage, max_appendage)):   # Gathers Appendage Positions and Appendage Strengths
            str = random.randint(min_appendage_str, max_appendage_str)
            pos = random.choice(avail_appendage_pos)
            avail_appendage_pos.remove(pos)
            appendage_list.append(pos)
            appendage_str_list.append(str)
            appendage_color_avg.append((.011 * (str**2)) + (.9*str))
            phalange_list = []
            phalange_str_list = []
            avail_phalange_pos = range(1, 6)
            for i in range(random.randint(min_phalange, max_phalange)):    # Gathers Phalange Positions and Phalange Strengths
                str = random.randint(min_phalange_str, max_phalange_str)
                pos = random.choice(avail_phalange_pos)
                avail_phalange_pos.remove(pos)
                phalange_list.append(pos)
                phalange_str_list.append(str)
                phalange_color_avg.append((.011 * (str**2)) + (.9*str))
            appendage_list.append(phalange_list)    # Adds phalanges inside of appendage list
            appendage_str_list.append(phalange_str_list)    # Same for strengths
        limb_list.append(appendage_list)    # Adds appendages and phalanges inside of limb list
        limb_str_list.append(appendage_str_list)    # Same for strengths
    color_values = (limb_color_avg, appendage_color_avg, phalange_color_avg)
    return (limb_list, limb_str_list, color_values)
            
            
class Creature():
    
    def __init__(self):
        print ('Welcome to the Creature Interface, commands can be found with Creature.help()')
        
    def help(self):
        print ('This is the help tab, list of commands and what they do can be found here')
        
    def create(self):
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight() - 50
        window = Canvas(Tk(), width= screen_width, height= screen_height,background= "black")
        window.pack()
        mover = screen_width/2
        body_x_anchor = screen_width /2
        body_y_anchor = screen_height / 2
        limb_distance = mover/4
        appendage_distance = limb_distance/2
        phalange_distance = limb_distance/6
        limb_width = limb_distance/10
        appendage_width = limb_width/2
        phalange_width = appendage_width/2
        if raw_input('Would You Like To Customize Limits? ') == 'Yes':
            max_min_values = create_creature()
        else:
            max_min_values = (0,100,1,8,0,100,1,3,0,100,1,5)
        values = creature_creation(max_min_values[0], max_min_values[1], max_min_values[2], max_min_values[3], max_min_values[4], max_min_values[5], max_min_values[6], max_min_values[7], max_min_values[8], max_min_values[9], max_min_values[10], max_min_values[11],)
        limb_list = values[0]
        limb_str_list = values[1]
        body_color = values[2]
        draw_creature(limb_list, limb_str_list, (limb_distance, appendage_distance, phalange_distance), (limb_width, appendage_width, phalange_width),(body_x_anchor, body_y_anchor), window, body_color)
        mainloop()
        
        
    def create_multiple(self):
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight() - 50
        window = Canvas(Tk(), width= screen_width, height= screen_height,background= "black")
        window.pack()
        creature_number = collect_creature_number()
        mover = screen_width/(creature_number*2)
        body_x_anchor = mover
        body_y_anchor = screen_height - mover
        limb_distance = mover/4
        appendage_distance = limb_distance/2
        phalange_distance = limb_distance/6
        limb_width = limb_distance/10
        appendage_width = limb_width/2
        phalange_width = appendage_width/2
        if raw_input('Would You Like To Customize Limits? ') == 'Yes':
            max_min_values = create_creature()
        else:
            max_min_values = (0,100,1,8,0,100,1,3,0,100,1,5)
        for i in range(creature_number):
            if body_x_anchor + mover + limb_distance + appendage_distance + phalange_distance < screen_width:    # Changes x movement
                body_x_anchor += mover
            else:                               # Changes y movement
                body_x_anchor = mover
                body_y_anchor += mover
            values = creature_creation(max_min_values[0], max_min_values[1], max_min_values[2], max_min_values[3], max_min_values[4], max_min_values[5], max_min_values[6], max_min_values[7], max_min_values[8], max_min_values[9], max_min_values[10], max_min_values[11],)
            limb_list = values[1]
            limb_str_list = values[2]
            body_color = values[3]
            draw_creature(limb_list, limb_str_list, (limb_distance, appendage_distance, phalange_distance), (limb_width, appendage_width, phalange_width),(body_x_anchor, body_y_anchor), window, body_color)
        mainloop()

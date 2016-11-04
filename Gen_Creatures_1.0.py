import random
import sys
from collections import namedtuple
Creatures = namedtuple('Creatures', ['name', 'number', 'bodyparts'])
def create_creatures(creature_number, min_limb_str, max_limb_str, max_limb, min_appendage_str, max_appendage_str,max_appendage, min_phalange_str, max_phalange_str, max_phalange):
    creature_id = 0
    for i in range(creature_number):
        name = ''
        for i in range(random.randint(3,8)):
            if random.choice('12') == '1':
                name += random.choice('bcdfghjklmnpqrstvwxyz')
            else:
                name += random.choice('aeiouy')
        creature_id += 1
        limb_list = []
        avail_limb_pos = range(1, max_limb + 1)
        for i in range(random.randint(1,max_limb)):
            str = random.randint(min_phalange_str, max_phalange_str)
            pos = random.choice(avail_limb_pos)
            avail_limb_pos.remove(pos)
            limb_list.append(pos)
            appendage_list= []
            avail_appendage_pos = range(1, max_appendage + 1)
            for i in range(random.randint(1, max_appendage)):
                str = random.randint(min_phalange_str, max_phalange_str)
                pos = random.choice(avail_appendage_pos)
                avail_appendage_pos.remove(pos)
                appendage_list.append(pos)
                phalange_list = []
                avail_phalange_pos = range(1, max_phalange + 1)
                for i in range(random.randint(1, max_phalange)):
                    str = random.randint(min_phalange_str, max_phalange_str)
                    pos = random.choice(avail_phalange_pos)
                    avail_phalange_pos.remove(pos)
                    phalange_list.append(pos)
                appendage_list.append(phalange_list)
            limb_list.append(appendage_list)
        print (Creatures(name, creature_id, limb_list))

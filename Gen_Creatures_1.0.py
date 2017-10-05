else:
            if name[-1] in "eo":
                if len(name) > 1 and name[-1] != name[-2]:
                    if random.randint(1,5) == 1:
                        name += name[-1]
                    else:
                        if random.randint(1,4) == 1:
                            if random.randint(1,3) == 1:
                                name += random.choice(unusualCons)
                            else:
                                name += random.choice(commonCons)
                        else:
                            name += random.choice(frequentCons)
                else:
                    if random.randint(1,4) == 1:
                        if random.randint(1,3) == 1:
                            name += random.choice(unusualCons)
                        else:
                            name += random.choice(commonCons)
                    else:
                        name += random.choice(frequentCons)
            else:
                if random.randint(1,4) == 1:
                    if random.randint(1,3) == 1:
                        name += random.choice(unusualCons)
                    else:
                        name += random.choice(commonCons)
                else:
                    name += random.choice(frequentCons)
    return name

import random
ranwords = []
temp = ""

flag = 0

while flag == 0:
    choice = int(input("Enter 1 to manually input words for the Madlib. Enter 2 for random words to be used: "))
    if choice == 1 or choice == 2:
        flag = 1
    else:
        print("Invalid answer. Please enter 1 or 2 only.")
words = []
enter = []

def exp_ansbank(newlist):
    for x in newlist:
        if x[0] == "a plural noun":
            file = open("pluralnouns.txt", "a")
            file.write("\n")
            file.write(x[1])
            file.close()

        elif x[0] == "an adjective":
            file = open("adjectives.txt", "a")
            file.write("\n")
            file.write(x[1])
            file.close()

        elif x[0] == "a relative":
            file = open("relatives.txt", "a")
            file.write(x[1])
            file.write("\n")
            file.close()
            
        elif x[0] == "a noun":
            file = open("nouns.txt", "a")
            file.write("\n")
            file.write(x[1])
            file.close()

        elif x[0] == "an animal":
            file = open("animals.txt", "a")
            file.write("\n")
            file.write(x[1])
            file.close()

        elif x[0] == "a verb ending in \"ing\"":
            file = open("verbing.txt", "a")
            file.write("\n")
            file.write(x[1])
            file.close()

        elif x[0] == "a vegetable":
            file = open("vegetables.txt", "a")
            file.write(x[1])
            file.write("\n")
            file.close()
            
        elif x[0] == "a verb":
            file = open("verbs.txt", "a")
            file.write("\n")
            file.write(x[1])
            file.close()

        elif x[0] == "a liquid":
            file = open("liquids.txt", "a")
            file.write("\n")
            file.write(x[1])
            file.close()

        elif x[0] == "a profession":
            file = open("professions.txt", "a")
            file.write("\n")
            file.write(x[1])
            file.close()

        elif x[0] == "a place":
            file = open("places.txt", "a")
            file.write("\n")
            file.write(x[1])
            file.close()

        elif x[0] == "a bodypart":
            file = open("bodyparts.txt", "a")
            file.write("\n")
            file.write(x[1])
            file.close()

        elif x[0] == "a name":
            file = open("names.txt", "a")
            file.write("\n")
            file.write(x[1])
            file.close()


def imp_ansbank(words):
    for x in range(0, len(words)):
        temp = ""
        if words[x] == "a plural noun":
            num_lines = sum(1 for line in open('pluralnouns.txt'))
            file = open("pluralnouns.txt", "r")
            for x in file.read():
                if x == "\n" or x == " ":
                    ranwords.append(temp)
                    temp = ""
                else:
                    temp += x
            num =(random.randint(0,len(ranwords)))
            enter.append(ranwords[num])
            file.close()
            ranwords.clear()

        elif words[x] == "an adjective":
            num_lines = sum(1 for line in open('adjectives.txt'))
            file = open("adjectives.txt", "r")
            for x in file.read():
                if x == "\n" or x == " ":
                    ranwords.append(temp)
                    temp = ""
                else:
                    temp += x
            num =(random.randint(0,len(ranwords)))
            enter.append(ranwords[num]) 
            file.close()
            ranwords.clear()

        elif words[x] == "a relative":
            num_lines = sum(1 for line in open('relatives.txt'))
            file = open("relatives.txt", "r")
            for x in file.read():
                if x == "\n" or x == " ":
                    ranwords.append(temp)
                    temp = ""
                else:
                    temp += x
            num =(random.randint(0,len(ranwords)))
            enter.append(ranwords[num]) 
            file.close()
            ranwords.clear()

        elif words[x] == "a noun":
            num_lines = sum(1 for line in open('nouns.txt'))
            file = open("nouns.txt", "r")
            for x in file.read():
                if x == "\n" or x == " ":
                    ranwords.append(temp)
                    temp = ""
                else:
                    temp += x
            num =(random.randint(0,len(ranwords)))
            enter.append(ranwords[num]) 
            file.close()
            ranwords.clear()

        elif words[x] == "an animal":
            num_lines = sum(1 for line in open('animals.txt'))
            file = open("animals.txt", "r")
            for x in file.read():
                if x == "\n" or x == " ":
                    ranwords.append(temp)
                    temp = ""
                else:
                    temp += x
            num =(random.randint(0,len(ranwords)))
            enter.append(ranwords[num]) 
            file.close()
            ranwords.clear()
            
        elif words[x] == "a verb ending in \"ing\"":
            num_lines = sum(1 for line in open('verbing.txt'))
            file = open("verbing.txt", "r")
            for x in file.read():
                if x == "\n" or x == " ":
                    ranwords.append(temp)
                    temp = ""
                else:
                    temp += x
            num =(random.randint(0,len(ranwords)))
            enter.append(ranwords[num]) 
            file.close()
            ranwords.clear()

        elif words[x] == "a vegetable":
            num_lines = sum(1 for line in open('vegetables.txt'))
            file = open("vegetables.txt", "r")
            for x in file.read():
                if x == "\n" or x == " ":
                    ranwords.append(temp)
                    temp = ""
                else:
                    temp += x
            num =(random.randint(0,len(ranwords)))
            enter.append(ranwords[num]) 
            file.close()
            ranwords.clear()

        elif words[x] == "a verb":
            num_lines = sum(1 for line in open('verbs.txt'))
            file = open("verbs.txt", "r")
            for x in file.read():
                if x == "\n" or x == " ":
                    ranwords.append(temp)
                    temp = ""
                else:
                    temp += x
            num =(random.randint(0,len(ranwords)))
            enter.append(ranwords[num]) 
            file.close()
            ranwords.clear()

        elif words[x] == "a liquid":
            num_lines = sum(1 for line in open('liquids.txt'))
            file = open("liquids.txt", "r")
            for x in file.read():
                if x == "\n" or x == " ":
                    ranwords.append(temp)
                    temp = ""
                else:
                    temp += x
            num =(random.randint(0,len(ranwords)))
            enter.append(ranwords[num]) 
            file.close()
            ranwords.clear()

        elif words[x] == "a profession":
            num_lines = sum(1 for line in open('professions.txt'))
            file = open("professions.txt", "r")
            for x in file.read():
                if x == "\n" or x == " ":
                    ranwords.append(temp)
                    temp = ""
                else:
                    temp += x
            num =(random.randint(0,len(ranwords)))
            enter.append(ranwords[num]) 
            file.close()
            ranwords.clear()

        elif words[x] == "a place":
            num_lines = sum(1 for line in open('places.txt'))
            file = open("places.txt", "r")
            for x in file.read():
                if x == "\n" or x == " ":
                    ranwords.append(temp)
                    temp = ""
                else:
                    temp += x
            num =(random.randint(0,len(ranwords)))
            enter.append(ranwords[num]) 
            file.close()
            ranwords.clear()

        elif words[x] == "a bodypart":
            num_lines = sum(1 for line in open('bodyparts.txt'))
            file = open("bodyparts.txt", "r")
            for x in file.read():
                if x == "\n" or x == " ":
                    ranwords.append(temp)
                    temp = ""
                else:
                    temp += x
            num =(random.randint(0,len(ranwords)))
            enter.append(ranwords[num]) 
            file.close()
            ranwords.clear()

        elif words[x] == "a name":
            num_lines = sum(1 for line in open('names.txt'))
            file = open("names.txt", "r")
            for x in file.read():
                if x == "\n" or x == " ":
                    ranwords.append(temp)
                    temp = ""
                else:
                    temp += x
            num =(random.randint(0,len(ranwords)))
            enter.append(ranwords[num]) 
            file.close()
            ranwords.clear()

        elif words[x] == "a number":
            num = random.randint(0,101)
            enter.append(num) 

def story0():
    words = ["a bodypart"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""
Up In %s
"""%(newlist[0][1]))
    newlist = []

def story1():
    words = ["a bodypart"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""
No-%ser
"""%(newlist[0][1]))
    newlist = []

def story2():
    words = ["a noun"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""
%s(s) doesn't Grow On Trees
"""%(newlist[0][1]))
    newlist = []

def story3():
    words = ["an animal"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""
I Smell a %s
"""%(newlist[0][1]))
    newlist = []

def story4():
    words = ["an animal"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""
Playing %s
"""%(newlist[0][1]))
    newlist = []

def story5():
    words = ["a bodypart", "a bodypart"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""
Costs an %s and a %s
"""%(newlist[0][1], newlist[1][1]))
    newlist = []

def story6():
    words = ["an animal", "a verb"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""
Don't Count Your %s Before They %s
"""%(newlist[0][1], newlist[1][1]))
    newlist = []

def story7():
    words = ["a number", "a number"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""
%s down, %s to go
"""%(newlist[0][1], newlist[1][1]))
    newlist = []

def story8():
    words = ["an animal"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""
Wild %s chase 
"""%(newlist[0][1]))
    newlist = []

def story9():
    words = ["a noun"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""
%s in a Haystack
"""%(newlist[0][1]))
    newlist = []

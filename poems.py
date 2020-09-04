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
    words = ["a bodypart", "a noun", "a bodypart", "an adjective", "an adjective"]
    
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
I come with no %s or pretty pink %s. 
I am who I am, from my head to my %s. 
I tend to get %s when speaking my mind. 
Even a little %s some of the time.
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1], newlist[4][1]))
    newlist = []

def story1():
    words = ["a relative", "a verb", "a verb", "a verb"]
    
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
To those %s I've %s with
and to those I don't know your name,
we %s by one another.
You did not %s in vain.
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1]))
    newlist = []

def story2():
    words = ["a name", "a verb", "an adjective", "an adjective"]
    
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
Simple %s was a simple man.
He lived each day by a simple plan.
Enjoy your life and live while you %s.
Make each day %s and always %s.
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1]))
    newlist = []

def story3():
    words = ["an adjective", "an adjective", "a bodypart", "a name"]
    
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
In all %s beauty lies a %s work of art. 
Beautiful but torn, wreaking havoc on my %s.
Camouflaged by insecurities, blinded by it all.
I love the way %s sits there and barely notices me at all.
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1]))
    newlist = []

def story4():
    words = ["a verb", "a name", "a verb", "a name"]
    
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
Someday you will %s for %s
Like I %s for you.
Someday you'll miss %s 
Like I missed you.
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1]))
    newlist = []

def story5():
    words = ["an adjective", "an adjective", "a verb", "a bodypart"]
    
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
Little baby Oh so %s 
One day you will be %s and tall
I watch you while you run and %s
My %s for you grows everyday....
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1]))
    newlist = []

def story6():
    words = ["a bodypart", "a noun", "an adjective", "an adjective", "an adjective"]
    
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
Our %s is like a thorny %s
Not perfect, but always %s
The thorns represent the hardships in our lives. 
The %s petals represent the fun and %s things in our lives.
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1], newlist[4][1]))
    newlist = []

def story7():
    words = ["an animal", "a verb", "an adjective"]
    
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
The %s flies
People %s 
Souls are %s 
Tears dry... 
"""%(newlist[0][1], newlist[1][1], newlist[2][1]))
    newlist = []

def story8():
    words = ["a bodypart", "a noun", "a verb"]
    
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
Open %s and open mind,
On a %s of a lifetime.
Love and respect all,
Get back up when you %s. 
"""%(newlist[0][1], newlist[1][1], newlist[2][1]))
    newlist = []

def story9():
    words = ["a noun", "a verb", "a verb ending in \"ing\"", "a verb ending in \"ing\"", "a place"]
    
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
Wind is like %s
A swaying song it %s
%s away in the summer wind
%s grass in the %s.
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1], newlist[4][1]))
    newlist = []

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

def story1():
    words = ["a plural noun", "a relative", "an adjective", "an adjective", "an adjective", "a noun", "a verb", "an adjective", "an animal", "a noun", "an adjective", "a verb ending in \"ing\"", "a noun", "an adjective", "a noun", "an adjective", "a plural noun", "a vegetable"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""\"Letter to a TV Editor\"

How dumb can network %s be? They cancel an %s
show such as "I'll Be a Monkey's %s" and
replace it with another one of those %s reality shows.
Why don't they take all those %s TV executives, put
them on a desert %s, and leave them there to %s!
Signed: an %s Viewer

Believe me, television is going to the %s I can't
believe the %s they're dishing out. What's being offered to
the %s public is truly mind-%s.
Signed: A Disenchanted %s 

I think today's sitcoms are just as %s as the golden
%s of the past. What needs to be eliminated is the
%s laugh %s.
Signed: A Confirmed Couch %s
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1], newlist[4][1], newlist[5][1], newlist[6][1], newlist[7][1], newlist[8][1], newlist[9][1], newlist[10][1], newlist[11][1], newlist[12][1], newlist[13][1], newlist[14][1], newlist[15][1], newlist[16][1], newlist[17][1]))
    newlist = []

def story2():
    words = ["a name", "a name", "a noun", "a plural noun", "an adjective", "a plural noun","an adjective", "a plural noun", "a noun", "a place", "a plural noun", "a noun", "a profession"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))
        print(enter)

    return print("""\"ALBERT EINSTEIN\"

Albert Einstein, the son of %s and %s,
was born in Ulm, Germany, in 1879. In 1902, he had a job
as assistant %s in the Swiss patent office and attended
the University of Zurich. There he began studying atoms, molecules,
and %s. He developed the theory of
%s relativity, which expanded the phenomena of sub-atomic
%s and %s magnetism. In 1921,
he won the Nobel prize for %s Pand was director of
theoretical physics at the Kaiser Wilhelm %s in Berlin.
In 1933, when Hitler became Chancellor of %s,
Einstein came to America to take a post at Princeton Institute for
%s, where his theories helped America devise the first
atomic %s. There is no question about it: Einstein was
one of the most brilliant %s of our time.
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1], newlist[4][1], newlist[5][1], newlist[6][1], newlist[7][1], newlist[8][1], newlist[9][1], newlist[10][1], newlist[11][1], newlist[12][1]))
    newlist = []

def story3():
    words = ["a noun", "a noun", "a name", "a noun", "a name", "a place", "a noun", "a noun", "a plural noun", "a liquid", "a bodypart", "a plural noun"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""\"Alexander the Great\"

In 356 B.C., Phillip of Macedonia, the ruler of a province in northern
Greece, became the father of a bouncing baby %s
named Alexander. Alexander's teacher was Aristotle, the famous
%s. When he was twenty years old, his father was murdered
by %s, after which he became %s of all
Macedonia. In 334, he invaded Persia and defeated %s
at the battle of %s. Later, at Arbela, he won his most
important victory, over Darius the Third. This made him %s
%s NOUN.over all Persians. Then he marched to India, and
many of his %s died. After that, Alexander began
drinking too much %s, and at the age of 33, he died
of an infection in the %s. His last words are reported
to have been, "There are no more %s to conquer."
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1], newlist[4][1], newlist[5][1], newlist[6][1], newlist[7][1], newlist[8][1], newlist[9][1], newlist[10][1], newlist[11][1]))
    newlist = []

def story4():
    words = ["an adjective", "a noun", "a noun", "a noun", "a noun", "an adjective", "an adjective", "an adjective", "a noun", "a liquid", "a plural noun", "a number", "a bodypart", "a noun", "a noun"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""\"Medical Questions And Answers\"

PATIENT: Doctor, whenever I stand up I get a %s pain
in my %s. Is this serious?

DOCTOR: Sounds as if you have an inflammation of your %s.
You need an anti-%s shot.

PATIENT: Doctor, I'm thinking of having my %s removed.
Is this a %s operation?

DOCTOR: No, the operation is quite %s, providing you
have %s kidneys.

PATIENT: What are the symptoms of an overactive %s?

DOCTOR: High %s pressure. Also, severe %s Pin the abdomen.

PATIENT: Doctor, is it possible for a %s -year-old man to
have a %s attack?

DOCTOR: Only if he doesn't watch his %s and eats too much %s.
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1], newlist[4][1], newlist[5][1], newlist[6][1], newlist[7][1], newlist[8][1], newlist[9][1], newlist[10][1], newlist[11][1], newlist[12][1], newlist[13][1], newlist[14][1]))
    newlist = []

def story5():
    words = ["a bodypart", "a bodypart", "an adjective", "a noun", "a noun", "a verb", "a plural noun", "a noun", "a noun", "a plural noun", "an adjective", "a verb ending in \"ing\"", "an adjective", "a noun", "a noun", "a noun"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""\"The Prom\"

If there's a melody you can't seem to get out of your %s
or a song running through your %s , then bring your
feet to this year's %s prom. As usual, our %s 
will be held in our high school %s. A dress code will be
observed. No one will be admitted wearing %s or
torn %s. Girls must wear a %s and
boys must wear a dress shirt and a %s. As always, hot
%s will be served, and there will be %s
prizes and an award for the best- %s couple. The
%s dance committee is also proud to announce that
every girl who attends will receive a %s to pin to her
%s, and every boy will receive a complimentary %s.
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1], newlist[4][1], newlist[5][1], newlist[6][1], newlist[7][1], newlist[8][1], newlist[9][1], newlist[10][1], newlist[11][1], newlist[12][1], newlist[13][1], newlist[14][1], newlist[15][1]))
    newlist = []

def story6():
    words = ["a place", "an adjective", "a plural noun", "a place", "a profession", "a bodypart", "a noun", "a noun", "a noun", "a bodypart", "a name"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""\"Julius Caesar\"

Julius Caesar was born in 102BC in %s. He was
a %s general, and between 49 and 58 B.C. he defeated
the Gauls, the Goths, and the %s. After that, he
became more famous and defeated Pompey at the battle
of %s at Pharsala. The Romans then elected him
permanent %s , and he used to walk around wearing
a circlet of ivy leaves on his %s. Then Caesar went to
Egypt, where he met Cleopatra, the teenage Egyptian %s.
When he conquered the Syrians in 46 B.C., he sent back a message
saying, "Veni, vedi, %s." In 44 B.C., a soothsayer told Caesar
to "Beware the Ides of %s," but he ignored the warning
and in March he was stabbed in the %s by a group of
senators. His last words were, "Et tu %s?"
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1], newlist[4][1], newlist[5][1], newlist[6][1], newlist[7][1], newlist[8][1], newlist[9][1], newlist[10][1]))
    newlist = []

def story7():
    words = ["a plural noun", "an adjective", "a name", "an adjective", "a noun", "an adjective", "a plural noun", "an animal", "a verb", "a noun", "a noun", "a bodypart", "a noun", "a noun", "a bodypart"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""\"An Art Named Martial\"

Want to become an expet in Karate or Kung Fu? You can learn
martial %s in three %s lessons with Master
%s's video tape. This %s-selling tape
takes you step-by-%s through a series of %s
exercises guranteed to develop %s in your body and
make you strong as a %s. In less than a week, you will
be able to do one hundred %s-ups a day, skip a jumping
%s for an hour, and climb a %s without losing your your
%s. And believe it or not, by the end of the month,
you'll not only be eligible for a black %s, but be capable
of breaking a four-inch-thick %s easily with your own two %s!
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1], newlist[4][1], newlist[5][1], newlist[6][1], newlist[7][1], newlist[8][1], newlist[9][1], newlist[10][1], newlist[11][1], newlist[12][1], newlist[13][1], newlist[14][1]))
    newlist = []

def story8():
    words = ["a noun", "an adjective", "an adjective", "a noun", "a noun", "an adjective", "a noun", "a noun", "an adjective", "an adjective", "an adjective", "a number", "an adjective", "a plural noun", "an adjective", "a noun"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""\"Dogs\"

It has often been said that "a dog is a man's best %s." Dogs
are very %s and can be taught many %s
tricks. A dog can be trained to carry a %s in his mouth.
And if you throw his %s, he will run and fetch it. Dogs
will also bark %sly if someone tries to break into your
%s during the night. One of the most popular canine pets
today is the %s.Spaniel. Spaniels have curly %s
coats and %s ears. They also have very %s
dispositions and live to be %s years old. Other popular dogs
are %s Terriers, German %s , and the
%s Poodle. Every home should have a loyal dog for a %s.
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1], newlist[4][1], newlist[5][1], newlist[6][1], newlist[7][1], newlist[8][1], newlist[9][1], newlist[10][1], newlist[11][1], newlist[12][1], newlist[13][1], newlist[14][1], newlist[15][1]))
    newlist = []

def story9():
    words = ["a noun", "an adjective", "a noun", "an adjective", "a noun", "an adjective", "a name", "a noun", "an adjective", "a bodypart", "a noun", "a noun", "an adjective", "a bodypart"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""\"Courtroom Drama\"

LAWYER: Your honor, I have discovered a witness who can prove,
beyond a shadow of a %s, that my client is a %s man.

JUDGE: Call the %s.

CLERK: Do you solemnly swear to tell the %s truth and
nothing but the %s?

WITNESS: I do.

LAWYER: Please state your %s name and occupation.

WITNESS: (hard to understand) My name is %s and I
am a %s driver.

JUDGE: I can't understand you. What is wrong... are you %s?

WITNESS: I forgot my false %s. They're in my
car. (Laughter in the courtroom. Judge raps his %s on his %s)

JUDGE: Order in the court. We'll have a ten-minute recess to allow
the witness to get his %s %s.

"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1], newlist[4][1], newlist[5][1], newlist[6][1], newlist[7][1], newlist[8][1], newlist[9][1], newlist[10][1], newlist[11][1], newlist[12][1], newlist[13][1]))
    newlist = []

def story10():
    words = ["a name", "a plural noun", "an adjective", "a noun", "an adjective", "a plural noun", "an adjective", "a noun", "an adjective", "a noun", "a noun", "a number", "an adjective", "a noun", "a noun"]
    
    if choice == 1:
        for x in range(0, len(words)):
            user = str(input("Enter " + words[x] + ": "))
            enter.append(user)

        newlist = list(zip(words, enter))
        exp_ansbank(newlist)

    if choice == 2:
        imp_ansbank(words)
        newlist = list(zip(words, enter))

    return print("""\"Concert Program\"

This evening, the famous orchestra conductor, %s,
will present a program of classical %s at the %s
music center. He/She will conduct the %s Symphony
Orchestra, which is noted for its excellent string and %s
wind sections, considered by many %s to be the
world's most %s ensemble. The program will begin with
Debussy's "Clair de %s," followed by Mendelssohn's
"%s Song," and Strauss' "Tale of the Vienna %s."
Then we will hear Rachmaninoff's "%s.Concerto
Number %s," but only the %s movements.
After intermission, the second half of the program will be devoted to
a playing in its entirety of Beethoven's "Fifth %s" Tickets
are on sale now at the %s office.
"""%(newlist[0][1], newlist[1][1], newlist[2][1], newlist[3][1], newlist[4][1], newlist[5][1], newlist[6][1], newlist[7][1], newlist[8][1], newlist[9][1], newlist[10][1], newlist[11][1], newlist[12][1], newlist[13][1], newlist[14][1]))
    newlist = []

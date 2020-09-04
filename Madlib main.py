import random
flag = 0

while flag == 0:
    choices = int(input("""Welcome to Madlibs! Start by choosing a game mode below:
1- Short story
2- Poem
3- Phrase
Enter the number of your choice here: """))

    if choices > 3:
        print("Error: The value you have put entered is invalid. Please select numbers 1 to 3 only.")
        print(end = "\n")

    elif choices <= 3:
        print("Great Choice!")
        print("*****loading game*****")
        flag = 1
        
num1 = random.randint(0,9)

if choices == 1:
    import long_stories

    if num1 == 0:
        long_stories.story0()
    elif num1 == 1:
        long_stories.story1()
    elif num1 == 2:
        long_stories.story2()
    elif num1 == 3:
        long_stories.story3()
    elif num1 == 4:
        long_stories.story4()
    elif num1 == 5:
        long_stories.story5()
    elif num1 == 6:
        long_stories.story6()
    elif num1 == 7:
        long_stories.story7()
    elif num1 == 8:
        long_stories.story8()
    elif num1 == 9:
        long_stories.story9()

elif choices == 2:
    import poems

    if num1 == 0:
        poems.story0()
    elif num1 == 1:
        poems.story1()
    elif num1 == 2:
        poems.story2()
    elif num1 == 3:
        poems.story3()
    elif num1 == 4:
        poems.story4()
    elif num1 == 5:
        poems.story5()
    elif num1 == 6:
        poems.story6()
    elif num1 == 7:
        poems.story7()
    elif num1 == 8:
        poems.story8()
    elif num1 == 9:
        poems.story9()

elif choices == 3:
    import phrases

    if num1 == 0:
        phrases.story0()
    elif num1 == 1:
        phrases.story1()
    elif num1 == 2:
        phrases.story2()
    elif num1 == 3:
        phrases.story3()
    elif num1 == 4:
        phrases.story4()
    elif num1 == 5:
        phrases.story5()
    elif num1 == 6:
        phrases.story6()
    elif num1 == 7:
        phrases.story7()
    elif num1 == 8:
        phrases.story8()
    elif num1 == 9:
        phrases.story9()
        


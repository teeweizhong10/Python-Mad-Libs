# Python-Mad-Libs
Mad libs game made with python

Author: Wei Zhong Tee
Last Updated: February 25 2019
Project type: Command line/Python IDLE game 

This is a basic mad libs game project built using Python. It gives users the choice to either play with a long story, short sentence or poem. Users are then prompted to choose whether they want the game to auto generate the appropriate missing words or if they want to enter the words themselves. I built this game when I was in a basic programming class and relatively new to the Python programming language, hence much of it can be deemed inefficient. The types of words had to be manually coded and entered into arrays for it to be correctly generated should the user want random words generated for the game. 

The main game and its logic is built in Madlib main.py, but it uses the code from either long_stories.py, phrases.py or poems.py to randomly choose a story and display it to the user. The text files contain words of a certain category. For example, professions, places, verbs, names, etc. that were used for generating the right type of word randomly in the stories/sentences/peoms.

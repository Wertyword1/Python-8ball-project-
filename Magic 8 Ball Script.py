# purpose of this is to test the import function and create a fun and easy script

import random

def Reply(RandomizedNumber):
    if RandomizedNumber == 1:
        return 'This is certain'
    elif RandomizedNumber == 2:
        return 'Impossible, it will never happen'
    elif RandomizedNumber == 3:
        return 'It is very likely'
    elif RandomizedNumber == 4:
        return 'It is very unlikely'
    elif RandomizedNumber == 5:
        return 'Hmm... Maybe'
    elif RandomizedNumber == 6:
        return 'I am tired, ask me again tomorrow'
    elif RandomizedNumber == 7:
        return 'It is possible if you try your best'

print('Ask the Magic 8 Ball any question then hit enter on your keyboard and it shall answer any and all questions with a high degree of certainty')
input()

print(Reply(random.randint(1,7)))

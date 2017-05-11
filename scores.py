import random

print 'Scores and Grades'
def grade(numberr):
    for x in range(0, numberr):
        score=random.randint(60,100)
        if score>=90:
            print "Score: {}; Your grade is A".format(score)
        elif score>=80:
            print "Score: {}; Your grade is B".format(score)
        elif score>=70:
            print "Score: {}; Your grade is C".format(score)
        elif score>=60:
            print "Score: {}; Your grade is D".format(score)
        else:
            print 'You failed'




numberr=10
grade(numberr)

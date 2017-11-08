import random

for i in xrange(10):
    random_num = random.randint(60,100)
    grade = ""
    if random_num >= 90:
        grade = "A"
    elif random_num >= 80:
        grade = "B"
    elif random_num >= 70:
        grade = "C"        
    else:
        grade = "D"        
    print "Score:", random_num, "; Your grade is", grade




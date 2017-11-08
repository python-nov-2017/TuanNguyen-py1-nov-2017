person = {
    "name": "Anna",
    "age": 101,
    "country of birth": "The United State",
    "favorite language": "Python",
}

for key, value in person.items():
    print "My {} is {}".format(key, value)
    
print ""
print "My name is {}".format(person["name"])
print "My age is {}".format(person["age"])
print "My country of birth is {}".format(person["country of birth"])
print "My favorite language is {}".format(person["favorite language"])
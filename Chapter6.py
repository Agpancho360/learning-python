sentence = "Hello, World!"
name = "Pancho"
age = 20
option = 8  # modify value to see examples

if (option == 1):  # indexing and slicing strings
    print(sentence[0:5])
    print(sentence[-1])
    print(sentence[:5])
    print(sentence[7:])

elif (option == 2):  # operators with strings
    print('Hello' in sentence)
    print('hello' in sentence)
    print('Hello' not in sentence)
elif (option == 3):  # putting strings inside other strings
    print('Hello, my name is ' + name + '. I am ' + str(age) + ' years old.')
    print('My name is %s. I am %s years old.' % (name, age))
    print(f'My name is {name}. Next year I will be {age + 1}')
elif (option == 4):  # upper(), lower(), isupper(), islower() methods
    print(name.upper())
    print(name.lower())
    print(name.isupper())
    print(name.islower())
elif (option == 5):  # startswith() and endswith() methods
    print(name.startswith('Pan'))
    print(name.startswith('pan'))
    print(name.endswith('cho'))
elif (option == 6):  # join(), split(), partition methods
    print(' -  '.join(['cats', 'rats', 'bats']))
    print('  '.join(['cats', 'rats', 'bats']))
    print('My name is Pancho. I am 20 years old'.split())
    print('My name is Pancho. I am 20 years old'.split("a"))
    print('My name is Pancho. I am 20 years old'.partition("a"))
elif (option == 7):  # rjust(), ljust(), and center() methods
    print('Random string'.rjust(20, '*'))
    print('Random string'.rjust(30))
    print('Random string'.rjust(20, '-'))
    print('Random String'.center(40, "+"))
elif (option == 8): #removing whitespace iwth strip(), rstrip(), and lstrip() methods
    sentence = "         Hello World           "
    print(sentence.strip())
    print(sentence.lstrip())
    print(sentence.rstrip())

import re
# using the re library
option = 4
if (option == 1):
    phoneNumber = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
    mo = phoneNumber.search("My number is 123-456-7890")
    print("Area code found: ", mo.group(1))
    print("First part found: ", mo.group(2))
    print("Second part found: ", mo.group(3))
elif (option == 2):
    phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumber.search("My number is 123-456-7890")
    print("Full Phone #: " + mo.group())
elif (option == 3):  # looks for the first instance
    heros = re.compile(r'Batman|Superman')
    mo1 = heros.search('Batman is better than Superman')
    mo2 = heros.search('Superman is better than Batman')
    print("mo1:  " + mo1.group())
    print("mo2: " + mo2.group())
elif (option == 4):
    hero = re.compile(r'Super(wo)?man')
    mo1 = hero.search('The Adventures of Superman')
    mo2 = hero.search('The Adventures of Superwoman')
    print("mo1:  " + mo1.group())
    print("mo2: " + mo2.group())

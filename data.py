import bcrypt

users = {'john@doe.com': '$2b$12$/TYFvXOy9wDQUOn5SKgTzedwiqB6cm.UIfPewBnz0kUQeK9Eu4mSC'}

user_input = "Predator"
salt = bcrypt.gensalt()
bcrypt.hashpw(user_input.encode(encoding="utf-8"), salt)


questions = {
    "I ______ bus on Mondays.": {
        "a. 'm going to work with": False,
        "b. 'm going to work by": False,
        "c. go to work with": False,
        "d. go to work by": True
    },
    "Sorry, but this chair is ______.": {
        "a. me": False,
        "b. mine": True,
        "c. my": False,
        "d. our": False
    },
    "A: 'How old ______?'   B: 'I ______ .'": {
        "a. are you / am 20 years old.": True,
        "b. have you / have 20 years old.": False,
        "c. are you / am 20 years.": False,
        "d. do you have / have 20 years.": False
    },
    "I ______ to the cinema.": {
        "a. usually don't go": False,
        "b. don't usually go": True,
        "c. don't go usually": False,
        "d. do not go usually": False
    },
    "Where ______ ?": {
        "a. your sister works": False,
        "b. your sister work": False,
        "c. does your sister work": True,
        "d. do your sister work": False
    }
}

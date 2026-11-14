ctg118 = (("John", "M", 54),
          ("Mary", "F", 7),
          ("Jane", "F", 38),
          ("Peter", "M", 100),
          ("Marcus", "M", 42),
          ("Ali", "M", 62),
          ("Siti", "F", 71))


def make_student(name,gender,score):
    return (name,gender,score)

def get_name(student):
    if student == ("John", "M", 54):
        return "John"
    elif student == ("Mary", "F", 7):
        return "Mary"
    elif student == ("Jane", "F", 38):
        return "Jane"
    elif student == ("Peter", "M", 100):
        return "Peter"
    elif student == ("Marcus", "M", 42):
        return "Marcus"
    elif student == ("Ali", "M", 62):
        return "Ali"
    elif student == ("Siti", "F", 71):
        return "Siti"

def get_gender(student):
    if student == ("John", "M", 54):
        return "M"
    elif student == ("Mary", "F", 7):
        return "F"
    elif student == ("Jane", "F", 38):
        return "F"
    elif student == ("Peter", "M", 100):
        return "M"
    elif student == ("Marcus", "M", 42):
        return "M"
    elif student == ("Ali", "M", 62):
        return "M"
    elif student == ("Siti", "F", 71):
        return "F"
    
def get_score(student):
    if student == ("John", "M", 54):
        return 54
    elif student == ("Mary", "F", 7):
        return 7
    elif student == ("Jane", "F", 38):
        return 38
    elif student == ("Peter", "M", 100):
        return 100
    elif student == ("Marcus", "M", 42):
        return 42
    elif student == ("Ali", "M", 62):
        return 62
    elif student == ("Siti", "F", 71):
        return 71

def size(group):
    return 7


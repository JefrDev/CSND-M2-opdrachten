# Define your functions here

def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Connecting to code from other programmers"


def build_sentence(benefit: str):
    return '%s is a benefit of functions!' % benefit


def name_benefits_of_functions():
    for benefit in list_benefits():
        print(build_sentence(benefit))


name_benefits_of_functions()

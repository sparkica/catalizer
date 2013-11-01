def calculate_score_for_gender(gender):
    if gender == "male":
        return 10
    else:
        return 5

def calculate_score_for_age(age):
    return age * 2

def calculate_score_for_friends(friends, virtual_friends):
    return sum([friends,virtual_friends]) * 0.5

def calculate_score(gender, age, friends, virtual_friends):
    
    print "Calculating score...."
    
    result = calculate_score_for_gender(gender)
    result += calculate_score_for_age(age)
    result += calculate_score_for_friends(friends, virtual_friends)
    
    return result
def validator():
    grade = int(input("Please enter your final grade "))
    if (grade >= 90):
        print("Status: Honors")
    elif (grade >= 60 and grade <= 89):
        print("Status: Passed")
    elif (grade < 60):
        print("Status: Failed - Please contact the advisor")
    return

validator()
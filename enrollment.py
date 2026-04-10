def enrollment():
    name = str(input("Enter student first name: "))
    last_name = str(input("Enter student last name: "))
    age = int(input("Enter student age: "))
    tuition_balance = float(input("Enter tuition balance: "))
    
    is_active_input = input("Is the student active (true/false): ").lower()
    is_active = True if is_active_input == "true" else False

    print("\n===== Student Enrollment Report =====")
    print(f"Name: {name} {last_name}")
    print(f"Age: {age}")
    print(f"Tuition Balance: ${tuition_balance:.2f}")
    print(f"Active Status: {is_active}")
    print("=====================================\n")

    del tuition_balance

enrollment()
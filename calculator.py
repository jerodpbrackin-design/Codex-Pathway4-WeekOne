def tuition_calculator():
    base_tuition = 500
    registration_fee = 50
    total = base_tuition + registration_fee
    discount_total = total - 50
    print(f"The total tuition is {total} and the discounted price is {discount_total}")
    return

tuition_calculator()
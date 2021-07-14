def blind_bind():
    new_dict = {}
    bit_on = True
    cost = 0
    name = ""

    while bit_on:
        usr_name = input("What is your name?: ")
        usr_bit = int(input("Whats your bid? "))
        another = input("Anyone else wants to bit?")
        if another == "y":
            new_dict[usr_name] = usr_bit
        elif another == "n":
            new_dict[usr_name] = usr_bit
            bit_on = False
        else:
            new_dict[usr_name] = usr_bit
            bit_on = False

    for key, value in new_dict.items():
        if value > cost:
            cost = value
            name = key

    print(f"Congratulations! {name.title()} and your BIT is: {cost}.")
    


blind_bind()

def is_number(s):
    # handle for negative values
    negative = False
    if s[0] == '-':
        negative = True

    if negative:
        s = s[1:]

    # try to convert the string to float
    try:
        float(s)
        return True
    # catch exception if cannot be converted
    except ValueError:
        return False


def scale_checker():
    print("Input the scale in which you want to convert:")
    scale = input().lower()
    existing_scales = ["kelvin", "fahrenheit", "celsium"]
    if scale in existing_scales:
        return scale
    else:
        return "This scale doesn`t exist. Temperature remains the same. Try another scale."


def converter():
    print("Input the initial temperature:")
    user_temperature = input()

    # kelvin = +273.15
    # fahrenheit = +32
    # celsium = the most common t

    if is_number(user_temperature):
        chosen_scale = scale_checker()
        if chosen_scale == "kelvin":
            conv_to = float(user_temperature) + 273.15
        elif chosen_scale == "fahrenheit":
            conv_to = float(user_temperature) + 32
        else:
            conv_to = float(user_temperature)

    else:
        return "This is not a number. Try again."

    return "Temperature is: " + str(conv_to) + ".\nChosen scale is: " + str(chosen_scale)


print(converter())




#webhook0

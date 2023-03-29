def bmi (weight, height):
    if height < 1.0 or height > 2.5 or\
       weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(84, 1.75))

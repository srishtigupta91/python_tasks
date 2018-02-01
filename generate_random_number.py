from time import time

def get_seeds():
    #generating random value from the current time period is given
    value_1 = value_2 = 0
    while not value_1 and not value_2:
        try:
            value_1, value_2 = int(str(time() - int(time()))[-1]), int(str(time() - int(time()))[-2])
        except ValueError:
            get_seeds()
    return value_1, value_2


def validate_inputs(modulus, increment):
    # check the validity of the relation
    relation = 0
    while not relation:
        multiplier, seed = get_seeds()

        relation = 0 <= increment < modulus and 0 <= seed < modulus and multiplier in [1, 3, 7, 9]

    return multiplier, seed


def generate(modulus, increment):
    """generating multiplier and seed value and checking the
    current iteration should not be 0 and seed value"""
    multiplier, seed = validate_inputs(modulus, increment)
    output = [seed]
    current_iteration = -1
    switch = False

    while current_iteration != seed and current_iteration != 0:
        if not switch:
            current_iteration = (seed * multiplier) + increment
            switch = True
        else:
            current_iteration = (current_iteration * multiplier) + increment
            if current_iteration > modulus:
                current_iteration %= modulus
            output.append(current_iteration)

    result = int(str(''.join([str(i) for i in output]))[-1])
    return result

maxlist = []
minlist = []
m = 10
i = 0
loop = True
times = 100
while loop:
    num = generate(m, i)
    # print num
    if num >= 5:
        if len(maxlist) < 73:
            maxlist.append(num)
    else:
        if len(minlist) < 27:
            minlist.append(num)
    if len(maxlist) == 73 and len(minlist) == 27:
        loop = False
print("Probability of occuring elements less than 5:", minlist)
print("Probability of occuring elements greater than 5:", maxlist)
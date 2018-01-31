from time import time
import time as t


def get_seeds():
    value_1 = value_2 = 0
    while not value_1 and not value_2:
        # print int(str(time() - int(time()))[-1]), int(str(time() - int(time()))[-2])
        try:
            value_1, value_2 = int(str(time() - int(time()))[-1]), int(str(time() - int(time()))[-2])
        except ValueError:
            get_seeds()
    return value_1, value_2

    # ensure relationship of seeds fits that of an lcg and return the "random" result


def validate_inputs(modulus, increment):
    relation = 0
    while not relation:
        multiplier, seed = get_seeds()

        # check validity of relation
        relation = 0 <= increment < modulus and 0 <= seed < modulus and multiplier in [1, 3, 7, 9]

    return multiplier, seed

    # main function


def generate(modulus, increment):
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


start = t.ctime().split(" ")[3]
maxlist = []
minlist = []
m = 10
i = 0
loop = True
times = 100
while loop:
    t.sleep(0.00000000000001)
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
end = t.ctime().split(" ")[3]
print(start, end)
print(len(minlist), len(maxlist))
print(minlist)
print(maxlist)
import json

def generate(x):
    """ generating new value based on the given quantity"""
    val = float(x)
    val_23 = x * 23 / 100
    val_50 = x * 50 / 100
    val_260 = x * 260 /100
    return val, val_23, val_50, val_260

def quantity_conversion():
    """ retrieving json quantity data given for 100 grms from the file and
    converting it in different quantities values."""

    with open('data.json') as json_file:
        data = json.load(json_file)
        data = data['data']
        keys1 = data["100gm"].keys()
        for k in keys1:
            print(k) #representing the items name
            dat = data["100gm"][k]
            for i in range(len(dat)):
                dat1 = dat[i]
                for k2 in dat1.keys():
                    dat2 = dat1[k2]
                    if k2 == 'sub_cat':
                        for k3 in range(len(dat2)):
                            y = dat2[k3].values()
                            for i in y:
                                if isinstance(i, list) == True:  # checking whether list containing the value or not
                                    for l in range(len(i)):
                                        list_0 = i[l].values()
                                        for m in range(len(list_0)):
                                            x = list_0[m]["quantity"]
                                            u = generate(x)
                                            print(u)
                                else:
                                    x = i["quantity"]
                                    u = generate(x)
                                    print(u)
                    else:
                        x = dat2["quantity"]
                        u = generate(x)
                        print(u)


y = quantity_conversion()
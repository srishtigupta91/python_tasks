import pandas as pd

d = pd.read_json('data.json', typ='series')
data = d["data"]


def conversion(t):
    t = float(t)
    to_23 = t * (0.23)
    to_50 = t * (0.5)
    to_260 = t * (2.60)
    return to_23, to_50, to_260


def generate(x):
    to_23, to_50, to_260 = conversion(x)
    return to_23, to_50, to_260, "**********", x


def quantity_conversion(data):
    keys1 = data["100gm"].keys()
    print(keys1)  # datatype: Dict
    for k in keys1:
        print(k)
        dat = data["100gm"][k]  # datatype : List
        for i in range(len(dat)):
            dat1 = dat[i]
            for k2 in dat1.keys():
                dat2 = dat1[k2]
                if k2 == 'sub_cat':
                    for k3 in range(len(dat2)):
                        y = dat2[k3].values()
                        for i in y:
                            if isinstance(i, list) == True:
                                for l in range(len(i)):
                                    list_0 = i[l].values()  # dataType = list
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


y = quantity_conversion(data)
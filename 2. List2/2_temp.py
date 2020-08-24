def get_power_set(s):
    power_set=[[]]
    for elem in s:
        for sub_set in power_set:
            power_set=power_set+[list(sub_set)+[elem]]
    return power_set

power_set=get_power_set([1,2,3])
print(power_set)

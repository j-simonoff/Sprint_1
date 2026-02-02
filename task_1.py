counter_of_hms = 0
big_hms = '1h 45m,360s,25m,30m 120s,2h 60s'

mid_hms = big_hms.split(',')

for i in mid_hms:
    lit_hms = i.split()
    for w in lit_hms:
        if 'h' in w:
           counter_of_hms += int(w.replace('h', '')) * 60
        elif 'm' in w:
           counter_of_hms += int(w.replace('m', ''))
        else:
            counter_of_hms += int(w.replace('s', '')) // 60

print(counter_of_hms)
mit=input int ("enter your number",)

def average( *vals ):
        total = 0
    for val in vals:
        total += val
    return total/len(vals)

print (average(mit))
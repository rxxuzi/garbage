import math
for i in range(2, 11):
    # Rounded down to the second decimal place
    nishiyama = round(math.log(2, i), 2)
    print(f"{i} = {nishiyama}")

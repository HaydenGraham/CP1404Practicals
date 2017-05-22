from math import factorial


baselength = input("How large do you want the base?")

def get_num_of_bricks(baselength):
    brickcount = 0
    for i in range(0, baselength + 1):
        brickcount += i
    print(brickcount)
get_num_of_bricks(baselength)

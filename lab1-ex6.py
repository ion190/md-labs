import random
from colorama import Fore, Style, init
def generate_random_list(length):
    return [random.choice([0, 1]) for _ in range(length)]

def print_matrix(matrix):
    formatted_row = "".join(f"{Fore.LIGHTWHITE_EX}▉" if val == 0 else f"{Fore.LIGHTRED_EX}▉" for val in matrix)
    print(formatted_row + Style.RESET_ALL)


def next_gen(x,y,z):
    if x==1 and y==1 and z==1:
        return 0
    elif x==1 and y==1 and z==0:
        return 1
    elif x==1 and y==0 and z==1:
        return 1
    elif x==1 and y==0 and z==0:
        return 0
    elif x==0 and y==1 and z==1:
        return 1
    elif x==0 and y==1 and z==0:
        return 1
    elif x==0 and y==0 and z==1:
        return 1
    elif x==0 and y==0 and z==0:
        return 0
try:
    n=int(input("Enter the array dimensions: "))
    #m=int(input("Enter the amount of generations: "))
    random_list = generate_random_list(n)
    random_list = (n-1)*[0]+[1]
    print("Generation 0: ",end='')
    print_matrix(random_list)
    next_gen_list=random_list.copy()
    for j in range(0,m):
        next_gen_list[0]=next_gen(0,random_list[0],random_list[1])
        for i in range(1,len(random_list)-1):
            next_gen_list[i]=next_gen(random_list[i-1],random_list[i],random_list[i+1])
        next_gen_list[-1]=next_gen(random_list[-2],random_list[-1],0)
        print("Generation {0}: ".format(j+1),end='')
        print_matrix(next_gen_list)
        random_list=next_gen_list.copy()

except:
    print("Incorrect input")

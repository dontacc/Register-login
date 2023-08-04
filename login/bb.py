# # from random import *
# # from sys import *

# # names = ['negar', 'ali', 'reza', 'mohammad', 'jafar']


# # name = []  # ["-", "-", "-", "-", "-"]
# # selected_name = choice(names) # negar
# # print(selected_name)

# # for i in range(len(selected_name)): 
# #     name.append('-')

# # print(name)

# # while True:
# #     guess = input("enter your guess : ") 

# #     for i in range(len(selected_name)):  
# #         if guess == selected_name[i]: 
# #             name[i] = guess 
# #             print(name, "your charecter guess : ", guess)

# #             if "-" not in name:
# #                 print("you win")
# #                 print("your name was", selected_name)
# #                 exit()
        


    
# import random

# counter = 0
# pairs = 0 
# six_pairs = 0

# while six_pairs < 1: 
#     counter += 1
    
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)


#     if (dice1 == dice2) and dice1 != 6 and dice2 != 6:
#         pairs += 1
#         print(dice1, dice2)
        
#     if dice1 == 6 and dice2 == 6:
#         six_pairs += 1

#         print("-----")
#         print(dice1, dice2)
#         print("-----")

# print(counter)
# print(pairs)








from random import *

names = ['alborz','ardebil','bushehr','azarbaijan','esfahan','fars','gilan',
        'golestan','hamadan','hormozgan','ilam','kerman','kermanshah',
        'khuzestan','kordestan','lorestan','markazi','mazandaran','khorasan',
        'qazvin','qom','semnan','sistan','tehran','yazd','zanjan']


shuffle(names)

print(names)









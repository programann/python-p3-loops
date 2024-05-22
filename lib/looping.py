#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i>0:
        print(i)
        i-=1
        
    print ('Happy New Year!')
  



def square_integers(integers_list):
    return [integer**2 for integer in integers_list]

def fizzbuzz():
    i=1
    while i <= 100:
        if (i % 3 == 0) and (i % 5 == 0):
            print('FizzBuzz')
        elif i % 3 == 0 :
            print ('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
        i+=1
print(fizzbuzz())

# i = 10
# while i>=0:
#     print(i)
#     i-=1

# for i in range(10):
#     print(f'i is {i}')
    


# player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

# inch_heights = [heights * 7920 for heights in player_heights]

# print(inch_heights)
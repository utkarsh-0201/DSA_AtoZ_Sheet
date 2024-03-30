"""
* * *
* * *
* * *
"""

def print_forest(n):

    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


#print_forest(8)
        
"""
* 
* * 
* * *
* * * *
* * * * *
* * * * * *
or 
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
or
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
"""

def print_triangle(n, to_print='*', print_nums_only=False):
    for i in range(1,n+1):
        for j in range(i):
            if print_nums_only is True:
                to_print = i
            elif to_print != '*':
                to_print = j + 1
            print(to_print, end="")
        print()

# print_triangle(6)
# print_triangle(6, to_print='num')
# print_triangle(6, print_nums_only=True)

"""
     *     
    ***    
   *****   
  *******  
 ********* 
***********
"""
def print_pyramid(N):
    for i in range(1, N+1):
        space_len = N - i 
        star_length = i * 2 - 1
        for j in range(space_len):
            print("", end=" ")
        for i in range(star_length):
            print("*", end="")
        print()

#print_pyramid(5)


def print_revrse_pyramid(N):

    for i in range(0, N):
        for j in range(i):
            print("", end=" ")
        for k in range(0, 2*N - (2*i+1)):
            print("*", end="")
        print()


print_revrse_pyramid(5)
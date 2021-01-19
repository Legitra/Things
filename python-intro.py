#helloworld#                #--------------------------------------------#

def helloworld():
    print("Hello, World!")
    return
    
#ifelse#                    #--------------------------------------------#
    
def ifelse(n):
    n = int(input().strip())
    if (n % 2 != 0):
        print("Weird")
    if (2 <= n <= 5) and (n % 2 == 0):
        print("Not Weird")
    if (6 <= n <= 20) and (n % 2 == 0):
        print("Weird")
    if (20 < n) and (n % 2 == 0):
        print("Not Weird")
    return
    
#arithmetic operators#      #--------------------------------------------#
        
def arithops(a,b):
    a = int(input())
    b = int(input())
    
    print(a + b)            #sum of A and B
    print(a - b)            #difference of A and B
    print(a * b)            #product of A and B
    return
    
#division#                  #--------------------------------------------#

def division(a,b):
    a = int(input())
    b = int(input())
    
    print(a // b)           #integer division
    print(a /  b)           #float division
    return
    
#loops#                     #--------------------------------------------#

def loops(n):
    n = int(input())
    
    for x in range (0,n):   #for every number (x) from 0 to n
        print(x ** 2)       #print the square of x

    return

#write a function#          #--------------------------------------------#

def is_leap(year):
'''
Takes input 'year' as integer.
Function returns bool;
    True if input is leap year,
    False if not leap year
'''
    if (year % 4 == 0):             #if year is divisable by 4;
        if (year % 100 == 0):       #   and also divisible by 100;
            if (year % 400 == 0):   #       and also 400;
                return True         #           it is a leap year
            else:
                return False        #not divisable by 400 therefore not leap year
        else:
             return True            #divisable by 4 but not 100 is a leap year

    return False                    #not divisable by 4

year = int(input())
print(is_leap(year))
#print function#            #--------------------------------------------#

def print_func(n):
    n = int(input())        #get given number
    
    for i in range(1,n+1):  #for each number from 1 to given number
        print(i,end = "")   #print the number with specified end ""

#helloworld#                #--------------------------------------------#

def helloworld():
    print("Hello, World!")
    
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
    
#arithmetic operators#      #--------------------------------------------#
        
def arithops(a,b):
    a = int(input())
    b = int(input())
    
    print(a + b)            #sum of A and B
    print(a - b)            #difference of A and B
    print(a * b)            #product of A and B
    
#challenge 4#               #--------------------------------------------#
#challenge 5#               #--------------------------------------------#
#challenge 6#               #--------------------------------------------#
#challenge 7#               #--------------------------------------------#

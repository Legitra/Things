if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    second = list(set(arr))         #finds unique scores by converting to 
                                    #                set then back to list
    second.sort(reverse=True)       #sort list in decending order        
    print(second[1])                #gets second item in list

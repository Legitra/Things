def get_score(l):
    '''
    function for use in sort()
    takes a nested list and returns the second item in the list
    '''
    return l[1]

if __name__ == '__main__':
    scores = []
    for _ in range(int(input())):                   #gets scores and names
        name = input()
        score = float(input())
        scores.append([name,score])

    scores.sort(key = get_score)                    #sort input in ascending according to score
    second_low  = []
    
    for s in scores:
        if s[1] != scores[0][1]:                    #find the first item that doesnt have the lowest score
            start = scores.index(s)
            break                                   #stop the loop

    second_low.append(scores[start][0])             #add first of the 'second lowest' people to list

    if start+1 < len(scores):                       #if the start isnt the last item in the list
        for n in range(start+1,len(scores)):
            if (scores[n][1] == scores[start][1]):  #if the next person has the same score as the 'second lowest'
                second_low.append(scores[n][0])     #add this person to the list
            else:
                break                               #if next person is not equal, stop the loop

    second_low.sort()                               #sort the list of 'second lowest'

    for name in second_low:                         #print the names
        print(name)



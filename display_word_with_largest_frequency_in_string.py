#PF-Assgn-56

def max_frequency_word_counter(data):
    word=""
    frequency=0
    x = data.split(" ")
    p = set(x)
    y = list(p)
    
    #print(y)
    #print(x)
    listC = []
    listW = []
    for i in y:
        count = 0
        for j in x:
            if(j==i):
                count = count + 1
        listC.append(count)
        listW.append(i)
    
    #print(listC)
    #print(listW)
    
    b = max(listC)
    j= 0
    M = []
    for i in listC:
        if(b == i):
            M.append(j)
        j=j+1
    #print(M)
    #print(b)
    almost =[]
    for i in M:
        almost.append((listW[i]))
    #print(almost)
    if(len(almost)>1):
        n = []
        for i in almost:
            len_of_str =len(i)
            n.append(len_of_str)
        #print(n)
        max_length = max(n)
        k=0
        for i in n:
            if(max_length == i):
                index = k
            k = k+1
        r = int(index)
        q = almost[r]
        word= word + str(q)
        frequency = b
        print(word,frequency)
        
    else:
        q = almost[0]
        word = word + str(q)
        frequency = b
        print(word,frequency)
        
    #start writing your code here
    #Populate the variables: word and frequency
    #print(word,frequency)


#Provide different values for data and test your program.
data = "Listen to the big clock Tick tock tick"

#data="Rain on the green grass and Rain on the tree"
#data ="Work like you do not need money love like you have never been hurt and dance like no one is watching"
x = data.lower()
#print(x)
max_frequency_word_counter(x)
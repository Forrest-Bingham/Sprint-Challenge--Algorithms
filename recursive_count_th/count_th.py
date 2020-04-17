'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''



def count_th(word, count=0):
    
    if len(word) <= 1:
        return count
    # TBC
    print(len(word), "------ Word Length")
    if len(word) > 1:
        print(word[0])
        print(word[1])
        if word[0]=="t" and word[1] =="h":
            count += 1
            word = word[1:]
            print(count, " COUNT!")
            print(word, "------- New Word String")
            
        else:
            word = word[1:]
            print(word, "------- New Word String")

    return count_th(word, count)        

word = "thlmnopthmthmthmthppp"

count_th(word)

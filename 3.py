print (" TRANSLATOR ")




def read_from_file () :
    global WORDS_BANK

    f = open ("translate.txt", "r")
    WORDS_BANK = []

    for line in f :
        word = line.split("\n")
    
    f.close ()

read_from_file ()
print (WORDS_BANK)
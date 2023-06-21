# Write an automated censor program that reads in the text from a file
# and creates a new file where all of the four-letterwords have been replaced by "****".
# You can ignore punctuation, and you may assume that no words in the file are splitacross multiple lines.
def main():
    print("using this file to replace the four-letter words by ****")
    # read file
    file = input("Please enter the file name:")
    text = open(file,'r').read()
    words = text.split()
    # write file
    filename = input("name a new file:")
    opw = open(filename, 'w')
    #  to get words length
    for w in words:
        if len(w) == 4 :
            w = "****"
        elif len(w) == 5 :
            if "." in w :
                w = "****."
            elif "," in w :
                 w = "****,"
            elif "?" in w :
                 w = "****?"
            elif "!" in w :
                 w = "****!"
        print(w, end=" ", file=opw )

if __name__ == '__main__':  main()   

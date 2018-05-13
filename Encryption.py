function = (input("Would you like to encrypt or decrypt text? "))
if function == "encrypt":
    texttoencrypt = (input("Enter text to encrypt "))
    shift = (int(input("Enter the Shift ")))
    numlist = (list(map(ord, texttoencrypt)))
    numlist2 = ([x+shift for x in numlist])
    numlist3 = (list(map(chr, numlist2)))
    s = "";
    print (s.join (numlist3))
elif function == "decrypt":
    texttodecrypt = (input("Enter text to decrypt "))
    shift = (int(input("Enter the Shift ")))
    numlist = (list(map(ord, texttodecrypt)))
    numlist2 = ([x-shift for x in numlist])
    numlist3 = (list(map(chr, numlist2)))
    s = "";
    print (s.join (numlist3))

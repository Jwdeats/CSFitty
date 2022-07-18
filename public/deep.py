x = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))
if x.casefold().strip() == "42":
    print('Yes')
else:
    if x.casefold().strip() == "forty-two":
        print("Yes")
    else:
        if x.casefold().strip() == "forty two":
            print("Yes")
        else:
            print("No")
            

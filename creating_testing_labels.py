with open("testing_label.txt","w") as a1:
    for i in range(0,515):
        print(a1.write("1" +"\n"))
    for i in range(515,978):
        print(a1.write("0" +"\n"))

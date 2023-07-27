import sys
def ff(*argv):

    # print(argv)
    if len(argv[0])==0:
        print("0 arguments.") 
    elif len(argv[0])==1:
        print("1 argument.")
        print("1: {}".format(argv[0][1]))
    else:
        x = argv[0]
        # print(x)
        print("{}: arguments".format(len(argv[0])-1))
        for i in range(1, len(x) ):
            print("{}: {}".format(i,x[i]))


ff(sys.argv)
  
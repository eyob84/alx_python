import sys
def ff(*argv):

    # print(argv)
    if len(argv[0])==1:
        print("0 arguments.") 
    elif len(argv[0])==2:
        print("1 argument:")
        print("1: {}".format(argv[0][1]))
    else:
        x = argv[0]
        # print(x)
        print("{} arguments:".format(len(argv[0])-1))
        for i in range(1, len(x) ):
            print("{}: {}".format(i,x[i]))
if __name__ == "__main__":
    ff(sys.argv)
  
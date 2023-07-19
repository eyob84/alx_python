for i in range(10):
    for j in range(i + 1, 10):
        combination = "{:02d}".format(i * 10 + j)
        print(combination, end=(", " if combination != "89" else "\n"))
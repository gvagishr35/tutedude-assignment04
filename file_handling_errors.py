try:
    f = open("sample.txt", "r")
    print("Reading file content:\n")

    count = 1
    for line in f:
        print("Line", count, ":", line.strip())
        count += 1

    f.close()

except:
    print("Error: The file 'sample.txt' was not found.")   
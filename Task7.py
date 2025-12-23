count = 1
try:
    with open("sample.txt","rt") as fh:
        contents = fh.readlines()
        print("Reading file content: ")
        for line in contents:
            print(f"Line {count}: {line.rstrip('\n')}")
            count += 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
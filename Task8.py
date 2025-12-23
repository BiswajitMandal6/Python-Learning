fh = open("output.txt","wt")
fh.write(input("Enter text to write to the file: ")+"\n")
print("Data successfully written to output.txt.\n")
fh.close()

fh = open("output.txt","at")
fh.write(input("Enter text to append: ")+"\n")
print("Data successfully appended.\n")
fh.close()

fh = open("output.txt","rt")
print("Final content of output.txt:")
content = fh.readlines()
for line in content:
    print(line,end="")
fh.close()

#Text File reader/writer
with open("hello_mam.txt", "w") as file:
    file.write("This is a new file")
with open("hello_mam.txt", "r") as file:
    content = file.read()
    print(content)
with open("hello_mam.txt", "a") as file:
    task =file.write("\n"+"bye")   
    

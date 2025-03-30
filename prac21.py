#write a function that replaces all occurences of "java" with "python" in above file.
def occurences():
    with open("practice.txt","r") as file:
        data=file.read()
    n_data=data.replace("java","python")
    print(n_data)

    with open("practice.txt","w") as file:
        file.write(n_data)
occurences()

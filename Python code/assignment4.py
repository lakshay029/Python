# #task 1
try:
    file1=open('simple.txt','r')
    reading_file=file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError:
    print('Error: The file "simple.txt" not exisit')
except Exception as e:
    print(f"An unexpected error occurred: {e}")


#task 2

user_input = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

print("Hello Python!")


additional_input = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")
    print("Additional data appended to output.txt.")


print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)

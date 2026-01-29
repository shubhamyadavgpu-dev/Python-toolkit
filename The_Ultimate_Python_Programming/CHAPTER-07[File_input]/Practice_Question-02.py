with open(r"C:\Coder\frontend\The_Ultimate_Python_Programming\CHAPTER-07[File_input]\practice.txt") as file:
    content = file.read()

new_content = content.replace("Java", "Python")
print(new_content)

# Open the file in write mode to update the content
with open(r"C:\Coder\frontend\The_Ultimate_Python_Programming\CHAPTER-07[File_input]\practice.txt", "w") as file:
    file.write(new_content)

def word() :
    word = "learning"
    with open(r"C:\Coder\frontend\The_Ultimate_Python_Programming\CHAPTER-07[File_input]\practice.txt","r") as f :
        data = f.read()
        if (data.find(word) != -1) :
            print("Found")
        else :
            print("Not Found")
word()            # @param x: int
# @return: string

def checkOddEven(x):
    # code here
    if x%2==0 :
        return Even
    else :
        return odd
print(checkOddEven(4))        
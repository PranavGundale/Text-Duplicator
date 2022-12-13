file = open("MyData.txt", "r") 
file2 = open("MyDataDuplicated.txt", "w")
file2.write(file.read()) #copying the text from file1 to paste it on file2
file2.close() #closing the dialouge box

# Pranav Gundale

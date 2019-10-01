"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
file = open("src/foo.txt", "r")
content = file.read()
print(content)
file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
a = ["""Open up a file called bar.txt (which doesn't exist yet) for
writing. Write three lines of arbitrary content to that file, then close the file. Open up "bar.txt" and inspect it to make 
 sure that it contains what you expect it to contain"""]
# YOUR CODE HERE
file= open("src/bar.txt","w+")
for i in a:
    file.write(i+"\n")
file.close()

file = open("src/bar.txt", "r")
content = file.read()
print("\n")
print(content)
file.close()
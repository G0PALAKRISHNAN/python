'''By using the with stmt it will opens a file in the name test.txt and
closes after the the block ends'''
with open('test.txt','r') as f:
    #print(f.read()) # displays the contents of the file
    #print(f.readlines()) # displays the file content in list manner of all lines
    #print(f.readline()) # displays the file content in list manner of first line
    '''print(f.readline(),end="") #thos will print first line
    print(f.readline(),end="") # this will print second line'''

    '''for line in f:
        print(line,end="") 
#This will prints all the lines without memory interruption for printing the line'''


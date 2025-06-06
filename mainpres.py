def display_using_loop(filename):
    print("Using Loop ------")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

def display_using_list(filename):
    print("Using List ------")
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

# Define the filename
filename = 'presidents.txt'

# Call the functions to display the contents
display_using_loop(filename)
print()
display_using_list(filename)

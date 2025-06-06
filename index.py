def create_file_with_string(filename, content):
    """
    Creates a file and writes a single string to it.
    """
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Email: {content}")



filename1 = 'email.txt'
content1 = input("Enter your email address: ")
create_file_with_string(filename1, content1)

def append_to_file(filename, line):

    with open(filename, 'a') as file:
       
        file.write(line + '\t')


append_to_file('email.txt', "McKenna")
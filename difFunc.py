def create_file_with_string(filename, content):
    """
    Creates a file and writes a single string to it.
    """
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File '{filename}' created with content: {content}")

def create_file_with_list(filename, lines):

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')
    print(f"File '{filename}' created with content: {lines}")

filename1 = 'single_string.txt'
content1 = "This is a single string written to the file."
create_file_with_string(filename1, content1)

filename2 = 'list_of_strings.txt'
content2 = ["First line", "Second line", "Third line"]
create_file_with_list(filename2, content2)

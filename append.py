def append_to_file(filename, line):

    with open(filename, 'a') as file:
       
        file.write(line + '\n')


append_to_file('email.txt', "McKenna")


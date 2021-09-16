import checkmypass as chkpass

#open password file
with open('list.txt','r') as file:
    list = file.read().splitlines()

if __name__ == '__main__':
    chkpass.main(list)
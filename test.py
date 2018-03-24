binary_string = ''
def recursive_bin(decimal):
        global binary_string
        binary_string += str(int(decimal % 2))
        if (decimal // 2) == 0:
            print (binary_string[::-1])
        else:
            decimal = decimal /2
            recursive_bin(decimal)  



recursive_bin(25)     
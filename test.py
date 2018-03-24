def recursive_bin(decimal):
    if decimal <0:
        return "no negative numbers" # you dont need the parenthesis
    elif decimal == 0:
        return 0 # the final output is an integer keep it this way ,converting to a string only applies where the number needs to be reversed
    else:
        # this is where the recursion occurs if the number passes the above exceptions
        binary_string ='' # initilize and empty binary string where functions appends binary digits as they are generated
        binary_string += str(decimal % 2)
        decimal /= 2
        if decimal == 1:
            return binary_string
        else:
            return recursive_bin(decimal)
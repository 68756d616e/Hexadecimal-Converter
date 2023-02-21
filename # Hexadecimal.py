# Hexadecimal conversion

def decimal_to_hex(decimal):
    """Converts a decimal number to hexadecimal""" # What is does
    return hex(decimal)

def hex_to_decimal(hexadecimal):
    """Converts a hexadecimal string to decimal""" # What it does
    return int(hexadecimal, 16)


# Check if the input is a decimal number or a hexadecimal string
while True:

    # Provide a conversion or list of questions
    user_input = input("Please enter a decimal number, hexadecimal sequence or type 'list' for additional information: ")
        
    if user_input.isdecimal():
        decimal = int(user_input)
        hex_result = decimal_to_hex(decimal)
        print(f"Your Hexadecimal result: {hex_result}")

    elif user_input == 'list':
        print("")

    else:
        hexadecimal = user_input.lower() # Convert to lowercase for consistency
        decimal_result = hex_to_decimal(hexadecimal)
        print(f"Decimal result: {decimal_result}")


#!/usr/bin/python3
<<<<<<< HEAD
"""The Module determines if a given data set represents a valid UTF-8 encoding"""


def get_leading_set_bits(num):
    """
    returns the number of leading set bits (1).
    parameter: num - The number
    """
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Parameter: data - The provided data to check.
    """
    bits_count = 0
    for i in range(len(data)):
        if bits_count == 0:
            bits_count = get_leading_set_bits(data[i])
            """1-byte (format: 0xxxxxxx)"""
            if bits_count == 0:
                continue
            """a character in UTF-8 can be 1 to 4 bytes long"""
            if bits_count == 1 or bits_count > 4:
                return False
        else:
            """checks if current byte has format 10xxxxxx"""
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        bits_count -= 1
    return bits_count == 0
=======
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
     # Initialize a variable to keep track of the number of expected bytes
    expected_bytes = 0
    
    # Iterate through the data
    for byte in data:
        # Check if the byte is a continuation byte (starts with '10')
        if byte >> 6 == 0b10:
            # If it's a continuation byte, decrement the expected_bytes count
            expected_bytes -= 1
        else:
            # Otherwise, check the number of expected bytes based on the first byte
            if expected_bytes > 0:
                return False  # Invalid UTF-8 sequence
            elif byte >> 7 == 0b0:
                expected_bytes = 0  # Single-byte character
            elif byte >> 5 == 0b110:
                expected_bytes = 1  # Two-byte character
            elif byte >> 4 == 0b1110:
                expected_bytes = 2  # Three-byte character
            elif byte >> 3 == 0b11110:
                expected_bytes = 3  # Four-byte character
            else:
                return False  # Invalid UTF-8 sequence
    
    # Check if all expected bytes were consumed
    return expected_bytes == 0
>>>>>>> 09d38a5415b1696ab2a568b6bcd928c65f67fddb

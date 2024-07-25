#!/usr/bin/python3

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
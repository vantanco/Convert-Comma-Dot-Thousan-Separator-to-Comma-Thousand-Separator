import re

def convert_to_comma_thousand_dot_decimal(number_str):
    # Regular expression to match comma thousand separator and dot decimal separator
    decimal_pattern = r'(\d{1,3})[.,](\d{3})(?:[.,](\d{1,2}))?(%)?'

    # Check if the number string contains either a comma or a dot
    if ',' in number_str or '.' in number_str:
        # Replace comma thousand separator with empty string and dot decimal separator with comma
        formatted_number = re.sub(decimal_pattern, r'\1X\2,\3', number_str)
        if '.' not in formatted_number:
            formatted_number = formatted_number.replace('.', '').replace(',', '.').replace('X', ',')
        else :
            formatted_number=formatted_number


    else:
        # If the number string doesn't contain comma or dot, leave it unchanged
        formatted_number = number_str

    # Remove trailing dot if the number is an integer
    formatted_number = formatted_number.rstrip('.')

    return formatted_number

# Sample text containing numbers with different separators
text = """
1.234,56
12.345,67
123.456,78
10,45
0
10.45
1,234.56
12,345.67
123,456.78
1
12
123
1,234
12,345
123,456
1,234,567
12,345,678
500
"""

# Regular expression pattern to match numbers with both formats, excluding numbers without separators
pattern = r'\b\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{1,2})?%?\b'

# Find all numbers in the text
found_numbers = re.findall(pattern, text)

# Convert each found number to the desired format
converted_numbers = [convert_to_comma_thousand_dot_decimal(number) for number in found_numbers]

# Print the original and converted numbers
print("Founded numbers:", found_numbers)
print("Converted numbers:", converted_numbers)

# Convert-Comma-Dot-Thousan-Separator-to-Comma-Thousand-Separator
Find number in string and convert Comma Dot Thousanđ Separator to Comma Thousand Separator - Use case: Vietnamese

# Data test
``` python
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
```
# Result
``` python
Founded numbers: ['1.234,56', '12.345,67', '123.456,78', '10,45', '0', '10.45', '1,234.56', '12,345.67', '123,456.78', '1', '12', '123', '1,234', '12,345', '123,456', '1,234,567', '12,345,678', '500']
Converted numbers: ['1,234.56', '12,345.67', '123,456.78', '10.45', '0', '10.45', '1,234.56', '12,345.67', '123,456.78', '1', '12', '123', '1,234', '12,345', '123,456', '1,234.567', '12,345.678', '500']
```

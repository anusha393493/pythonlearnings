# Open the input file in read mode
with open(r"C:\Users\anusha.raparthi\Desktop\RPSR23Q4.txt", 'r') as input_file:
    # Read all lines from the input file
    lines = input_file.readlines()

# Open the same file in write mode
with open('input.txt', 'w') as output_file:
    # Iterate over each line
    for line in lines:
        # Add a comma at the end of each line
        line_with_comma = line.rstrip() + ',\n'
        # Write the modified line to the output file
        output_file.write(line_with_comma)


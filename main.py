# Currently using text files that contain XML data to format to JSON

# Using readline()
file1 = open('waffles.txt', 'r')        ### Change to the file you want
count = 0
element_name_list = []
element_contents_list = []
# element_name_end = []
leading_whitespace = 0

while True:
    count += 1
    # Get next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break
    element_name = " "
    element_start = 0
    element_end = 0
    line_len = len(line)

    # for loop to check for the beginning of an element based on "<" and ">"
    # also keeps count of the leading whitespace to add back to file later
    for ch in range(line_len):
        # check for starting white space
        leading_whitespace = len(line) - len(line.lstrip())
        # check for "<" to beginning position XML element
        if line[ch] == "<":
            element_start = ch
        # check for ">" to end position for XML element
        if line[ch] == ">":
            element_end = ch
            break

    # empty string used to add whitespace back into JSON format
    add_whitespace = ""

    # for loop to add space based on the whitespace counted earlier
    for lw in range(leading_whitespace):
        add_whitespace += " "

    # stores and formats the element name found between element characters "<", ">"
    element_name = add_whitespace + '"' + line[element_start+1:element_end] + '":'              ### THIS IS WHERE THE COLON IS ADDED
    if element_name[leading_whitespace+1] == "/":
        element_name = "}"

    # stores and formats the element contents found after ">" but before the ending "<"
    element_contents = '"' + line[element_end+1:line_len-(element_end-(leading_whitespace-3))] + '",'

    # stores and formats the element name found between ending element characters "<", ">" for input validation later
    # element_endName = '"' + line[line_len - len(element_name) + 1:-1] + '"'

    # appends each element name to its larger list
    element_name_list.append(element_name)

    # check the element contents if they are empty or and if they contain a trailing ","
    if element_contents == '""' and element_name != "}":
        element_contents = "{"
    elif element_contents == '"",':
        element_contents = ""
    # appends each set of element content to its larger list
    element_contents_list.append(element_contents)
    # element_name_end.append(line[line_len - len(element_name) + 1:-1])

file1.close()

for i in range(len(element_name_list)):
    print(element_name_list[i], end=" ")
    print(element_contents_list[i])


# CHECK DESCRIPTION LINE 'INPUT'; ADDING EXTRA ":"

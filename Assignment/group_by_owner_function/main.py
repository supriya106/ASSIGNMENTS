# Input dictionary.
files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
# Function to group the files.
def group_by_owners(files):

    # Dictionary object to hold the result.
    result = {}

    for key, value in files.items(): #dict_items([('Input.txt', 'Randy'), ('Code.py', 'Stan'), ('Output.txt', Randy)])

        if value not in result.keys():

            # append the values into the result dictionary
            # by interchanging the key, values.
            result[value] = [key]
        else:

            # Append the other file name if the owner is same.
            result[value].append(key)

    return result

print(group_by_owners(files))
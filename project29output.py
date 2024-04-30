def flames_meaning(result):
    switcher = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Affectionate',
        'M': 'Married',
        'E': 'Enemies',
        'S': 'Separated'
    }
    return switcher.get(result)

def flames(name1, name2):
    flames = 'FLAMES'
    for x in name1:
        if x in name2:
            name2 = name2.replace(x, '', 1)
            name1 = name1.replace(x, '', 1)
    flamed_name = name1 + name2
    flamed_name_length = len(flamed_name)
    while len(flames) != 1:
        if len(flames) >= flamed_name_length:
            striked_out_char = flames[flamed_name_length - 1]
            flames = flames.replace(striked_out_char, '', 1)
        else:
            striked_out_char = flames[-1]
            flames = flames[:-1]
        for i, char in enumerate(flames):
            if char == striked_out_char:
                flames = flames[:i] + flames[i+1:]
    return flames_meaning(flames)

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
print("The relationship between " + name1 + " and " + name2 + " is " + flames(name1, name2))

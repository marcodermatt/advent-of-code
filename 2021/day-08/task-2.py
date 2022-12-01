with open("input.txt") as f:
    data = [line.split() for line in f.readlines()]

sum = 0
for line in data:
    for entry in line[:10]:
        match len(entry):
            case 2:
                one = set(entry)
            case 3:
                seven = set(entry)
            case 4:
                four = set(entry)
            case 7:
                eight = set(entry)
    output = ''
    for digit in line[11:]:
        match len(digit):
            case 2:
                output += '1'
                one = digit
            case 3:
                output += '7'
                seven = digit
            case 4:
                output += '4'
                four = digit
            case 7:
                output += '8'
                eight = digit
            case 5:
                if len(set(digit).intersection(one)) == 2:
                    output += '3'
                elif len(set(digit).intersection(four)) == 2:
                    output += '2'
                else:
                    output += '5'
            case 6:
                if len(set(digit).intersection(one)) == 1:
                    output += '6'
                elif len(set(digit).intersection(four)) == 3:
                    output += '0'
                else:
                    output += '9'
            case _:
                output += '_'
    sum += int(output)
print(sum)
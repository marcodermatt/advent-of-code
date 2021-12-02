if __name__ == '__main__':

    with open("day-1/input.txt") as f:
        previous = 700
        counter = 0
        for line in f:
            if previous < int(line):
                counter += 1
            previous = int(line)
        print(counter)

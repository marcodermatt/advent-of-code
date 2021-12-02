if __name__ == '__main__':

    with open("input.txt") as f:
        previous = 700
        counter = 0
        input_data = []
        for line in f:
            input_data.append(int(line))

        window_size = 3

        for i in range(len(input_data) - window_size + 1):
            window_sum = sum(input_data[i: i + window_size])
            if previous < window_sum:
                counter += 1
            previous = window_sum

        print(counter)

import random as r


def fill(filename, rows, min_x_y=-100, max_x_y=100):
    with open(filename, "w") as file:
        for i in range(rows):
            line = ""
            for j in range(3):
                point = str(r.randint(min_x_y, max_x_y)) + " " + str(r.randint(min_x_y, max_x_y))
                line += point
                if j != 2:
                    line += ","
            if i != rows - 1:
                line += "\n"
            file.write(line)


if __name__ == '__main__':
    fill("input05.txt", 100)
import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def __str__(self):
        return f"<Triangle " \
               f"({self.point1.x}, {self.point1.y}), " \
               f"({self.point2.x}, {self.point2.y}), " \
               f"({self.point3.x}, {self.point3.y})>"

    def __repr__(self):
        return f"{self.point1.x} {self.point1.y}," \
               f"{self.point2.x} {self.point2.y}," \
               f"{self.point3.x} {self.point3.y}"


def get_data_from_file(filename):
    triangles = []
    with open(filename, "r") as file:
        file_data = file.readlines()
        for i in range(len(file_data)):
            points = file_data[i].split(",")
            points = [Point(*[int(n) for n in i.split(" ")]) for i in points]
            triangles.append(Triangle(*points))
    return triangles


def write_triangles_to_file(filename, triangles):
    with open(filename, "w") as file:
        for i in range(len(triangles)):
            file.writelines(repr(triangles[i]))
            if i != len(triangles) - 1:
                file.writelines("\n")


def is_in_one_quarter(triangle):
    points = [triangle.point1, triangle.point2, triangle.point3]
    x_set = set()
    y_set = set()
    for point in points:
        x_set.add(True if point.x >= 0 else False)
        y_set.add(True if point.y >= 0 else False)
    return len(x_set) == 1 and len(y_set) == 1


def get_in_one_quarter_triangles(triangles):
    in_one_quarter_triangles = []
    for t in triangles:
        if is_in_one_quarter(t):
            in_one_quarter_triangles.append(t)
    return in_one_quarter_triangles


if __name__ == '__main__':
    if len(sys.argv) > 1:
        triangles = get_data_from_file(sys.argv[1])
        in_one_quarter_triangles = get_in_one_quarter_triangles(triangles)
        write_triangles_to_file(sys.argv[2], in_one_quarter_triangles)
    else:
        triangles = get_data_from_file(input("Enter input file: "))
        in_one_quarter_triangles = get_in_one_quarter_triangles(triangles)
        write_triangles_to_file(input("Enter output file: "), in_one_quarter_triangles)
    [print(t) for t in in_one_quarter_triangles]

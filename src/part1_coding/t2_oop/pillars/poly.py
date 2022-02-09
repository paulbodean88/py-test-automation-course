def add(x, y, z=0, data_type=str):
    if data_type is str:
        return str(x) + str(y) + str(z)
    else:
        return x + y + z


print(add(1, 2))
print(add(1, 2, 4))
print(add("a", "B", data_type=str))
my_list = [(-1 + 0j), 1, 2.2, True, None, 'string', [3,4], range(11), (b"twelve"), frozenset(),]

for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")
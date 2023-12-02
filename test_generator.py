def try_generator():
    for data in (1, 2, 3, 4, 5):
        yield data #←ここでdataが一度、返却される
# def main():
#     for data in try_generator():
#         print(data)
#         if data > 2:
#             break

def main():
    gene = (i for i in range(5))
    for i in gene:
        print(i)
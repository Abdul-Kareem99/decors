import datetime


path = 'C:/Users/User/PycharmProjects/decors_hw/'
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]]


def main_decorator(my_path):
    def sub_decorator(func):
        def logger(*args, **kwargs):
            current_datetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            result = func(*args, **kwargs)
            with open(f'{my_path}logs.txt', 'w') as f:
                f.write(f'{current_datetime}, название функции - {func.__name__}, аргументы функции - {args, kwargs},'
                        f'возвращаемое значение - {result}\n')
            return result
        return logger
    return sub_decorator


main_decorator(path)


class FlatIterator:

    def __init__(self, my_list):
        self.my_list = my_list

    def __iter__(self):
        self.cursor = 0
        self.sub_cursor = -1
        return self

    @main_decorator(path)
    def __next__(self):
        if self.sub_cursor + 1 < len(self.my_list[self.cursor]):
            self.sub_cursor += 1
        elif self.cursor + 1 < len(self.my_list):
            self.cursor += 1
            self.sub_cursor = 0
        else:
            raise StopIteration
        return self.my_list[self.cursor][self.sub_cursor]


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)




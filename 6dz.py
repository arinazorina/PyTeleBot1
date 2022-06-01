import os

import argparse

if __name__ == "__main__":
    print("Hello!")
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-n", "--name", default="мир!", help='имя пользователя')
    parser.add_argument("-a", '--age', default=0, help='введите возраст')
    path = os.getcwd()
    args = parser.parse_args()
    file = open(args.path, 'a')
    print(f'hi {args.name}!')
    print(args)
    try:
        file.write('name- ' + args.name + '\n')
        file.write('age- ' + (str(args.age)) + '\n')
    finally:
        file.close()
else:
    print("файл запущен не напрямую")


from recursion_directory import recursion_file
import sys

# Проверяем, есть ли аргумент командной строки
if __name__=='__main__':
    if len(sys.argv) > 1:
        target_directory = sys.argv[1]
        recursion_file(target_directory)
    else:
        print("Укажите путь к целевой папке в аргументах командной строки.")
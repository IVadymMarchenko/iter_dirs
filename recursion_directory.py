from normalize import normalize
from pathlib import Path
import shutil
import sys


def recursion_file(file):
    file_iter=Path(file)
    categories = {'images':[], 'video':[], 'audio':[], 'documents':[], 'archives':[]}
    known_extensions = {
        'images': ('.jpeg', '.png', '.jpg', '.svg'),
        'video': ('.avi', '.mp4', '.mov', '.mkv'),
        'audio': ('.mp3', '.ogg', '.wav', '.amr'),
        'documents': ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
        'archives': ('.zip', '.gz', '.tar'),
    }
    known_file= set()
    unknown_file= set()
    #рекурсивно обходим все папки и файлы
    for i in file_iter.glob("**/*"):
        category = False
        if i.is_dir():
            #если папка пустая удаляем её
            if not list(i.iterdir()):
                shutil.rmtree(i)
                #сли это файл то проверяем на наличие его разрешения в словаре
        if i.is_file():
            for dir, type in known_extensions.items():
                #Создаем папку по ключу словаря и переносим файл туда также переносим i.suffix в known_file
                if i.suffix in type:
                    new_dir = file_iter / dir
                    new_dir.mkdir(parents=True, exist_ok=True)
                    i.rename(new_dir / normalize(i.name))
                    known_file.add(i.suffix)
                    categories.get(dir,[]).append(i.name)
                    category=True
                    break
            if not category:
                unknown_file.add(i.suffix)


        #Проверяем есть ли папка 'archives'
    zips=Path(file_iter/'archives')
    if zips.is_dir():
        new_zips_file=zips/'archives'
        new_zips_file.mkdir(parents=True,exist_ok=True)
        #Итерируемся по содержимому папки 'archives'
        # Делаем распаковку
        for i in zips.iterdir():
            if i.suffix in known_extensions['archives']:
                shutil.unpack_archive(i,new_zips_file)
    #Проходим рекурсией по папкам и если они пустые то удаляем их если нет меняем имя
    for i in file_iter.glob('**/*'):
        if i.is_dir() and not list(i.iterdir()) and i.name not in known_extensions.keys():
            shutil.rmtree(i)
        else:
            new_name = normalize(i.name)
            i.rename(i.with_name(new_name))
    #Получаем список файлов по категориям
    for i, j in categories.items():
        print(i,j)
    print(f'Список всех известных расширений:{list(known_file)}')
    print(f'Список всех не известных расширений:{list(unknown_file)}')

recursion_file('D:\dir_for_python')
















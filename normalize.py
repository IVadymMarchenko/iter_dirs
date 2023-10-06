import string

def normalize(stryng: str):
    ascll=string.ascii_letters
    trnsliteration_dict = {
        'а': 'a','б': 'b','в': 'v','г': 'h',
        'д': 'd','е': 'e','ё': 'yo','ж': 'zh',
        'з': 'z','и': 'i','й': 'y','к': 'k','л': 'l',
        'м': 'm','н': 'n','о': 'o','п': 'p','р': 'r',
        'с': 's','т': 't','у': 'u','ф': 'f','х': 'kh','ц': 'ts',
        'ч': 'ch','ш': 'sh','щ': 'sch','ъ': '','ы': 'y','ь': '',
        'э': 'uh','ю': 'yu','я': 'ya', 'А': 'A','Б': 'B','В': 'V','Г': 'H',
        'Д': 'D','Е': 'E','Ё': 'Yo','Ж': 'Zh',
        'З': 'Z','И': 'I','Й': 'Y','К': 'K','Л': 'L',
        'М': 'M','Н': 'N','О': 'O','П': 'P','Р': 'R',
        'С': 'S','Т': 'T','У': 'U','Ф': 'F','Х': 'Kh','Ц': 'Ts',
        'Ч': 'Ch','Ш': 'Sh','Щ': 'Sch','Ъ': '','Ы': 'Y','Ь': '',
        'Э': 'Uh','Ю': 'Yu','Я': 'Ya','.': '.'

    }
    result_string = ''
    for i in stryng:
        if i.lower() in trnsliteration_dict:
            result_string+=trnsliteration_dict[i]
        elif i.isdigit():
            result_string+=i
        elif i in ascll:
            result_string+=i
        else:
            result_string+='_'

    return result_string


#print(normalize('афAРа57?.txt'))

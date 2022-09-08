import csv

lst_greetings = ['здравствуйте', 'добрый день', 'добрый вечер', 'здравствуй', 'доброе утро', 'приветствую', 'привет',
                 'здарова', 'здравия желаем', 'здравия желаю', 'приветствую вас', 'салют', 'хеллоу', 'хелло', 'здоров',
                 'здрасте', 'приветик', 'физкульт-привет', 'хай', 'добрый', 'хаюшки']

lst_parting = ['до свидания', 'до встречи', 'будьте здоровы', 'всего наилучшего', 'пока', 'бывай', 'доброго',
               'до новых встреч', 'до связи', 'до скорой встречи', 'счастливо', 'гуд-бай', 'бай',
               'разрешите откланяться', 'счастливо оставаться', 'до скорого', 'удачи', ' честь имею']

lst_presentation = ['зовут', 'мое имя', 'это']

lst_company = ['компания', 'из компании', 'представляю', 'компанию']

with open('test_data.csv', 'r', encoding='utf-8') as csv_file:
    headers = next(csv_file)
    reader = csv.reader(csv_file)
    manager_info = {}
    result = []
    dlg_id = -1

    for row in reader:
        if row[0] != dlg_id:
            if dlg_id != -1:
                result.append(manager_info)
                manager_info = {}
            dlg_id = row[0]
            manager_info[dlg_id] = dlg_id

        if row[2] == 'manager':

            manager_replica = row[3].lower()

            result_greetings = [s for s in lst_greetings if s in manager_replica]
            if result_greetings:
                manager_info['greetings'] = row[3]

            result_parting = [s for s in lst_parting if s in manager_replica]
            if result_parting:
                manager_info['parting'] = row[3]

            if 'presentation' not in manager_info.keys():
                result_presentation = [s for s in lst_presentation if s in manager_replica]
                if result_presentation:
                    if result_presentation[0] != 'зовут' or manager_replica.split('зовут')[0].split('меня')[1] == ' ':
                        try:
                            repr_str = manager_replica.split(result_presentation[0] + ' ')[1].split()[0].capitalize()
                            manager_info['name'] = repr_str
                        except:
                            pass
                    else:
                        try:
                            repr_str = manager_replica.split('зовут')[0].split('меня' + ' ')[1].split()[0].capitalize()
                            manager_info['name'] = repr_str
                        except:
                            pass

                    manager_info['presentation'] = row[3]
            if 'company' not in manager_info.keys():
                result_company = [s for s in lst_company if s in manager_replica]
                if result_company:
                    try:
                        repr_str = manager_replica.split(result_company[0])[1].split()[0].capitalize()
                        manager_info['company'] = repr_str
                    except:
                        pass

print(result)

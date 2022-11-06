def title():
    try:
        text = input('words -> ')
        title = text.title()
        print(title)

        dig_count = text.count('1') + text.count('2') + text.count('3')+ text.count('4')+ text.count('5')+ text.count('6')+ text.count('7')+ text.count('8') + text.count('9') + text.count('0')
        print(f'digital count = {dig_count}')

        a = text.count('.')
        b = text.count('!')
        c = text.count(',')
        d = text.count(':')
        e = text.count(';')
        print(f'punctuation count :\n"." = {a}\n"!" = {b}\n"," = {c}\n":" = {d}\n";" = {e}')

    except Exception as ex:
        print(f'Error: {ex}')
title()
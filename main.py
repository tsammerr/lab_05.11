def list():
    try:
        text = input('numbers -> ')
        b = input('search number -> ')
        count = text.count(b)
        print(f'Count of {b}:', count)

    except Exception as ex:
        print(f'Error: {ex}')
list()
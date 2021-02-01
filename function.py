def add():
    try:
        x = float(input('skriv inn tal '))
        t = float(input('skriv inn tal '))
        svar = x + t
        print('{} plusset {} = {}'.format(x,t,svar))
    except:
        print('noko stemme dårle')
        add()

def add():
    try:
        x = float(input('skriv inn tal '))
        t = float(input('skriv inn tal '))
        svar = x + t
        print('{} + {} = {}'.format(x,t,svar))
    except:
        print('noko stemme dårle')
        add()

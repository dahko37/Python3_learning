"""

graficas : este programa visualiza una serie de graficas en un espacio 2d

Made by Alejandro Gonzalvo
Github: https://github.com/dahko37/Python3_learning

"""


import matplotlib.pyplot as plt

from numpy import linspace

from cmath import sin, cos, pi



def espiral_1():
    """Representa la función R(t) = t / 2pi para: 0 <= t <= 2pi"""
    
    x_val = []
    y_val = []
    
    for t in linspace(0, 4*pi, 2000):
        r = t / (2*pi)
        x = r * cos(t)
        y = r * sin(t)
        x_val.append(x)
        y_val.append(y)

    return x_val, y_val


def espiral_2():
    """Representa la función R(t) = 1 - t / 2pi para: 0 <= t <= 2pi"""

    x_val = []
    y_val = []
    
    for t in linspace(0, 2*pi, 2000):
        r = 1 - (t / (2*pi))
        x = r * cos(t)
        y = r * sin(t)
        x_val.append(x)
        y_val.append(y)

    return x_val, y_val


def cardioide_1():
    """
    Representa la ecuacion parametrica:

    x = (1 + cost)cost
    y = (1 + cost)sent

    para: 0 <= t <= 2pi

    """

    x_val = []
    y_val = []

    for t in linspace(0, 2*pi, 2000):
        x = (1 + cos(t))*cos(t)
        y = (1 + cos(t))*sin(t)

        x_val.append(x)
        y_val.append(y)

    return x_val, y_val


def cardioide_2():
    """
    Representa la ecuacion parametrica:

    x = (1 - cost)cost
    y = (1 - cost)sint

    para: 0 <= t <= 2pi

    """

    x_val = []
    y_val = []

    for t in linspace(0, 2*pi, 2000):
        x = (1 - cos(t))*cos(t)
        y = (1 - cos(t))*sin(t)

        x_val.append(x)
        y_val.append(y)

    return x_val, y_val


def flor_1():
    """
    
    Representa la equacion parametrica:
    
    x = 2.5*sin**2(-5*t)*2**cos(cos(4.28*2.3*t))
    y = 2.5*sin(sin(-5*t))*cos**2(4.28*2.3*t)

    para: -6 <= t <= 6
    
    """

    x_val = []
    y_val = []

    for t in linspace(-8, 8, 50000):
        x = 2.5*(sin(-5*t)**11)*(2**cos(cos(4.28*2.3*t)))
        y = 2.5*sin(cos(-5*t))*cos(4.28*2.3*t)**3
        x_val.append(x)
        y_val.append(y)

    return x_val, y_val

def nudo():
    """

    Representa la equacion paramétrica:

    x = (3*t) / (1 + t**3)
    y = (3*t**2) / (1 + t**3)

    """

    x_val = []
    y_val = []

    for t in linspace(-1000, 1000, 10000):

        x = (3*t) / (1 + t**3)
        y = (3*t**2) / (1 + t**3)
        x_val.append(x)
        y_val.append(y)

    return x_val, y_val        

def cardinal():
    """

    Representa la equacion parametrica:

    x = cos(t)**n
    y = sen(t)**n

    para: 0 < t < 2pi, n = 1,3,5 

    """

    x_val = []
    y_val = []
    n_val = [1, 3, 5] 

    for n in n_val:
        for t in linspace(0, 2*pi, 1000):

            x = cos(t)**n
            y = sin(t)**n
            x_val.append(x)
            y_val.append(y)

    return x_val, y_val

def red():
    """

    Representa la equacion parametrica:

    x = cos(3*t)
    y = sin(5*t)

    para: 0 < t < 2pi, n = 1,3,5 

    """

    x_val = []
    y_val = [] 

    for t in linspace(0, 2*pi, 1000):

        x = cos(3*t)
        y = sin(5*t)
        x_val.append(x)
        y_val.append(y)

    return x_val, y_val
    

def main():
    """Ejecuta el programa principal"""

    while True:    
        listaeq = [
            'espiral_1',
            'espiral_2',
            'cardioide_1',
            'cardioide_2',
            'flor_1',
            'nudo',
            'cardinal',
            'red',
            'salir'
            ]

        print('\n{0}'.format(listaeq))
        a = input('\nSeleccione la equacion que desea visualizar: ')

        if a in listaeq:

            try:
                lnw = float(input('\n seleccione el grosor de linea(0-2): '))

            except ValueError:
                print('\nERROR: INTRODUZCA UN NÚMERO POR FAVOR.')
                continue

            if a == 'espiral_1':
                x_val, y_val = espiral_1()

            if a == 'espiral_2':
                x_val, y_val = espiral_2()

            if a == 'cardioide_1':
                x_val, y_val = cardioide_1()

            if a == 'cardioide_2':
                x_val, y_val = cardioide_2()

            if a == 'flor_1':
                x_val, y_val = flor_1()

            if a == 'nudo':
                x_val, y_val = nudo()

            if a == 'cardinal':
                x_val, y_val = cardinal()

            if a == 'red':
                x_val, y_val = red()

            plt.plot(x_val, y_val, lnw)
            plt.show()

        elif a == 'salir':
            break


        else:
            print('ERROR: LA EQUACIÓN INTRODUCIDA NO EXISTE')


main()
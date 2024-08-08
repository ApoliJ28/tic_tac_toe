from os import system

# Diccionario de letra del jugador

dict_player = {
    1: 'X',
    2: 'O'
}

dict_letter_player = {
    'X': 1,
    'O': 2
}

# Creamos las filas en formas de listas, y las columnas son los indices de estas listas

tablero = [
            ['-','-','-'],
            ['-','-','-'],
            ['-','-','-']
            ]

# Funcion para mostrar el tablero actual

def mostrar_tablero() -> None:

    for i in range(len(tablero)):
        # print(i)
        if i == 0:
            print('   0 | 1 | 2 -> columns')
            print('  -----------')
        row = f'{i}  '
        for j in range(len(tablero[i])):
            # print(j)
            row += f"{tablero[i][j]} {'| ' if j != 2 else ''}"
        print(row)
        print('  -----------')
    print('|')
    print('\/')
    print('rows')

# Funcion para cambiar los valores del tablero

def update_tablero(letter, row, col) -> None:
    tablero[row][col] = letter

def valida_tablero_lleno() -> bool:
    contador = 0
    
    for row in tablero:
        for values in row:
            contador += 1 if not values == '-' else 0
    return True if contador >= 9 else False

def validar_ganador() -> str:
    
    letters = ["X", "O"]
    ganador = ""
    # Validar ganador en filas:
    for letter in letters:
        for list_row in tablero:
            conteo = 0
            for value in list_row:
                conteo += 1 if value == letter else 0
            if conteo == 3:
                ganador = letter
                break
    
    # validar ganador en columnas
    
    if not ganador:
        n_columns = len(tablero[0])
        for letter in letters:
            for n_column in range(n_columns):
                conteo=0
                for list_row in  tablero:
                    
                    conteo += 1 if list_row[n_column] == letter else 0
                if conteo == 3:
                    ganador = letter
                    break
    # Validar ganador en diagonales
    
    if not ganador:
        n_columns = len(tablero[0])
        
        for letter in letters:
            conteo=0
            for n_column in range(n_columns):
                conteo += 1 if tablero[n_column][n_column] == letter else 0
            
            if conteo == 3:
                ganador = letter
                break
            
            conteo=0
            for n_column in range(n_columns):
                conteo += 1 if tablero[n_column][(n_columns -1) - n_column] == letter else 0
            
            if conteo == 3:
                ganador = letter
                break
    
    return ganador

def validar_campo_lleno(row, column) -> bool:
    return True if not tablero[row][column] == '-' else False 

#Funcion main

def main() -> None:
    
    play = True
    
    while play:
        
        global tablero

        tablero = [
                    ['-','-','-'],
                    ['-','-','-'],
                    ['-','-','-']
                    ]

    
        player = 1
        
        while not (valida_tablero_lleno() or validar_ganador()):
            while True:
                mostrar_tablero()
                while True:
                    
                    player_row = int(input(f'Jugador {player} selecccione la fila (0-2): '))
                    
                    if not player_row in range(3):
                        
                        print('Por favor ingresar una fila en el rago del 0 al 2')
                    else:
                        break
                
                while True:
                
                    player_column = int(input(f'Jugador {player} selecccione la columna (0-2): '))
                    
                    if not player_column in range(3):
                        
                        print('Por favor ingresar una columna en el rago del 0 al 2')
                    else:
                        break
                
                if validar_campo_lleno(row=player_row, column=player_column):
                    system('cls')
                    print('El campo seleccionado ya esta lleno, vuelva a intentar, con los campos vacios')
                else:
                    system('cls')
                    update_tablero(letter=dict_player[player], row=player_row, col=player_column)
                
                    if player == 1:
                        player = 2
                    else:
                        player = 1
                        
                    break
        if validar_ganador():
            print(f'Gann el jugador {dict_letter_player[validar_ganador()]}')
        else:
            print("Empate!")

        while True:
            
            op = input('Quieres volver a jugar? (S/N): ').upper()
            
            if op in ['S','N']:
                if op == 'N':
                    play = False
                system('cls')
                break
            else:
                print('Por favor eliguir una de las dos opciones (s/n).')
                
    print('Gracias por jugar, Vuelva pronto!')


if __name__ == '__main__':
    main()

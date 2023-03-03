class Pawns:
    points = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
              'J': 8, 'K': 5, 'L': 2, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
              'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

    def __init__(self):
        self.letters = []

    def addPawn(self, c):
        """
        Añade una ficha 'c' al array de caracteres letters.
        """
        self.letters.append(c)

    def addPawns(self, c, n):
        """
        Añade 'n' veces, una ficha 'c' al array de caracteres letters.
        """
        for i in range(n):
            self.addPawn(c)

    def createBag(self):
        """
        Crea la bolsa con las 100 fichas del juego.
        """
        import pandas as pd
        filepath = 'docs/bag_of_pawns.csv'
        bag = pd.read_csv(filepath)
        for item in bag.itertuples():
            self.addPawns(item[1], item[2])

    def showPaws(self):
        """
        Muestra las fichas que contiene la bolsa y el número de veces que está repetida cada ficha.
        """
        ft_pawns = self.getFrequency()
        ft_pawns.showFrequency()

    def takeRandomPawn(self):
        """
        Toma una ficha de la bolsa de forma aleatoria y la elimina de la bolsa.
        """
        from numpy import random
        idx = random.randint(0, self.getTotalPawns() - 1)
        letter = self.letters[idx]
        self.letters.remove(letter)
        return letter

    def getFrequency(self):
        """
        Muestra la frequencia de aparición de cada ficha.
        """
        ft = FrequencyTable()
        for c in self.letters:
            ft.update(c)
        return ft

    def takePawn(self, c):
        """
        Toma la ficha 'c' de la bolsa y la elimina de la bolsa.
        """
        self.letters.remove(c)

    def getTotalPawns(self):
        """
        Obtenemos el total de fichas del objeto.
        """
        return len(self.letters)

    @staticmethod
    def getPoints(c):
        """
        Devuelve los puntos de la ficha 'c'.
        """
        return Pawns.points[c]

    @staticmethod
    def showPawnsPoints():
        """
        Muestra por pantalla la puntuación de cada ficha.
        """
        print('Puntos de cada ficha: ')
        count = 0
        fin = '   '
        for key in Pawns.points:
            print(f'{key}:{" " if Pawns.getPoints(key) < 9 else ""}{Pawns.getPoints(key)}', end=fin)
            count += 1
            fin = '\n' if count % 3 == 2 else '   '


class Word:

    def __init__(self):
        self.word = []

    def __str__(self):
        """
        Imprimimos la palabra en formato string.
        """
        string = ''
        for i in range(self.getLengthWord()):
            string += self.word[i]
        return string

    def areEqual(self, w):
        """
        Comprueba si dos palabras son iguales.
        """
        return self.word == w.word

    def isEmpty(self):
        """
        Comprueba si una palabra está vacía.
        """
        return self.getLengthWord() == 0

    @classmethod
    def readWord(cls):
        """
        Lee una palabra por teclado y la devuelve como un objeto de la clase Word.
        """
        input_word = input().strip()
        w = Word()
        for c in input_word.upper():
            w.word.append(c)
        return w

    @staticmethod
    def readWordFromFile(f):
        """
        Lee una palabra del fichero 'f' y la devuelve como un objeto de la clase word.
        """
        w = Word()
        file_word = f.readline()
        # Consideramos toda la línea alvo el salto de línea \n --> solo consideramos la palabra.
        for c in file_word[:-1]:
            w.word.append(c)
        return w

    def getFrequency(self):
        """
        Muestra la frecuencia de aparición de cada letra en una palabra.
        """
        ft = FrequencyTable()
        for c in self.word:
            ft.update(c)
        return ft

    def getLengthWord(self):
        """
        Devuelve la longitud de la palabra.
        """
        return len(self.word)


class Dictionary:
    filepath = 'C:/APYLABRADOS/docs/dictionary.txt'

    @staticmethod
    def validateWord(word):
        """
        Comprueba si la palabra word se encuentra en el diccionario.
        """
        with open(Dictionary.filepath, 'r') as f:
            w = Word.readWordFromFile(f)
            while not w.isEmpty() and not word.areEqual(w):
                w = Word.readWordFromFile(f)

        if w.isEmpty() and not word.areEqual(w):
            print('La palabra no se encuentra en el diccionario.')
            return False

        else:
            return True

    @staticmethod
    def showWords(pawns):
        """
        Muestra todas las posibles palabras que se pueden formar con las fichas de pawns.
        """
        tf_pawns = pawns.getFrequency()
        count = 0
        fin = ' '
        with open(Dictionary.filepath, 'r') as f:
            word = Word.readWordFromFile(f)
            while not word.isEmpty():
                n = word.getLengthWord()
                tf_word = word.getFrequency()
                if FrequencyTable.isSubset(tf_word, tf_pawns):
                    print(word, end=fin * (10 - n) if fin == ' ' else fin)
                    count += 1
                    fin = '\n' if count % 5 == 4 else ' '
                word = Word.readWordFromFile(f)

    @staticmethod
    def showWordsPlus(pawns, c):
        """
        Muestra todas las posibles palabras que contienen el caracter 'c'
        y que se pueden formar con las fichas de pawns.
        """
        tf_pawns = pawns.getFrequency()
        tf_pawns.update(c)
        count = 0
        fin = ' '
        with open(Dictionary.filepath, 'r') as f:
            word = Word.readWordFromFile(f)
            while not word.isEmpty():
                n = word.getLengthWord()
                if c in word.word:
                    tf_word = word.getFrequency()
                    if FrequencyTable.isSubset(tf_word, tf_pawns):
                        print(word, end=fin * (10 - n) if fin == ' ' else fin)
                        count += 1
                        fin = '\n' if count % 5 == 4 else ' '
                word = Word.readWordFromFile(f)
        print('')


class FrequencyTable:

    def __init__(self):
        self.letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        self.frequencies = [0 for _ in range(0, len(self.letters))]

    def showFrequency(self):
        """
        Muestra la frecuencia de aquellas letras con frecuencia diferente a 0.
        """
        for i in range(len(self.letters)):
            if self.frequencies[i] != 0:
                print(f'{self.letters[i]}: {self.frequencies[i]}')

    @staticmethod
    def isSubset(ft1, ft2):
        """
        Comprueba si ft1 es subconjunto de ft2.
        """
        for x in range(len(ft1.frequencies)):
            if ft1.frequencies[x] > ft2.frequencies[x]:
                return False
        return True

    def update(self, c):
        """
        Actualiza la frecuencia de la letra 'c' que pasemos por parámetro (suma 1)
        """
        idx = self.letters.index(c)
        self.frequencies[idx] += 1

    def delete(self, c):
        """
        Actualiza la frecuencia de la letra 'c' que pasemos por parámetro (resta 1)
        """
        idx = self.letters.index(c)
        self.frequencies[idx] -= 1


class Board:
    score = 0

    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.totalWords = 0
        self.totalPawns = 0
        self.multiplier = [[(1, '') for j in range(15)] for i in range(15)]

    def showBoard(self):
        """
        Muestra el tablero.
        """
        # Librerias necesarias
        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd

        # Genera vertices para pintarlos.
        def generate_vertex(center_x, center_y):
            vertex = np.array([[center_x - 0.5, center_y - 0.5], [center_x - 0.5, center_y + 0.5],
                               [center_x + 0.5, center_y + 0.5], [center_x + 0.5, center_y - 0.5]])
            return vertex

        # Función que pasa del intervalo (-1, 16) al (0, 1)
        def transformation(x):
            return (x + 1) / 17

        filepath = 'docs/xycolor_board.csv'
        xycolors = pd.read_csv(filepath)

        # Creamos la figura del tablero
        fig = plt.figure(figsize=[10, 10])
        ax = fig.add_subplot(111)

        # Dibujamos las verticales y horiszontales.
        for x in range(16):
            ax.plot([x, x], [0, 15], 'k')
        for y in range(16):
            ax.plot([0, 15], [y, y], 'k')

        # Definimos los límites.
        ax.set_xlim(-1, 16)
        ax.set_ylim(-1, 16)

        # Escalamos la figura.
        ax.set_position([0, 0, 1, 1])

        # Eliminamos ejes.
        ax.set_axis_off()

        # Pinta los cuadrados.
        for row in xycolors.itertuples():
            polygon = plt.Polygon(generate_vertex(row[1], row[2]), color=row[3])
            ax.add_artist(polygon)

        for i in range(len(self.board)):
            # Números horizontales.
            ax.text(transformation(i + 0.5), transformation(15.5), str(i),
                    verticalalignment='center', horizontalalignment='center',
                    fontsize=20, fontfamily='fantasy', fontweight='bold',
                    transform=ax.transAxes)
            # Números verticales.
            ax.text(transformation(15.5), transformation(i + 0.5), str(14 - i),
                    verticalalignment='center', horizontalalignment='center',
                    fontsize=20, fontfamily='fantasy', fontweight='bold',
                    transform=ax.transAxes)
            # Letras.
            for j in range(len(self.board)):
                ax.text(transformation(j + 0.5), transformation(14 - i + 0.5), self.board[i][j],
                        verticalalignment='center', horizontalalignment='center',
                        transform=ax.transAxes, fontsize=15)

        ax.text(transformation(0), transformation(-0.5), f'Score: {Board.score}',
                verticalalignment='center', horizontalalignment='left',
                fontsize=25, fontfamily='fantasy', fontweight='bold',
                transform=ax.transAxes)

        deal7Pawns()

        pawn_pos = 4
        for pawn in player_pawns.letters:
            polygon = plt.Polygon(generate_vertex(pawn_pos, -0.6), color='#FFF68F')
            ax.add_artist(polygon)
            ax.text(transformation(pawn_pos), transformation(-0.6), pawn,
                    verticalalignment='center', horizontalalignment='center',
                    transform=ax.transAxes, fontsize=15)
            pawn_pos += 1.5

        plt.show()

    def placeWord(self, player_pawns2, word, x, y, direction):
        """
        Colocamos la palabra word sobre el tablero y eliminamos las fichas usadas de la bolsa del jugador.
        """
        word_points = 0
        word_multiplier = 1
        for letter in word.word:
            if letter != self.board[x][y]:
                player_pawns2.takePawn(letter)
                self.totalPawns += 1
                self.board[x][y] = letter

                if self.multiplier[x][y][1] != 'w':  # Multiplicador de pawn o nada.
                    word_points += Pawns.getPoints(letter) * self.multiplier[x][y][0]
                else:  # Multiplicador de word.
                    word_points += Pawns.getPoints(letter)
                    word_multiplier *= self.multiplier[x][y][0]

            if direction == 'V':
                x += 1
            if direction == 'H':
                y += 1

        Board.score += word_points * word_multiplier
        self.totalWords += 1

    def isPossible(self, word, x, y, direction):
        """
        Comprueba si es posible colocar la palabra en la posición elegida.
        """
        x0 = x
        y0 = y

        # Si es el primer turno, comprobamos si alguna ficha se situa sobre la casilla central.
        if self.totalWords == 0:
            message = 'Ninguna ficha pasa por la casilla central'
            if direction == 'V':
                if y0 != 7:
                    return False, message
                elif x0 + word.getLengthWord() - 1 < 7 or x0 > 7:
                    return False, message

            if direction == 'H':
                if x0 != 7:
                    return False, message
                elif y0 + word.getLengthWord() - 1 < 7 or y0 > 7:
                    return False, message

        else:
            # Comprobamos si la palabra se sale del tablero.
            message = 'La palabra se sale del tablero'
            if x0 < 0 or x0 >= 15 or y0 < 0 or y0 >= 15:
                return False, message
            if direction == 'V' and x0 + word.getLengthWord() - 1 >= 15:
                return False, message
            if direction == 'H' and y0 + word.getLengthWord() - 1 >= 15:
                return False, message

            # Comprobamos si se utiliza alguna ficha del tablero para formar la palabra
            x = x0
            y = y0
            blanks = []
            for c in word.word:
                if self.board[x][y] == ' ':
                    blanks.append(c)

                if direction == 'V':
                    x += 1
                if direction == 'H':
                    y += 1

            if len(blanks) == word.getLengthWord():
                message = 'No se está utilizando ninguna ficha del tablero'
                return False, message

            # Comprobamos si la casilla está libre u ocupada por la misma letra.
            x = x0
            y = y0
            for c in word.word:
                if self.board[x][y] != ' ' and self.board[x][y] != c:
                    message = 'Hay una ficha diferente ocupando una posición'
                    return False, message
                if direction == 'V':
                    x += 1
                if direction == 'H':
                    y += 1

            # Comprobamos si se coloca una nueva ficha en el tablero.
            x = x0
            y = y0
            matching = []
            for c in word.word:
                if self.board[x][y] == c:
                    matching.append(c)
                if direction == 'V':
                    x += 1
                if direction == 'H':
                    y += 1

            if len(matching) == word.getLengthWord():
                message = 'No se está colocando ninguna ficha nueva en el tablero'
                return False, message

            # Comprobamos que no hay fichas adicionales a principio y final de la palabra.
            message = 'Hay fichas adicionales a principio o final de la palabra'
            x = x0
            y = y0
            if direction == 'V' and ((x != 0 and self.board[x - 1][y] != ' ') or
                                     (x + word.getLengthWord() != 14 and self.board[x + word.getLengthWord()][
                                         y] != ' ')):
                return False, message
            if direction == 'H' and ((y != 0 and self.board[x][y - 1] != ' ') or
                                     (y + word.getLengthWord() != 14 and self.board[x][
                                         y + word.getLengthWord()] != ' ')):
                return False, message

        message = 'La palabra se puede colocar en el tablero'
        return True, message

    def getPawns(self, word, x, y, direction):
        """
        Dada una palabra, posición y dirección, devuelve las letras necesarias para formar la palabra word.
        """
        needed_letters = Word()
        possible, message = self.isPossible(word, x, y, direction)

        if not possible:
            print(message)
        else:
            for c in word.word:
                if self.board[x][y] != c:
                    needed_letters.word.append(c)
                if direction == 'V':
                    x += 1
                if direction == 'H':
                    y += 1
        return needed_letters

    def showWordPlacement(self, pawns, word):
        """
        Dadas las fichas del jugador y una palabra, muestra las posibles colocaciones de la palabra.
        """
        for direction in ['V', 'H']:
            print(f'{"//Vertical//" if direction == "V" else "//Horizontal//"}')
            for i in range(15):
                for j in range(15):
                    if self.isPossible(word, i, j, direction)[0]:
                        needed_pawns = self.getPawns(word, i, j, direction)
                        if FrequencyTable.isSubset(needed_pawns.getFrequency(), pawns.getFrequency()):
                            print(f'(Fila = {i}, Columna = {j})')

    def setUpMultiplier(self):
        """
        Configura el multiplicador de cada casilla.
        """
        import pandas as pd
        filepath = 'docs/multiplier_boardcsv.txt'
        multipliers = pd.read_csv(filepath)
        for row in multipliers.itertuples():
            self.multiplier[row[1]][row[2]] = (row[3], row[4])


# Variables que serán globales
end = ''
show_help = ''
show_help_plus = ''
bag_of_pawns = ''
player_pawns = ''
board = ''


def startGame():
    """
    Inicializa todas las variables para comenzar una nueva partida.
    """
    # Creamos las variables booleanas end, show_help y show_help_plus
    global end
    end = False
    global show_help
    show_help = True
    global show_help_plus
    show_help_plus = True

    # Creamos la bolsa de fichas del juego
    global bag_of_pawns
    bag_of_pawns = Pawns()
    bag_of_pawns.createBag()

    # Creamos las fichas del jugador
    global player_pawns
    player_pawns = Pawns()

    # Creamos el tablero de juego
    global board
    board = Board()
    Board.score = 0
    board.setUpMultiplier()

    # Mensaje de bienvenida e instrucciones
    welcome()
    instructions()
    deal7Pawns()
    board.showBoard()
    legend()


def legend():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    def generate_vertes(center_x, center_y):
        vertex = np.array([[center_x - 0.5, center_y - 0.5], [center_x - 0.5, center_y + 0.5],
                           [center_x + 0.5, center_y + 0.5], [center_x + 0.5, center_y - 0.5]])
        return vertex

    def transformationX(x):
        return x / 16

    def transformationY(x):
        return (x + 1) / 3

    fig = plt.figure(figsize=[10, 2])
    ax = fig.add_subplot(111)

    ax.set_xlim(0, 16)
    ax.set_ylim(-1, 2)

    # Escalamos.
    ax.set_position([0, 0, 1, 1])

    # Fuera ejes.
    ax.set_axis_off()

    colors = ['#FFCCCC', '#B2FFCD', '#CCCEFF', '#CCF9FF']
    texts = ['x3\nPalabra', 'x2\nPalabra', 'x3\nLetra', 'x2\nLetra']
    for i in range(4):
        polygon = plt.Polygon(generate_vertes(1.5 + 4 * i, 0.5), color=colors[i])
        ax.add_artist(polygon)
        ax.text(transformationX(3.5 + 4 * i), transformationY(.5), texts[i],
                verticalalignment='center', horizontalalignment='center',
                fontsize=25, fontfamily='fantasy', fontweight='bold',
                transform=ax.transAxes)

    plt.show()


def welcome():
    """
    Muestra el mensaje de bienvenida para la primera vez.
    """
    filepath = 'docs/welcome.txt'
    with open(filepath, 'r') as f:
        print(f.read())


def instructions():
    """
    Muestra las instrucciones del juego.
    """
    filepath = 'docs/instrucciones.txt'
    with open(filepath, 'r') as f:
        print(f.read())


def deal7Pawns():
    """
    Reparte fichas al jugador hasta completar las 7 de su mano actual.
    """
    while player_pawns.getTotalPawns() < 7:
        player_pawns.addPawn(bag_of_pawns.takeRandomPawn())


def showOptions():
    """
    Muestra las opciones en caso de que todavia no haya palabra introducida.
    """
    global show_help
    filepath = 'docs/opciones.txt'
    print(f'\n Qué deseas hacer? {"" if show_help else "(Pulsa 9 para ver las diferentes opciones)"}')
    if show_help:
        with open(filepath, 'r') as f:
            print(f.read())
        show_help = False
    ans = input().upper()
    if ans == '9':
        show_help = True
        showOptions()
    elif ans == '1':
        introduceNewWord()
    elif ans == '2':
        print('Estas son tus fichas: ')
        player_pawns.showPaws()
        showOptions()
    elif ans == '3':
        print(f'Puntos: {Board.score}')
        showOptions()
    elif ans == '4':
        Pawns.showPawnsPoints()
        showOptions()
    elif ans == '5':
        helpWithWords()
        showOptions()
    elif ans == '8':
        legend()
        showOptions()
    elif ans == '0':
        endGame()
    else:
        showOptions()


def showOptionsPlus():
    """
    Muestra las opciones en caso de que haya una palabra introducida.
    """
    global show_help_plus
    filepath = 'docs/opciones_plus.txt'
    print(f'\n Qué deseas hacer? {"" if show_help_plus else "(Pulsa 9 para ver las diferentes opciones)"}')
    if show_help_plus:
        with open(filepath, 'r') as f:
            print(f.read())
        show_help_plus = False
    ans = input().upper()
    if ans == '9':
        show_help_plus = True
        showOptionsPlus()
    elif ans == '6':
        introduceCoordinatesAndDirection()
    elif ans == '1':
        introduceNewWord()
    elif ans == '2':
        print('Estas son tus fichas: ')
        player_pawns.showPaws()
        showOptionsPlus()
    elif ans == '3':
        print(f'Puntos: {Board.score}')
        showOptionsPlus()
    elif ans == '4':
        Pawns.showPawnsPoints()
        showOptionsPlus()
    elif ans == '5':
        helpWithWords()
        showOptionsPlus()
    elif ans == '7':
        helpWithPosition()
        showOptionsPlus()
    elif ans == '8':
        legend()
        showOptionsPlus()
    elif ans == '0':
        endGame()
    else:
        showOptionsPlus()


def helpWithWords():
    """
    Muestra las posibles palabras que se pueden formar con las fichas disponibles del jugador
    y las que hay colocadas en el tablero.
    """
    print('Estas son las posibles palabras a formar: ')
    if board.totalWords == 0:
        Dictionary.showWords(player_pawns)
    else:
        board_letters = []
        for i in range(15):
            for j in range(15):
                if board.board[i][j] != ' ' and board.board[i][j] not in board_letters:
                    board_letters.append(board.board[i][j])
                    Dictionary.showWordsPlus(player_pawns, board.board[i][j])


def helpWithPosition():
    """
    Muestra las posibles colocaciones en el tablero de la palabra introducida.
    """
    print('Estas son las posibles colocaciones')
    board.showWordPlacement(player_pawns, new_word)


# Variables que serán globales
new_word = ''
newWordIsSubset = ''


def introduceNewWord():
    """
    Permite que el usuario introduzca una nueva palabra por consola
    y comprueba que existe en el diccionario, y que puede formarse con
    las fichas de que dispone el jugador y las ubicadas sobre el tablero.
    """
    print('Introduce tu palabra: ')
    global new_word, newWordIsSubset
    new_word = Word.readWord()
    new_word_ft = new_word.getFrequency()
    player_pawns_ft = player_pawns.getFrequency()
    isInDictionary = Dictionary.validateWord(new_word)

    if board.totalWords == 0:
        newWordIsSubset = FrequencyTable.isSubset(new_word_ft, player_pawns_ft)
    else:
        board_letters = []
        forceBreak = False

        for i in range(15):
            if forceBreak:
                break
            for j in range(15):
                if board.board[i][j] != ' ' and board.board[i][j] not in board_letters:
                    board_letters.append(board.board[i][j])
                    player_pawns_plus = player_pawns_ft
                    player_pawns_plus.update(board.board[i][j])
                    newWordIsSubset = FrequencyTable.isSubset(new_word_ft, player_pawns_plus)
                    player_pawns_plus.delete(board.board[i][j])

                    if newWordIsSubset:
                        forceBreak = True
                        break

    if not isInDictionary or not newWordIsSubset:
        if not newWordIsSubset:
            print('No puedes formar esa palabra con tus fichas')
        showOptions()
    else:
        showOptionsPlus()


def introduceCoordinatesAndDirection():
    """
    Permite al jugador introducir por consola la posición y orientación de una palabra.
    Comprueba si la palabra se puede colocar en dicha ubicación.
    """
    print('Introduce coordenada de la fila: ', end=' ')
    x = int(input())
    print('Introduce coordenada de la columna: ', end=' ')
    y = int(input())
    print('Introduce dirección: ', end=' ')
    direction = input().upper()

    if direction != 'V' and direction != 'H':
        print('Recuerda: solamente hay dos posibles direcciones para colocar las palabras: V (vertical) y H ('
              'horizontal)')
        showOptionsPlus()

    possible, message = board.isPossible(new_word, x, y, direction)
    if not possible:
        print(message)
        showOptionsPlus()
    else:
        needed_pawns = board.getPawns(new_word, x, y, direction)
        if FrequencyTable.isSubset(needed_pawns.getFrequency(), player_pawns.getFrequency()):
            board.placeWord(player_pawns, new_word, x, y, direction)
            board.showBoard()
        else:
            print('Las fichas de que dispones no son suficientes')
            showOptionsPlus()


def endGame():
    """
    Finaliza la partida.
    """
    print('Fin del juego')
    global end
    end = True

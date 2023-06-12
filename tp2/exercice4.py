# Fonction fournie ne pas modifier
clearConsole = lambda: print('\n' * 10)


def print_table(table):
    # Dimension 1 = ligne
    # Dimension 2 = colonne
    clearConsole()
    for i, row in enumerate(table):
        row_str = "{:>2}" * len(row)
        row_str = row_str.format(*row)
        print("{:^20}".format(row_str), '\n')

# ________________________________________________________________


# Partie 1
def init_maze(nb_row, nb_col, player_pos, end_pos, walls):
    # Génère un labyrinthe vide -> rempli de "_"
    maze = []
    for row in range(nb_row):
        maze_row = []
        for col in range(nb_col):
            maze_row.append('_')
        maze.append(maze_row)

    # Place le joueur "O" la sortie "X" les murs "W"
    maze[player_pos[0]][player_pos[1]] = 'O'
    maze[end_pos[0]][end_pos[1]] = 'X'

    for wall in walls:
        maze[wall[0]][wall[1]] = 'W'

    return maze



# Partie 2
def validate_move(maze, new_player_position):
    # Vérifie si la position est valide -> dans le labyrinthe et pas sur un mur
    result = False
    # Vérifie que la nouvelle position se trouve soit sur une case '_' ou 'X', qu'elle se trouve dans le labyrinthe,
    # et que le joueur n'utilise pas d'index négatif.
    if 4 > new_player_position[0] >= 0 and 7 > new_player_position[1] >= 0:
        new_position_char = maze[new_player_position[0]][new_player_position[1]]
        if new_position_char == '_' or new_position_char == 'X':
            result = True
    return result


# Partie 3
def move(key_pressed, maze, player_pos):
    # Crée le dictionnaire d'équivalence entre la touche appuyée et la direction ("up", "left", "down", "right")
    move_dic = {'w': 'up', 'a': 'left', 's': 'down', 'd': 'right'}

    # Vérifie si la touche appuyée est dans le dictionnaire
    if key_pressed in move_dic:
        move = move_dic[key_pressed]  # Récupère la direction du mouvement

        # Génère la position potentielle du joueur en fonction de la direction
        if move == 'up':
            new_player_pos = (player_pos[0] - 1, player_pos[1])
        elif move == 'down':
            new_player_pos = (player_pos[0] + 1, player_pos[1])
        elif move == 'left':
            new_player_pos = (player_pos[0], player_pos[1] - 1)
        elif move == 'right':
            new_player_pos = (player_pos[0], player_pos[1] + 1)

        if validate_move(maze, new_player_pos):
            # Change réellement la position du joueur
            maze[player_pos[0]][player_pos[1]] = '_'
            maze[new_player_pos[0]][new_player_pos[1]] = 'O'
            player_pos = new_player_pos

    return maze, player_pos


if __name__ == '__main__':
    nb_row = 4
    nb_col = 7
    player_pos = (0, 0)  # Défini la position ligne, colonne sur en haut à gauche
    end_pos = (3, 6)  # Défini la position ligne, colonne sur en bas à droite
    # Coordoné sous la forme (ligne, colone)
    walls = [[0, 1], [1, 1], [1, 2], [1, 3], [1, 5], [2, 1], [2, 5], [3, 3], [3, 5]]
    maze = init_maze(nb_row, nb_col, player_pos, end_pos, walls)

    print_table(maze)

    # Décommenter pour tester le code en Partie 2
    test_pos = [1, 0] # changer les valeurs pour tester tous les cas possibles
    valid = validate_move(maze, test_pos)
    print(valid)


    # Décommenter pour tester le code en Partie 3
    while player_pos != end_pos:
        key_pressed = input("mouvement : ")
        maze, player_pos = move(key_pressed, maze, player_pos)
        print_table(maze)
    
    print("Vous avez gagnez !")

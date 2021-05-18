

from typing import List

def print_matrice(matrice: List[List[int]]):
    for line in matrice:
        for column in line:
            print(column, end="\t")
        print('\n')


def kuhn(matrice_origin: List[List[int]]):
    matrice: List[List[int]] = []

    for line in matrice_origin:
        matrice.append(line[:])

    # Etape 0 #
    # On retranche les lignes
    print("Matrice originale :")
    print_matrice(matrice)

    for line in matrice:
        min_val = min(line)

        for i in range(len(line)):
            line[i] -= min_val

    # On retranche les colonnes
    for column in range(len(matrice)):
        col_values = [line[column] for line in matrice]

        min_val = min(col_values)
        for line in matrice:
            line[column] -= min_val

    print_matrice(matrice)

    zeros_marques = [-1]
    while -1 in zeros_marques:
        # Etapes 2
        zeros_marques = []
        colonnes_barres = []
        
        for line_index in range(len(matrice)):
            for column_index in range(len(matrice[line_index])):
                if matrice[line_index][column_index] == 0:
                    if column_index in zeros_marques:
                        continue
                    zeros_marques.append(column_index)

                    col_values = [line[column_index] for line in matrice]
                    for i in range(len(col_values)):
                        if col_values[i] == line_index and col_values[i] == 0:
                            colonnes_barres.append(column_index)
                            break                       

                    break
            
            if len(zeros_marques) != line_index + 1:
                zeros_marques.append(-1)
        
        print("zeros_marques", zeros_marques)
        print("colonnes_barres", colonnes_barres)

        # Bilan 0

        if not -1 in zeros_marques:
            break

        # Etape 3
        sous_tbl = []
        sous_indices = []
        for line_index in range(len(matrice)):
            if zeros_marques[line_index] == -1 or zeros_marques[line_index] in colonnes_barres:
                for column_index in range(len(matrice[line_index])):
                    if column_index not in colonnes_barres:
                        sous_tbl.append(matrice[line_index][column_index])
                        sous_indices.append((line_index, column_index))
        
        print("sous_tbl", sous_tbl)

        min_val = min(sous_tbl)
        for cell in sous_indices:
            matrice[cell[0]][cell[1]] -= min_val
        
        print_matrice(matrice)

        for line_index in range(len(matrice)):
            if zeros_marques[line_index] != -1 and zeros_marques[line_index] not in colonnes_barres:
                for column_index in range(len(matrice[line_index])):
                    if column_index in colonnes_barres:
                        matrice[line_index][column_index] += min_val
        
        print("\n====================================\n")
        print_matrice(matrice)
    
    print("Matrice finale :")
    print_matrice(matrice)
    print('zeros_marques', zeros_marques)
    res = 0
    for i in range(len(zeros_marques)):
        res += matrice_origin[i][zeros_marques[i]]

    return res            


if __name__ == "__main__":

    mat = [
        [17,15,9,5,12],
        [16, 16, 10, 5, 10],
        [12,15,14,11,5],
        [4,8,14,17,13],
        [13, 9, 8, 12, 17],
    ]

    print("Résultat", kuhn(mat))

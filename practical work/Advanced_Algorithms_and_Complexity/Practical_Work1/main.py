import time
import sys
import os

# Changer le répertoire courant vers celui où se trouve le script. 
# Cela évite les erreurs "file not found" lorsque vous lisez ou écrivez des fichiers.
os.chdir(os.path.dirname(__file__))

#############################################################################################################################
# QUESTION 1 – Lecture du fichier
# Écrire une fonction Python permettant de lire les valeurs entières du fichier valeurs_aleatoires.txt
# La lecture doit se faire à l’aide d’une liste, en convertissant chaque ligne en entier.
#############################################################################################################################

def read_file(file_name):
    # Ouvre le fichier en mode lecture 'r'
    file = open(file_name, 'r')
    values = []   # Liste qui va contenir les entiers du fichier
    for line in file:
        # Convertir chaque ligne en entier et l'ajouter à la liste
        values.append(int(line.strip()))
    file.close()  # Fermer le fichier après lecture
    return values    

#############################################################################################################################
# QUESTION 2 – Comptage des occurrences (Complexité O(n²))
# Écrire une fonction nombre_occurrences(values_list) utilisant :
# - une boucle imbriquée
# - un dictionnaire pour stocker les occurrences
#
# QUESTION 3 – Analyse algorithmique
# - Indiquer le nombre exact d’itérations
# - Déterminer la complexité temporelle en notation O.
# - Intégrer un chronomètre pour mesurer la durée d’exécution
#############################################################################################################################

def nombre_occurrences(values_list):
    iterations = 0
    start_time = time.time()
    occurrences = dict()
    remaining_time = 0

    for i in range(n):
        iterations += 1
        count = 0
        for j in range(n):
            iterations += 1
            if values_list[j] == values_list[i]:
                count += 1
            occurrences[values_list[i]] = count
        
        #               100% --> n
        # elapsed_percentage --> i+1 => elapsed_percentage  = (i + 1) * 100 / n  
        elapsed_percentage   = (i + 1) * 100 / n
        remaining_percentage = 100 - elapsed_percentage 

        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_percentage  > 0:
            #    elapsed_time --> elapsed_percentage 
            #  remaining_time --> remaining_percentage => remaining_time = remaining_percentage * elapsed_time / elapsed_percentage 
            remaining_time = remaining_percentage * elapsed_time / elapsed_percentage 
        
        # Affiche la progression sur une seule ligne en écrasant l'affichage précédent.
        # \r ramène le curseur au début de la ligne, sys.stdout.write écrit le texte sans retour à la ligne,
        # et le formatage affiche le pourcentage, le temps écoulé et le temps restant estimé.
        sys.stdout.write(f"\rProgress: {elapsed_percentage :.2f}%, Elapsed Time: {elapsed_time:.2f}s, RemainingTime: {remaining_time:.2f}s")

        # Force l'affichage immédiat du texte (sinon Python peut attendre avant d'afficher).
        sys.stdout.flush()  

    end_time = time.time()
    print(f"\n⏱ Durée totale du comptage : {end_time - start_time:.5f} secondes")
    print(f"Nombre total d’itérations : {iterations}")
    return occurrences
# fin nombre_occurrences

# QUESTION 4 – Amélioration du calcul des occurrences (Complexité O(n))
# Écrire une fonction nombre_occurrences_ameliore(values_list)
# Objectif : réduire la complexité de O(n²) → O(n)
#############################################################################################################################

def nombre_occurrences_ameliore(values_list):
    """
    Counts occurrences of each value in O(n) time.
    Uses a single loop and a dictionary.
    """

    occurrences = {}  # Dictionary to store counts

    # Single loop → O(n)
    for value in values_list:
        if value in occurrences:
            occurrences[value] += 1
        else:
            occurrences[value] = 1

    return occurrences

# QUESTION 5 – Tri par sélection (Selection Sort)
# Écrire une fonction selection_sort() qui :
# - trie les éléments en ordre croissant
# - indique le nombre exact d’itérations
# - affiche la complexité 
# - intègre un chronomètre
#############################################################################################################################

# def selection_sort():

import time

def selection_sort(values_list):
    """
    Sorts the list in ascending order using Selection Sort.
    Also displays:
    - exact number of iterations
    - time complexity
    - execution time (timer)
    """

    n = len(values_list)
    iterations = 0  # Count comparisons

    start_time = time.time()  # Start chronometer

    # Selection Sort algorithm
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            iterations += 1  # Count each comparison
            if values_list[j] < values_list[min_index]:
                min_index = j

        # Swap the smallest found value with the current index
        values_list[i], values_list[min_index] = values_list[min_index], values_list[i]

    end_time = time.time()  # End chronometer
    execution_time = end_time - start_time

    # Displaying results
    print("Sorted list:", values_list)
    print("Number of iterations:", iterations)
    print("Time complexity: O(n^2)")
    print(f"Execution time: {execution_time:.6f} seconds")

    return values_list


# QUESTION 6 – Tri par fusion (Merge Sort)
# Écrire une fonction merge_sort(tab) qui :
# - trie les éléments en ordre croissant
# - compte le nombre d’itérations
# - affiche la complexité : O(n log n)
# - intègre un chronomètre
#############################################################################################################################

# def merge_sort():


import time

# Global counter for iterations
merge_iterations = 0

def merge_sort(tab):
    global merge_iterations
    merge_iterations = 0  # reset counter
    
    print("Starting Merge Sort...")
    start_time = time.time()
    
    result = merge_sort_recursive(tab)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print("\n--- MERGE SORT RESULTS ---")
    print("Sorted list :", result)
    print("Iterations  :", merge_iterations)
    print("Complexity  : O(n log n)")
    print(f"Time taken  : {execution_time:.6f} seconds")
    
    return result


def merge_sort_recursive(tab):
    global merge_iterations
    merge_iterations += 1  # counting each recursive call
    
    if len(tab) <= 1:
        return tab
    
    mid = len(tab) // 2
    left = merge_sort_recursive(tab[:mid])
    right = merge_sort_recursive(tab[mid:])
    
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    
    # merge two sorted lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# Example test
# merge_sort([38, 27, 43, 3, 9, 82, 10])


# QUESTION 7 – Sauvegarde du tableau trié
# Écrire une fonction write_to_file(tab) qui enregistre les valeurs triées dans 
# un fichier nommé valeurs_aleatoires_tries.txt
#############################################################################################################################

# def write_to_file():

def write_to_file(tab):
    """
    Saves the sorted list 'tab' into a text file.
    Each value is written on the same line, separated by spaces.
    """
    
    filename = "valeurs_aleatoires_tries.txt"
    
    try:
        with open(filename, "w") as file:
            # Write values as a single line
            file.write(" ".join(str(x) for x in tab))
        
        print(f"✔️ File '{filename}' successfully created!")
    
    except Exception as e:
        print("❌ Error while writing to file:", e)

#############################################################################################################################
# Début du script principal
#############################################################################################################################

# 1. Lecture du fichier
valeurs_aleatoires_list = read_file('valeurs_aleatoires.txt')
list_length = len(valeurs_aleatoires_list)
n = len(valeurs_aleatoires_list) # n est utilisé dans nombre_occurrences

print('Valeurs lues :', valeurs_aleatoires_list[:10], '...')
print('Longueur de la liste (n) :', n)

# 2. & 3. Comptage des occurrences (O(n²))
occurrences_on2 = nombre_occurrences(valeurs_aleatoires_list)
# print("Occurrences (O(n²)) :", occurrences_on2)

# 4. Comptage des occurrences amélioré (O(n))
# occurrences_on = nombre_occurrences_ameliore(valeurs_aleatoires_list)
# print("Occurrences (O(n)) :", occurrences_on)

# 5. Tri par sélection (Selection Sort)
# sorted_selection = selection_sort()

# 6. Tri par fusion (Merge Sort)
# sorted_merge = merge_sort()

# 7. Sauvegarde du tableau trié
# write_to_file()






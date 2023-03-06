#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
create_training_table

Script pour récupérer les données d'entraînement et créer un dataframe pandas
concatenant toutes les données par semaine. Ce dataframe est ensuite transformé
en tableau et exporté au format pdf pour plus de lisibilité.

Auteur : Corentin MICHEL
Date de création : 18/01/2023
Dernière modification : 06/03/2023
"""
import datetime
import os
import matplotlib.pyplot as plt

import pandas
import numpy
# import numpy

import frac1
import frac2
import footing
import end

WORKOUT_DATES = pandas.date_range("2023/01/01", "2023/12/31", freq='w-mon')
MIN_LENGTH = min([
    len(dataframe.columns) - 1
    for dataframe in [frac1.frac1, frac2.frac2, footing.footing, end.end]
])

fig, ax = plt.subplots()


def update_header():
    """
    Update the date of last modification in the header of the current python file
    """
    # Récupère la date de dernière modification du fichier
    file_path = os.path.realpath(__file__)
    last_modified = os.path.getmtime(file_path)

    mod_date = datetime.datetime.fromtimestamp(last_modified).strftime(
        "%d/%m/%Y")

    with open(file_path, "r+") as f:
        lines = f.readlines()
        # change la date de dernière modification si elle est différente de la
        # date actuelle.

        for i, line in enumerate(lines):
            if line.startswith("Dernière modification :"):
                if line[i] != f"Dernière modification : {mod_date}\n":
                    lines[i] = f"Dernière modification : {mod_date}\n"

                    break
        # Remonte au début du fichier et écrit les lignes mises à jour
        f.seek(0)
        f.writelines(lines)


def create_training_table():
    """
    fonction de crétation de tableau d'entrainement par semaine.
    """
    mod_time = os.path.getmtime('test.py')
    mod_date = datetime.datetime.fromtimestamp(mod_time).strftime('%d/%m/%Y')
    print(f"# Dernière modification : {mod_date}\n")
    # Créer une liste de toutes les valeurs pour chaque colonne
    dates = pandas.to_datetime(WORKOUT_DATES).strftime('%d.%m.%Y')[:MIN_LENGTH]
    frac1_descriptions = [
        frac1.frac1[[str(i + 1)]].values[0] for i in range(MIN_LENGTH)
    ]
    frac1_values = [[
        float(frac1.frac1[[str(i + 1)]].values[1]),
        float(frac1.frac1[[str(i + 1)]].values[2]),
        float(frac1.frac1[[str(i + 1)]].values[3])
    ] for i in range(MIN_LENGTH)]
    frac2_descriptions = [
        frac2.frac2[[str(i + 1)]].values[0] for i in range(MIN_LENGTH)
    ]
    frac2_values = [[
        float(frac2.frac2[[str(i + 1)]].values[1]),
        float(frac2.frac2[[str(i + 1)]].values[2]),
        float(frac2.frac2[[str(i + 1)]].values[3])
    ] for i in range(MIN_LENGTH)]
    footing_descriptions = [
        footing.footing[[str(i + 1)]].values[0] for i in range(MIN_LENGTH)
    ]
    footing_values = [[
        float(footing.footing[[str(i + 1)]].values[1]),
        float(footing.footing[[str(i + 1)]].values[2]),
        float(footing.footing[[str(i + 1)]].values[3])
    ] for i in range(MIN_LENGTH)]
    end_descriptions = [
        end.end[[str(i + 1)]].values[0] for i in range(MIN_LENGTH)
    ]
    end_values = [[
        float(end.end[[str(i + 1)]].values[1]),
        float(end.end[[str(i + 1)]].values[2]),
        float(end.end[[str(i + 1)]].values[3])
    ] for i in range(MIN_LENGTH)]

    # Créer un dictionnaire de données pour le DataFrame
    data = {
        'date': dates,
        'description_frac1': frac1_descriptions,
        'frac1_distance': [x[0] for x in frac1_values],
        'frac1_freq': [x[1] for x in frac1_values],
        'frac1_time': [x[2] for x in frac1_values],
        'description_frac2': frac2_descriptions,
        'frac2_distance': [x[0] for x in frac2_values],
        'frac2_time': [x[1] for x in frac2_values],
        'frac2_load': [x[2] for x in frac2_values],
        'description_footing': footing_descriptions,
        'footing_distance': [x[0] for x in footing_values],
        'footing_freq': [x[1] for x in footing_values],
        'footing_time': [x[2] for x in footing_values],
        'description_end': end_descriptions,
        'end_distance': [x[0] for x in end_values],
        'end_freq': [x[1] for x in end_values],
        'end_time': [x[2] for x in end_values]
    }

    # Créer le DataFrame à partir du dictionnaire de données
    dataframe = pandas.DataFrame(data)

    # Transformer les listes de chaînes de caractères en une chaîne de
    # caractères simple
    # dataframe['description_end'] = dataframe['description_end'].explode().str.join('')
    dataframe = dataframe.applymap(lambda x: ' '.join(x)
                                   if isinstance(x, numpy.ndarray) else x)
    dataframe.style.set_properties(subset=pandas.IndexSlice[[0], :],
                                   **{'font-weight': 'bold'})
    table = ax.table(cellText=dataframe.values,
                     colLabels=dataframe.columns,
                     loc='center')

    print(dataframe)
    # Ajuster la largeur des colonnes pour diviser le texte sur plusieurs lignes
    table.auto_set_column_width(col=list(range(len(dataframe.columns))))
    ax.axis('off')
    plt.savefig('training_table.pdf', format='pdf', bbox_inches='tight')


# Programme principal

if __name__ == '__main__':
    # Instructions à exécuter si le script est exécuté directement
    update_header()
    create_training_table()

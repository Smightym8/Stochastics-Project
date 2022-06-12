import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def create_bar_plot(dataset, plots_dir):
    # Species per island
    species_per_island_pivot = dataset.pivot_table(index=['island', 'species'], aggfunc={'species': np.size},
                                                   fill_value=0)
    print(species_per_island_pivot)

    labels = ['Biscoe', 'Dream', 'Torgersen']
    adelie_data = [44, 55, 47]
    gentoo_data = [119, 0, 0]
    chinstrap_data = [0, 68, 0]

    x = np.arange(len(labels))
    width = 0.25

    races_per_island_bar, races_per_island_bar_ax = plt.subplots()
    rects1 = races_per_island_bar_ax.bar(x - width, adelie_data, width, label='Adelie')
    rects2 = races_per_island_bar_ax.bar(x + width / 60, gentoo_data, width, label='Gentoo')
    rects3 = races_per_island_bar_ax.bar(x + width, chinstrap_data, width, label='Chinstrap')

    races_per_island_bar_ax.set_ylabel('Amount')
    races_per_island_bar_ax.set_title('Races by island')
    races_per_island_bar_ax.set_xticks(x, labels)
    races_per_island_bar_ax.legend()

    races_per_island_bar_ax.bar_label(rects1, padding=3)
    races_per_island_bar_ax.bar_label(rects2, padding=3)
    races_per_island_bar_ax.bar_label(rects3, padding=3)

    races_per_island_bar.tight_layout()
    races_per_island_bar.savefig(plots_dir + "/races_per_island_bar.jpg", dpi=races_per_island_bar.dpi)

    # Male female per race
    sex_per_race_pivot = dataset.pivot_table(index=['species', 'sex'], aggfunc={'sex': np.size},
                                                   fill_value=0)

    print(sex_per_race_pivot)

    labels = ['Adelie', 'Chinstrap', 'Gentoo']
    female_data = [73, 34, 58]
    male_data = [73, 34, 61]

    x = np.arange(len(labels))
    width = 0.25

    sex_per_race_bar, sex_per_race_bar_ax = plt.subplots()
    rects1 = sex_per_race_bar_ax.bar(x - width / 2, female_data, width, label='Female')
    rects2 = sex_per_race_bar_ax.bar(x + width / 2, male_data, width, label='Male')

    sex_per_race_bar_ax.set_ylabel('Amount')
    sex_per_race_bar_ax.set_title('Sex by race')
    sex_per_race_bar_ax.set_xticks(x, labels)
    sex_per_race_bar_ax.legend()

    sex_per_race_bar_ax.bar_label(rects1, padding=3)
    sex_per_race_bar_ax.bar_label(rects2, padding=3)

    sex_per_race_bar.tight_layout()
    sex_per_race_bar.savefig(plots_dir + "/sex_per_race_bar.jpg", dpi=sex_per_race_bar.dpi)

    # Male female per island
    sex_per_island_pivot = dataset.pivot_table(index=['island', 'sex'], aggfunc={'sex': np.size},
                                             fill_value=0)

    print(sex_per_island_pivot)

    labels = ['Biscoe', 'Dream', 'Torgersen']
    female_data = [80, 61, 24]
    male_data = [83, 62, 23]

    x = np.arange(len(labels))
    width = 0.25

    sex_per_island_bar, sex_per_island_bar_ax = plt.subplots()
    rects1 = sex_per_island_bar_ax.bar(x - width / 2, female_data, width, label='Female')
    rects2 = sex_per_island_bar_ax.bar(x + width / 2, male_data, width, label='Male')

    sex_per_island_bar_ax.set_ylabel('Amount')
    sex_per_island_bar_ax.set_title('Sex by island')
    sex_per_island_bar_ax.set_xticks(x, labels)
    sex_per_island_bar_ax.legend()

    sex_per_island_bar_ax.bar_label(rects1, padding=3)
    sex_per_island_bar_ax.bar_label(rects2, padding=3)

    sex_per_island_bar.tight_layout()
    sex_per_island_bar.savefig(plots_dir + "/sex_per_island_bar.jpg", dpi=sex_per_island_bar.dpi)
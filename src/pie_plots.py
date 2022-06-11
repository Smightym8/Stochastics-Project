import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def generate_pie_plots(dataset, plots_dir):
    # Pie Chart of species, island and sex
    # Species Pie
    species_grouped_pivot = dataset.pivot_table(index=['species'], aggfunc=np.size)
    species_grouped_df = pd.DataFrame(species_grouped_pivot)
    species_labels = ['Adelie', 'Chinstrap', 'Gentoo']

    species_pie, species_pie_ax = plt.subplots()
    species_pie_ax.set_title("Species")
    species_pie_ax.pie(species_grouped_df.island, labels=species_labels, autopct='%1.1f%%', startangle=90)
    species_pie.savefig(plots_dir + "/species_pie.jpg", dpi=species_pie.dpi)

    # Island Pie
    island_grouped_pivot = dataset.pivot_table(index=['island'], aggfunc=np.size)
    island_grouped_df = pd.DataFrame(island_grouped_pivot)
    island_labels = ['Biscoe', 'Dream', 'Torgersen']

    island_pie, island_pie_ax = plt.subplots()
    island_pie_ax.set_title("Island")
    island_pie_ax.pie(island_grouped_df.species, labels=island_labels, autopct='%1.1f%%', startangle=90)
    island_pie.savefig(plots_dir + "/island_pie.jpg", dpi=island_pie.dpi)

    # Sex Pie
    sex_grouped_pivot = dataset.pivot_table(index=['sex'], aggfunc=np.size)
    sex_grouped_df = pd.DataFrame(sex_grouped_pivot)
    sex_labels = ['Female', 'Male']

    sex_pie, sex_pie_ax = plt.subplots()
    sex_pie_ax.set_title("Sex")
    sex_pie_ax.pie(sex_grouped_df.species, labels=sex_labels, autopct='%1.1f%%', startangle=90)
    sex_pie.savefig(plots_dir + "/sex_pie.jpg", dpi=island_pie.dpi)

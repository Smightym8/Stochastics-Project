import pandas as pd
import matplotlib.pyplot as plt

def generate_boxplots(dataset: pd.DataFrame, plots_dir: str):
    dataset_male = dataset.loc[dataset['sex'] == 'male']
    dataset_female = dataset.loc[dataset['sex'] == 'female']

    # Boxplot for bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g
    # Bill length boxplot
    bill_length_boxplot, bill_length_boxplot_ax = plt.subplots()
    bill_length_boxplot_ax.set_title('Bill length (mm)')
    bill_length_boxplot_ax.boxplot(dataset.bill_length_mm, vert=False)
    bill_length_boxplot.savefig(plots_dir + "/bill_length_mm_boxplot.jpg", dpi=bill_length_boxplot.dpi)

    # Bill depth boxplot
    bill_depth_boxplot, bill_depth_boxplot_ax = plt.subplots()
    bill_depth_boxplot_ax.set_title('Bill depth (mm)')
    bill_depth_boxplot_ax.boxplot(dataset.bill_depth_mm, vert=False)
    bill_depth_boxplot.savefig(plots_dir + "/bill_depth_mm_boxplot.jpg", dpi=bill_depth_boxplot.dpi)

    # Flipper length boxplot
    flipper_length_boxplot, flipper_length_boxplot_ax = plt.subplots()
    flipper_length_boxplot_ax.set_title('Flipper length (mm)')
    flipper_length_boxplot_ax.boxplot(dataset.flipper_length_mm, vert=False)
    flipper_length_boxplot.savefig(plots_dir + "/flipper_length_mm_boxplot.jpg", dpi=flipper_length_boxplot.dpi)

    # Body mass boxplot
    body_mass_boxplot, body_mass_boxplot_ax = plt.subplots()
    body_mass_boxplot_ax.set_title('Body mass (g)')
    body_mass_boxplot_ax.boxplot(dataset.body_mass_g, vert=False)
    body_mass_boxplot.savefig(plots_dir + "/body_mass_g.jpg", dpi=body_mass_boxplot.dpi)

    # Bill length male boxplot
    bill_length_male_boxplot, bill_length_male_boxplot_ax = plt.subplots()
    bill_length_male_boxplot_ax.set_title('Bill length male (mm)')
    bill_length_male_boxplot_ax.boxplot(dataset_male.bill_length_mm, vert=False)
    bill_length_male_boxplot.savefig(plots_dir + "/bill_length_male_boxplot.jpg", dpi=bill_length_male_boxplot.dpi)

    # Bill length female boxplot
    bill_length_female_boxplot, bill_length_female_boxplot_ax = plt.subplots()
    bill_length_female_boxplot_ax.set_title('Bill length female (mm)')
    bill_length_female_boxplot_ax.boxplot(dataset_female.bill_length_mm, vert=False)
    bill_length_female_boxplot.savefig(plots_dir + "/bill_length_female_boxplot.jpg",
                                       dpi=bill_length_female_boxplot.dpi)

    # Bill depth male boxplot
    bill_depth_male_boxplot, bill_depth_male_boxplot_ax = plt.subplots()
    bill_depth_male_boxplot_ax.set_title('Bill depth male (mm)')
    bill_depth_male_boxplot_ax.boxplot(dataset_male.bill_depth_mm, vert=False)
    bill_depth_male_boxplot.savefig(plots_dir + "/bill_depth_male_boxplot.jpg", dpi=bill_depth_male_boxplot.dpi)

    # Bill depth female boxplot
    bill_depth_female_boxplot, bill_depth_female_boxplot_ax = plt.subplots()
    bill_depth_female_boxplot_ax.set_title('Bill depth female (mm)')
    bill_depth_female_boxplot_ax.boxplot(dataset_female.bill_depth_mm, vert=False)
    bill_depth_female_boxplot.savefig(plots_dir + "/bill_depth_female_boxplot.jpg", dpi=bill_depth_female_boxplot.dpi)

    # Flipper length male boxplot
    flipper_length_male_boxplot, flipper_length_male_boxplot_ax = plt.subplots()
    flipper_length_male_boxplot_ax.set_title('Flipper length male (mm)')
    flipper_length_male_boxplot_ax.boxplot(dataset_male.flipper_length_mm, vert=False)
    flipper_length_male_boxplot.savefig(plots_dir + "/flipper_length_male_boxplot.jpg",
                                        dpi=flipper_length_male_boxplot.dpi)

    # Flipper length female boxplot
    flipper_length_female_boxplot, flipper_length_female_boxplot_ax = plt.subplots()
    flipper_length_female_boxplot_ax.set_title('Flipper length female (mm)')
    flipper_length_female_boxplot_ax.boxplot(dataset_female.flipper_length_mm, vert=False)
    flipper_length_female_boxplot.savefig(plots_dir + "/flipper_length_female_boxplot.jpg",
                                          dpi=flipper_length_female_boxplot.dpi)

    # Body mass male boxplot
    body_mass_male_boxplot, body_mass_male_boxplot_ax = plt.subplots()
    body_mass_male_boxplot_ax.set_title('Body mass male (g)')
    body_mass_male_boxplot_ax.boxplot(dataset_male.body_mass_g, vert=False)
    body_mass_male_boxplot.savefig(plots_dir + "/body_mass_male_boxplot.jpg", dpi=body_mass_male_boxplot.dpi)

    # Body mass female boxplot
    body_mass_female_boxplot, body_mass_female_boxplot_ax = plt.subplots()
    body_mass_female_boxplot_ax.set_title('Body mass female (g)')
    body_mass_female_boxplot_ax.boxplot(dataset_female.body_mass_g, vert=False)
    body_mass_female_boxplot.savefig(plots_dir + "/body_mass_female_boxplot.jpg", dpi=body_mass_female_boxplot.dpi)
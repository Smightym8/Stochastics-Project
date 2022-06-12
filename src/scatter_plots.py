import matplotlib.pyplot as plt


# TODO: Colorize by species
def generate_scatter_plots(dataset, plots_dir):
    # Scatter plots
    # Sex and bill lengths
    sex_bill_length_correlation, sex_bill_length_correlation_ax = plt.subplots()
    sex_bill_length_correlation_ax.scatter(x=dataset.sex, y=dataset.bill_length_mm)
    sex_bill_length_correlation_ax.set_title('Correlation of Sex and Bill length (mm)')
    sex_bill_length_correlation_ax.set_xlabel('Sex')
    sex_bill_length_correlation_ax.set_ylabel('Bill length (mm)')
    sex_bill_length_correlation.savefig(plots_dir + "/sex_bill_length_correlation.jpg",
                                        dpi=sex_bill_length_correlation.dpi)

    # Sex and bill depths
    sex_bill_depth_correlation, sex_bill_depth_correlation_ax = plt.subplots()
    sex_bill_depth_correlation_ax.scatter(x=dataset.sex, y=dataset.bill_depth_mm)
    sex_bill_depth_correlation_ax.set_title('Correlation of Sex and Bill depth (mm)')
    sex_bill_depth_correlation_ax.set_xlabel('Sex')
    sex_bill_depth_correlation_ax.set_ylabel('Bill depth (mm)')
    sex_bill_depth_correlation.savefig(plots_dir + "/sex_bill_depth_correlation.jpg",
                                       dpi=sex_bill_depth_correlation.dpi)

    # Sex and flipper length
    sex_flipper_length_correlation, sex_flipper_length_correlation_ax = plt.subplots()
    sex_flipper_length_correlation_ax.scatter(x=dataset.sex, y=dataset.flipper_length_mm)
    sex_flipper_length_correlation_ax.set_title('Correlation of Sex and Flipper length (mm)')
    sex_flipper_length_correlation_ax.set_xlabel('Sex')
    sex_flipper_length_correlation_ax.set_ylabel('Flipper length (mm)')
    sex_flipper_length_correlation.savefig(plots_dir + "/sex_flipper_length_correlation.jpg",
                                           dpi=sex_flipper_length_correlation.dpi)

    # Sex and body mass
    sex_body_mass_correlation, sex_body_mass_correlation_ax = plt.subplots()
    sex_body_mass_correlation_ax.scatter(x=dataset.sex, y=dataset.body_mass_g)
    sex_body_mass_correlation_ax.set_title('Correlation of Sex and Body mass (g)')
    sex_body_mass_correlation_ax.set_xlabel('Sex')
    sex_body_mass_correlation_ax.set_ylabel('Body mass (g)')
    sex_body_mass_correlation.savefig(plots_dir + "/sex_body_mass_correlation.jpg",
                                      dpi=sex_body_mass_correlation.dpi)

    # Bill length and Bill depth correlation
    bill_length_depth_correlation, bill_length_depth_correlation_ax = plt.subplots()
    bill_length_depth_correlation_ax.scatter(x=dataset.bill_length_mm, y=dataset.bill_depth_mm)
    bill_length_depth_correlation_ax.set_title('Correlation of Bill length (mm) and Bill depth (mm)')
    bill_length_depth_correlation_ax.set_xlabel('Bill length (mm)')
    bill_length_depth_correlation_ax.set_ylabel('Bill depth (mm)')
    bill_length_depth_correlation.savefig(plots_dir + "/bill_length_depth_correlation.jpg",
                                          dpi=bill_length_depth_correlation.dpi)

    # Bill length and flipper length correlation
    bill_length_flipper_length_correlation, bill_length_flipper_length_correlation_ax = plt.subplots()
    bill_length_flipper_length_correlation_ax.scatter(x=dataset.bill_length_mm, y=dataset.flipper_length_mm)
    bill_length_flipper_length_correlation_ax.set_title('Correlation of Bill length (mm) and Flippers length (mm)')
    bill_length_flipper_length_correlation_ax.set_xlabel('Bill length (mm)')
    bill_length_flipper_length_correlation_ax.set_ylabel('Flipper length (mm)')
    bill_length_flipper_length_correlation.savefig(plots_dir + "/bill_length_flipper_length_correlation.jpg",
                                                   dpi=bill_length_flipper_length_correlation.dpi)

    # Bill length and body mass correlation
    bill_length_body_mass_correlation, bill_length_body_mass_correlation_ax = plt.subplots()
    bill_length_body_mass_correlation_ax.scatter(x=dataset.bill_length_mm, y=dataset.body_mass_g)
    bill_length_body_mass_correlation_ax.set_title('Correlation of Bill length (mm) and Body mass (g)')
    bill_length_body_mass_correlation_ax.set_xlabel('Bill length (mm)')
    bill_length_body_mass_correlation_ax.set_ylabel('Body mass (g)')
    bill_length_body_mass_correlation.savefig(plots_dir + "/bill_length_body_mass_correlation.jpg",
                                              dpi=bill_length_body_mass_correlation.dpi)

    # Bill depth and flipper length correlation
    bill_depth_flipper_length_correlation, bill_depth_flipper_length_correlation_ax = plt.subplots()
    bill_depth_flipper_length_correlation_ax.scatter(x=dataset.bill_depth_mm, y=dataset.flipper_length_mm)
    bill_depth_flipper_length_correlation_ax.set_title('Correlation of Bill depth (mm) and Flipper length (mm)')
    bill_depth_flipper_length_correlation_ax.set_xlabel('Bill depth (mm)')
    bill_depth_flipper_length_correlation_ax.set_ylabel('Flipper length (mm)')
    bill_depth_flipper_length_correlation.savefig(plots_dir + "/bill_depth_flipper_length_correlation.jpg",
                                                  dpi=bill_depth_flipper_length_correlation.dpi)

    # Bill depth and body mass correlation
    bill_depth_body_mass_correlation, bill_depth_body_mass_correlation_ax = plt.subplots()
    bill_depth_body_mass_correlation_ax.scatter(x=dataset.bill_depth_mm, y=dataset.body_mass_g)
    bill_depth_body_mass_correlation_ax.set_title('Correlation of Bill depth (mm) and Body mass (g)')
    bill_depth_body_mass_correlation_ax.set_xlabel('Bill depth (mm)')
    bill_depth_body_mass_correlation_ax.set_ylabel('Body mass (g)')
    bill_depth_body_mass_correlation.savefig(plots_dir + "/bill_depth_body_mass_correlation.jpg",
                                             dpi=bill_depth_body_mass_correlation.dpi)

    # Flipper length and body mass correlation
    flipper_length_body_mass_correlation, flipper_length_body_mass_correlation_ax = plt.subplots()
    flipper_length_body_mass_correlation_ax.scatter(x=dataset.flipper_length_mm, y=dataset.body_mass_g)
    flipper_length_body_mass_correlation_ax.set_title('Correlation of Flipper length (mm) and Body mass (g)')
    flipper_length_body_mass_correlation_ax.set_xlabel('Flipper length (mm)')
    flipper_length_body_mass_correlation_ax.set_ylabel('Body mass (g)')
    flipper_length_body_mass_correlation.savefig(plots_dir + "/flipper_length_body_mass_correlation.jpg",
                                                 dpi=flipper_length_body_mass_correlation.dpi)

    # Species and bill length
    species_bill_length_correlation, species_bill_length_correlation_ax = plt.subplots()
    species_bill_length_correlation_ax.scatter(x=dataset.species, y=dataset.bill_length_mm)
    species_bill_length_correlation_ax.set_title('Correlation of Species and Bill length (mm)')
    species_bill_length_correlation_ax.set_xlabel('Species')
    species_bill_length_correlation_ax.set_ylabel('Bill length (mm)')
    species_bill_length_correlation.savefig(plots_dir + "/species_bill_length_correlation.jpg",
                                            dpi=species_bill_length_correlation.dpi)

    # Species and bill depth
    species_bill_depth_correlation, species_bill_depth_correlation_ax = plt.subplots()
    species_bill_depth_correlation_ax.scatter(x=dataset.species, y=dataset.bill_depth_mm)
    species_bill_depth_correlation_ax.set_title('Correlation of Species and Bill depth (mm)')
    species_bill_depth_correlation_ax.set_xlabel('Species')
    species_bill_depth_correlation_ax.set_ylabel('Bill depth (mm)')
    species_bill_depth_correlation.savefig(plots_dir + "/species_bill_depth_correlation.jpg",
                                           dpi=species_bill_depth_correlation.dpi)

    # Species and flipper length
    species_flipper_length_correlation, species_flipper_length_correlation_ax = plt.subplots()
    species_flipper_length_correlation_ax.scatter(x=dataset.species, y=dataset.flipper_length_mm)
    species_flipper_length_correlation_ax.set_title('Correlation of Species and Flipper length (mm)')
    species_flipper_length_correlation_ax.set_xlabel('Species')
    species_flipper_length_correlation_ax.set_ylabel('Flipper length (mm)')
    species_flipper_length_correlation.savefig(plots_dir + "/species_flipper_length_correlation.jpg",
                                               dpi=species_flipper_length_correlation.dpi)

    # Species and body mass
    species_body_mass_correlation, species_body_mass_correlation_ax = plt.subplots()
    species_body_mass_correlation_ax.scatter(x=dataset.species, y=dataset.body_mass_g)
    species_body_mass_correlation_ax.set_title('Correlation of Species and Body mass (g)')
    species_body_mass_correlation_ax.set_xlabel('Species')
    species_body_mass_correlation_ax.set_ylabel('Body mass (g)')
    species_body_mass_correlation.savefig(plots_dir + "/species_body_mass_correlation.jpg",
                                          dpi=species_body_mass_correlation.dpi)

    # Island and bill length
    island_bill_length_correlation, island_bill_length_correlation_ax = plt.subplots()
    island_bill_length_correlation_ax.scatter(x=dataset.island, y=dataset.bill_length_mm)
    island_bill_length_correlation_ax.set_title('Correlation of Island and Bill length (mm)')
    island_bill_length_correlation_ax.set_xlabel('Island')
    island_bill_length_correlation_ax.set_ylabel('Bill length (mm)')
    island_bill_length_correlation.savefig(plots_dir + "/island_bill_length_correlation.jpg",
                                           dpi=island_bill_length_correlation.dpi)

    # Island and bill depth
    island_bill_depth_correlation, island_bill_depth_correlation_ax = plt.subplots()
    island_bill_depth_correlation_ax.scatter(x=dataset.island, y=dataset.bill_depth_mm)
    island_bill_depth_correlation_ax.set_title('Correlation of Island and Bill depth (mm)')
    island_bill_depth_correlation_ax.set_xlabel('Island')
    island_bill_depth_correlation_ax.set_ylabel('Bill depth (mm)')
    island_bill_depth_correlation.savefig(plots_dir + "/island_bill_depth_correlation.jpg",
                                          dpi=island_bill_depth_correlation.dpi)

    # Island and flipper length
    island_flipper_length_correlation, island_flipper_length_correlation_ax = plt.subplots()
    island_flipper_length_correlation_ax.scatter(x=dataset.island, y=dataset.flipper_length_mm)
    island_flipper_length_correlation_ax.set_title('Correlation of Island and Flipper length (mm)')
    island_flipper_length_correlation_ax.set_xlabel('Island')
    island_flipper_length_correlation_ax.set_ylabel('Flipper length (mm)')
    island_flipper_length_correlation.savefig(plots_dir + "/island_flipper_length_correlation.jpg",
                                              dpi=island_flipper_length_correlation.dpi)

    # Island and body mass
    island_body_mass_correlation, island_body_mass_correlation_ax = plt.subplots()
    island_body_mass_correlation_ax.scatter(x=dataset.island, y=dataset.body_mass_g)
    island_body_mass_correlation_ax.set_title('Correlation of Island and Body mass (g)')
    island_body_mass_correlation_ax.set_xlabel('Island')
    island_body_mass_correlation_ax.set_ylabel('Body mass (g)')
    island_body_mass_correlation.savefig(plots_dir + "/island_body_mass_correlation.jpg",
                                         dpi=island_body_mass_correlation.dpi)

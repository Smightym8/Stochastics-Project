import numpy as np


def calculate_statistical_values(dataset):
    # Statistical values (mean, median, etc.)
    # Bill length
    bill_length_avg = np.average(dataset.bill_length_mm)
    bill_length_median = np.median(dataset.bill_length_mm)
    bill_length_std = np.std(dataset.bill_length_mm)
    bill_length_var = np.var(dataset.bill_length_mm)

    print("Average bill length: " + str(bill_length_avg) + "mm")
    print("Median bill length: " + str(bill_length_median) + "mm")
    print("Standard Deviation bill length: " + str(bill_length_std) + "mm")
    print("Variance bill length: " + str(bill_length_var) + "mm²\n")

    # Bill depth
    bill_depth_avg = np.average(dataset.bill_depth_mm)
    bill_depth_median = np.median(dataset.bill_depth_mm)
    bill_depth_std = np.std(dataset.bill_depth_mm)
    bill_depth_var = np.var(dataset.bill_depth_mm)

    print("Average bill depth: " + str(bill_depth_avg) + "mm")
    print("Median bill depth: " + str(bill_depth_median) + "mm")
    print("Standard Deviation bill depth: " + str(bill_depth_std) + "mm")
    print("Variance bill depth: " + str(bill_depth_var) + "mm²\n")

    # Flipper length
    flipper_length_avg = np.average(dataset.flipper_length_mm)
    flipper_length_median = np.median(dataset.flipper_length_mm)
    flipper_length_std = np.std(dataset.flipper_length_mm)
    flipper_length_var = np.var(dataset.flipper_length_mm)

    print("Average flipper length: " + str(flipper_length_avg) + "mm")
    print("Median flipper length: " + str(flipper_length_median) + "mm")
    print("Standard Deviation flipper length: " + str(flipper_length_std) + "mm")
    print("Variance flipper length: " + str(flipper_length_var) + "mm²\n")

    # Body mass
    body_mass_avg = np.average(dataset.body_mass_g)
    body_mass_median = np.median(dataset.body_mass_g)
    body_mass_std = np.std(dataset.body_mass_g)
    body_mass_var = np.var(dataset.body_mass_g)

    print("Average body mass: " + str(body_mass_avg) + "g")
    print("Median body mass: " + str(body_mass_median) + "g")
    print("Standard Deviation body mass: " + str(body_mass_std) + "g")
    print("Variance body mass: " + str(body_mass_var) + "g²\n")

    # Bill length female
    bill_length_female = dataset.loc[dataset['sex'] == 'female', ['bill_length_mm']]
    bill_length_avg_female = np.average(bill_length_female)
    bill_length_median_female = np.median(bill_length_female)
    bill_length_std_female = np.std(bill_length_female)
    bill_length_var_female = np.var(bill_length_female)

    print("Average bill length female: " + str(bill_length_avg_female) + "mm")
    print("Median bill length female: " + str(bill_length_median_female) + "mm")
    print("Standard Deviation bill length female: " + str(bill_length_std_female) + "mm")
    print("Variance bill length female: " + str(bill_length_var_female) + "mm²\n")

    # Bill depth female
    bill_depth_female = dataset.loc[dataset['sex'] == 'female', ['bill_depth_mm']]
    bill_depth_avg_female = np.average(bill_depth_female)
    bill_depth_median_female = np.median(bill_depth_female)
    bill_depth_std_female = np.std(bill_depth_female)
    bill_depth_var_female = np.var(bill_depth_female)

    print("Average bill depth female: " + str(bill_depth_avg_female) + "mm")
    print("Median bill depth female: " + str(bill_depth_median_female) + "mm")
    print("Standard Deviation bill depth female: " + str(bill_depth_std_female) + "mm")
    print("Variance bill depth female: " + str(bill_depth_var_female) + "mm²\n")

    # Flipper length female
    flipper_length_female = dataset.loc[dataset['sex'] == 'female', ['flipper_length_mm']]
    flipper_length_avg_female = np.average(flipper_length_female)
    flipper_length_median_female = np.median(flipper_length_female)
    flipper_length_std_female = np.std(flipper_length_female)
    flipper_length_var_female = np.var(flipper_length_female)

    print("Average flipper length female: " + str(flipper_length_avg_female) + "mm")
    print("Median flipper length female: " + str(flipper_length_median_female) + "mm")
    print("Standard Deviation flipper length female: " + str(flipper_length_std_female) + "mm")
    print("Variance flipper length female: " + str(flipper_length_var_female) + "mm²\n")

    # Body mass female
    body_mass_female = dataset.loc[dataset['sex'] == 'female', ['body_mass_g']]
    body_mass_avg_female = np.average(body_mass_female)
    body_mass_median_female = np.median(body_mass_female)
    body_mass_std_female = np.std(body_mass_female)
    body_mass_var_female = np.var(body_mass_female)

    print("Average body mass female: " + str(body_mass_avg_female) + "g")
    print("Median body mass female: " + str(body_mass_median_female) + "g")
    print("Standard Deviation body mass female: " + str(body_mass_std_female) + "g")
    print("Variance body mass female: " + str(body_mass_var_female) + "g²\n")

    # Bill length male
    bill_length_male = dataset.loc[dataset['sex'] == 'male', ['bill_length_mm']]
    bill_length_avg_male = np.average(bill_length_male)
    bill_length_median_male = np.median(bill_length_male)
    bill_length_std_male = np.std(bill_length_male)
    bill_length_var_male = np.var(bill_length_male)

    print("Average bill length male: " + str(bill_length_avg_male) + "mm")
    print("Median bill length male: " + str(bill_length_median_male) + "mm")
    print("Standard Deviation bill length male: " + str(bill_length_std_male) + "mm")
    print("Variance bill length male: " + str(bill_length_var_male) + "mm²\n")

    # Bill depth male
    bill_depth_male = dataset.loc[dataset['sex'] == 'male', ['bill_depth_mm']]
    bill_depth_avg_male = np.average(bill_depth_male)
    bill_depth_median_male = np.median(bill_depth_male)
    bill_depth_std_male = np.std(bill_depth_male)
    bill_depth_var_male = np.var(bill_depth_male)

    print("Average bill depth male: " + str(bill_depth_avg_male) + "mm")
    print("Median bill depth male: " + str(bill_depth_median_male) + "mm")
    print("Standard Deviation bill depth male: " + str(bill_depth_std_male) + "mm")
    print("Variance bill depth male: " + str(bill_depth_var_male) + "mm²\n")

    # Flipper length male
    flipper_length_male = dataset.loc[dataset['sex'] == 'male', ['flipper_length_mm']]
    flipper_length_avg_male = np.average(flipper_length_male)
    flipper_length_median_male = np.median(flipper_length_male)
    flipper_length_std_male = np.std(flipper_length_male)
    flipper_length_var_male = np.var(flipper_length_male)

    print("Average flipper length male: " + str(flipper_length_avg_male) + "mm")
    print("Median flipper length male: " + str(flipper_length_median_male) + "mm")
    print("Standard Deviation flipper length male: " + str(flipper_length_std_male) + "mm")
    print("Variance flipper length male: " + str(flipper_length_var_male) + "mm²\n")

    # Body mass male
    body_mass_male = dataset.loc[dataset['sex'] == 'male', ['body_mass_g']]
    body_mass_avg_male = np.average(body_mass_male)
    body_mass_median_male = np.median(body_mass_male)
    body_mass_std_male = np.std(body_mass_male)
    body_mass_var_male = np.var(body_mass_male)

    print("Average body mass male: " + str(body_mass_avg_male) + "g")
    print("Median body mass male: " + str(body_mass_median_male) + "g")
    print("Standard Deviation body mass male: " + str(body_mass_std_male) + "g")
    print("Variance body mass male: " + str(body_mass_var_male) + "g²\n")

    # Bill length Adelie
    bill_length_adelie = dataset.loc[dataset['species'] == 'Adelie', ['bill_length_mm']]
    bill_length_avg_adelie = np.average(bill_length_adelie)
    bill_length_median_adelie = np.median(bill_length_adelie)
    bill_length_std_adelie = np.std(bill_length_adelie)
    bill_length_var_adelie = np.var(bill_length_adelie)

    print("Average bill length adelie: " + str(bill_length_avg_adelie) + "mm")
    print("Median bill length adelie: " + str(bill_length_median_adelie) + "mm")
    print("Standard Deviation bill length adelie: " + str(bill_length_std_adelie) + "mm")
    print("Variance bill length adelie: " + str(bill_length_var_adelie) + "mm²\n")

    # Bill depth Adelie
    bill_depth_adelie = dataset.loc[dataset['species'] == 'Adelie', ['bill_depth_mm']]
    bill_depth_avg_adelie = np.average(bill_depth_adelie)
    bill_depth_median_adelie = np.median(bill_depth_adelie)
    bill_depth_std_adelie = np.std(bill_depth_adelie)
    bill_depth_var_adelie = np.var(bill_depth_adelie)

    print("Average bill depth adelie: " + str(bill_depth_avg_adelie) + "mm")
    print("Median bill depth adelie: " + str(bill_depth_median_adelie) + "mm")
    print("Standard Deviation bill depth adelie: " + str(bill_depth_std_adelie) + "mm")
    print("Variance bill depth adelie: " + str(bill_depth_var_adelie) + "mm²\n")

    # Flipper length Adelie
    flipper_length_adelie = dataset.loc[dataset['species'] == 'Adelie', ['flipper_length_mm']]
    flipper_length_avg_adelie = np.average(flipper_length_adelie)
    flipper_length_median_adelie = np.median(flipper_length_adelie)
    flipper_length_std_adelie = np.std(flipper_length_adelie)
    flipper_length_var_adelie = np.var(flipper_length_adelie)

    print("Average flipper length adelie: " + str(flipper_length_avg_adelie) + "mm")
    print("Median flipper length adelie: " + str(flipper_length_median_adelie) + "mm")
    print("Standard Deviation flipper length adelie: " + str(flipper_length_std_adelie) + "mm")
    print("Variance flipper length adelie: " + str(flipper_length_var_adelie) + "mm²\n")

    # Body mass Adelie
    body_mass_adelie = dataset.loc[dataset['species'] == 'Adelie', ['body_mass_g']]
    body_mass_avg_adelie = np.average(body_mass_adelie)
    body_mass_median_adelie = np.median(body_mass_adelie)
    body_mass_std_adelie = np.std(body_mass_adelie)
    body_mass_var_adelie = np.var(body_mass_adelie)

    print("Average body mass adelie: " + str(body_mass_avg_adelie) + "g")
    print("Median body mass adelie: " + str(body_mass_median_adelie) + "g")
    print("Standard Deviation body mass adelie: " + str(body_mass_std_adelie) + "g")
    print("Variance body mass adelie: " + str(body_mass_var_adelie) + "g²\n")

    # Bill length Gentoo
    bill_length_gentoo = dataset.loc[dataset['species'] == 'Gentoo', ['bill_length_mm']]
    bill_length_avg_gentoo = np.average(bill_length_gentoo)
    bill_length_median_gentoo = np.median(bill_length_gentoo)
    bill_length_std_gentoo = np.std(bill_length_gentoo)
    bill_length_var_gentoo = np.var(bill_length_gentoo)

    print("Average bill length gentoo: " + str(bill_length_avg_gentoo) + "mm")
    print("Median bill length gentoo: " + str(bill_length_median_gentoo) + "mm")
    print("Standard Deviation bill length gentoo: " + str(bill_length_std_gentoo) + "mm")
    print("Variance bill length gentoo: " + str(bill_length_var_gentoo) + "mm²\n")

    # Bill depth Gentoo
    bill_depth_gentoo = dataset.loc[dataset['species'] == 'Gentoo', ['bill_depth_mm']]
    bill_depth_avg_gentoo = np.average(bill_depth_gentoo)
    bill_depth_median_gentoo = np.median(bill_depth_gentoo)
    bill_depth_std_gentoo = np.std(bill_depth_gentoo)
    bill_depth_var_gentoo = np.var(bill_depth_gentoo)

    print("Average bill depth gentoo: " + str(bill_depth_avg_gentoo) + "mm")
    print("Median bill depth gentoo: " + str(bill_depth_median_gentoo) + "mm")
    print("Standard Deviation bill depth gentoo: " + str(bill_depth_std_gentoo) + "mm")
    print("Variance bill depth gentoo: " + str(bill_depth_var_gentoo) + "mm²\n")

    # Flipper length Gentoo
    flipper_length_gentoo = dataset.loc[dataset['species'] == 'Gentoo', ['flipper_length_mm']]
    flipper_length_avg_gentoo = np.average(flipper_length_gentoo)
    flipper_length_median_gentoo = np.median(flipper_length_gentoo)
    flipper_length_std_gentoo = np.std(flipper_length_gentoo)
    flipper_length_var_gentoo = np.var(flipper_length_gentoo)

    print("Average flipper length gentoo: " + str(flipper_length_avg_gentoo) + "mm")
    print("Median flipper length gentoo: " + str(flipper_length_median_gentoo) + "mm")
    print("Standard Deviation flipper length gentoo: " + str(flipper_length_std_gentoo) + "mm")
    print("Variance flipper length gentoo: " + str(flipper_length_var_gentoo) + "mm²\n")

    # Body mass Gentoo
    body_mass_gentoo = dataset.loc[dataset['species'] == 'Gentoo', ['body_mass_g']]
    body_mass_avg_gentoo = np.average(body_mass_gentoo)
    body_mass_median_gentoo = np.median(body_mass_gentoo)
    body_mass_std_gentoo = np.std(body_mass_gentoo)
    body_mass_var_gentoo = np.var(body_mass_gentoo)

    print("Average body mass gentoo: " + str(body_mass_avg_gentoo) + "g")
    print("Median body mass gentoo: " + str(body_mass_median_gentoo) + "g")
    print("Standard Deviation body mass gentoo: " + str(body_mass_std_gentoo) + "g")
    print("Variance body mass gentoo: " + str(body_mass_var_gentoo) + "g²\n")

    # Bill length Chinstrap
    bill_length_chinstrap = dataset.loc[dataset['species'] == 'Chinstrap', ['bill_length_mm']]
    bill_length_avg_chinstrap = np.average(bill_length_chinstrap)
    bill_length_median_chinstrap = np.median(bill_length_chinstrap)
    bill_length_std_chinstrap = np.std(bill_length_chinstrap)
    bill_length_var_chinstrap = np.var(bill_length_chinstrap)

    print("Average bill length chinstrap: " + str(bill_length_avg_chinstrap) + "mm")
    print("Median bill length chinstrap: " + str(bill_length_median_chinstrap) + "mm")
    print("Standard Deviation bill length chinstrap: " + str(bill_length_std_chinstrap) + "mm")
    print("Variance bill length chinstrap: " + str(bill_length_var_chinstrap) + "mm²\n")

    # Bill depth Chinstrap
    bill_depth_chinstrap = dataset.loc[dataset['species'] == 'Chinstrap', ['bill_depth_mm']]
    bill_depth_avg_chinstrap = np.average(bill_depth_chinstrap)
    bill_depth_median_chinstrap = np.median(bill_depth_chinstrap)
    bill_depth_std_chinstrap = np.std(bill_depth_chinstrap)
    bill_depth_var_chinstrap = np.var(bill_depth_chinstrap)

    print("Average bill depth chinstrap: " + str(bill_depth_avg_chinstrap) + "mm")
    print("Median bill depth chinstrap: " + str(bill_depth_median_chinstrap) + "mm")
    print("Standard Deviation bill depth chinstrap: " + str(bill_depth_std_chinstrap) + "mm")
    print("Variance bill depth chinstrap: " + str(bill_depth_var_chinstrap) + "mm²\n")

    # Flipper length Chinstrap
    flipper_length_chinstrap = dataset.loc[dataset['species'] == 'Chinstrap', ['flipper_length_mm']]
    flipper_length_avg_chinstrap = np.average(flipper_length_chinstrap)
    flipper_length_median_chinstrap = np.median(flipper_length_chinstrap)
    flipper_length_std_chinstrap = np.std(flipper_length_chinstrap)
    flipper_length_var_chinstrap = np.var(flipper_length_chinstrap)

    print("Average flipper length chinstrap: " + str(flipper_length_avg_chinstrap) + "mm")
    print("Median flipper length chinstrap: " + str(flipper_length_median_chinstrap) + "mm")
    print("Standard Deviation flipper length chinstrap: " + str(flipper_length_std_chinstrap) + "mm")
    print("Variance flipper length chinstrap: " + str(flipper_length_var_chinstrap) + "mm²\n")

    # Body mass Chinstrap
    body_mass_chinstrap = dataset.loc[dataset['species'] == 'Chinstrap', ['body_mass_g']]
    body_mass_avg_chinstrap = np.average(body_mass_chinstrap)
    body_mass_median_chinstrap = np.median(body_mass_chinstrap)
    body_mass_std_chinstrap = np.std(body_mass_chinstrap)
    body_mass_var_chinstrap = np.var(body_mass_chinstrap)

    print("Average body mass chinstrap: " + str(body_mass_avg_chinstrap) + "g")
    print("Median body mass chinstrap: " + str(body_mass_median_chinstrap) + "g")
    print("Standard Deviation body mass chinstrap: " + str(body_mass_std_chinstrap) + "g")
    print("Variance body mass chinstrap: " + str(body_mass_var_chinstrap) + "g²\n")

    # Bill length Torgersen
    bill_length_torgersen = dataset.loc[dataset['island'] == 'Torgersen', ['bill_length_mm']]
    bill_length_avg_torgersen = np.average(bill_length_torgersen)
    bill_length_median_torgersen = np.median(bill_length_torgersen)
    bill_length_std_torgersen = np.std(bill_length_torgersen)
    bill_length_var_torgersen = np.var(bill_length_torgersen)

    print("Average bill length torgersen: " + str(bill_length_avg_torgersen) + "mm")
    print("Median bill length torgersen: " + str(bill_length_median_torgersen) + "mm")
    print("Standard Deviation bill length torgersen: " + str(bill_length_std_torgersen) + "mm")
    print("Variance bill length torgersen: " + str(bill_length_var_torgersen) + "mm²\n")

    # Bill depth Torgersen
    bill_depth_torgersen = dataset.loc[dataset['island'] == 'Torgersen', ['bill_depth_mm']]
    bill_depth_avg_torgersen = np.average(bill_depth_torgersen)
    bill_depth_median_torgersen = np.median(bill_depth_torgersen)
    bill_depth_std_torgersen = np.std(bill_depth_torgersen)
    bill_depth_var_torgersen = np.var(bill_depth_torgersen)

    print("Average bill depth torgersen: " + str(bill_depth_avg_torgersen) + "mm")
    print("Median bill depth torgersen: " + str(bill_depth_median_torgersen) + "mm")
    print("Standard Deviation bill depth torgersen: " + str(bill_depth_std_torgersen) + "mm")
    print("Variance bill depth torgersen: " + str(bill_depth_var_torgersen) + "mm²\n")

    # Flipper length Torgersen
    flipper_length_torgersen = dataset.loc[dataset['island'] == 'Torgersen', ['flipper_length_mm']]
    flipper_length_avg_torgersen = np.average(flipper_length_torgersen)
    flipper_length_median_torgersen = np.median(flipper_length_torgersen)
    flipper_length_std_torgersen = np.std(flipper_length_torgersen)
    flipper_length_var_torgersen = np.var(flipper_length_torgersen)

    print("Average flipper length torgersen: " + str(flipper_length_avg_torgersen) + "mm")
    print("Median flipper length torgersen: " + str(flipper_length_median_torgersen) + "mm")
    print("Standard Deviation flipper length torgersen: " + str(flipper_length_std_torgersen) + "mm")
    print("Variance flipper length torgersen: " + str(flipper_length_var_torgersen) + "mm²\n")

    # Body mass Torgersen
    body_mass_torgersen = dataset.loc[dataset['island'] == 'Torgersen', ['body_mass_g']]
    body_mass_avg_torgersen = np.average(body_mass_torgersen)
    body_mass_median_torgersen = np.median(body_mass_torgersen)
    body_mass_std_torgersen = np.std(body_mass_torgersen)
    body_mass_var_torgersen = np.var(body_mass_torgersen)

    print("Average flipper length torgersen: " + str(body_mass_avg_torgersen) + "g")
    print("Median flipper length torgersen: " + str(body_mass_median_torgersen) + "g")
    print("Standard Deviation flipper length torgersen: " + str(body_mass_std_torgersen) + "g")
    print("Variance flipper length torgersen: " + str(body_mass_var_torgersen) + "g²\n")

    # Bill length Biscoe
    bill_length_biscoe = dataset.loc[dataset['island'] == 'Biscoe', ['bill_length_mm']]
    bill_length_avg_biscoe = np.average(bill_length_biscoe)
    bill_length_median_biscoe = np.median(bill_length_biscoe)
    bill_length_std_biscoe = np.std(bill_length_biscoe)
    bill_length_var_biscoe = np.var(bill_length_biscoe)

    print("Average bill length biscoe: " + str(bill_length_avg_biscoe) + "mm")
    print("Median bill length biscoe: " + str(bill_length_median_biscoe) + "mm")
    print("Standard Deviation bill length biscoe: " + str(bill_length_std_biscoe) + "mm")
    print("Variance bill length biscoe: " + str(bill_length_var_biscoe) + "mm²\n")

    # Bill depth Biscoe
    bill_depth_biscoe = dataset.loc[dataset['island'] == 'Biscoe', ['bill_depth_mm']]
    bill_depth_avg_biscoe = np.average(bill_depth_biscoe)
    bill_depth_median_biscoe = np.median(bill_depth_biscoe)
    bill_depth_std_biscoe = np.std(bill_depth_biscoe)
    bill_depth_var_biscoe = np.var(bill_depth_biscoe)

    print("Average bill depth biscoe: " + str(bill_depth_avg_biscoe) + "mm")
    print("Median bill depth biscoe: " + str(bill_depth_median_biscoe) + "mm")
    print("Standard Deviation bill depth biscoe: " + str(bill_depth_std_biscoe) + "mm")
    print("Variance bill depth biscoe: " + str(bill_depth_var_biscoe) + "mm²\n")

    # Flipper length Biscoe
    flipper_length_biscoe = dataset.loc[dataset['island'] == 'Biscoe', ['flipper_length_mm']]
    flipper_length_avg_biscoe = np.average(flipper_length_biscoe)
    flipper_length_median_biscoe = np.median(flipper_length_biscoe)
    flipper_length_std_biscoe = np.std(flipper_length_biscoe)
    flipper_length_var_biscoe = np.var(flipper_length_biscoe)

    print("Average flipper length biscoe: " + str(flipper_length_avg_biscoe) + "mm")
    print("Median flipper length biscoe: " + str(flipper_length_median_biscoe) + "mm")
    print("Standard Deviation flipper length biscoe: " + str(flipper_length_std_biscoe) + "mm")
    print("Variance flipper length biscoe: " + str(flipper_length_var_biscoe) + "mm²\n")

    # Body mass Biscoe
    body_mass_biscoe = dataset.loc[dataset['island'] == 'Biscoe', ['body_mass_g']]
    body_mass_avg_biscoe = np.average(body_mass_biscoe)
    body_mass_median_biscoe = np.median(body_mass_biscoe)
    body_mass_std_biscoe = np.std(body_mass_biscoe)
    body_mass_var_biscoe = np.var(body_mass_biscoe)

    print("Average body mass biscoe: " + str(body_mass_avg_biscoe) + "g")
    print("Median body mass biscoe: " + str(body_mass_median_biscoe) + "g")
    print("Standard Deviation body mass biscoe: " + str(body_mass_std_biscoe) + "g")
    print("Variance body mass biscoe: " + str(body_mass_var_biscoe) + "g²\n")

    # Bill length Dream
    bill_length_dream = dataset.loc[dataset['island'] == 'Dream', ['bill_length_mm']]
    bill_length_avg_dream = np.average(bill_length_dream)
    bill_length_median_dream = np.median(bill_length_dream)
    bill_length_std_dream = np.std(bill_length_dream)
    bill_length_var_dream = np.var(bill_length_dream)

    print("Average bill length dream: " + str(bill_length_avg_dream) + "mm")
    print("Median bill length dream: " + str(bill_length_median_dream) + "mm")
    print("Standard Deviation bill length dream: " + str(bill_length_std_dream) + "mm")
    print("Variance bill length dream: " + str(bill_length_var_dream) + "mm²\n")

    # Bill depth Dream
    bill_depth_dream = dataset.loc[dataset['island'] == 'Dream', ['bill_depth_mm']]
    bill_depth_avg_dream = np.average(bill_depth_dream)
    bill_depth_median_dream = np.median(bill_depth_dream)
    bill_depth_std_dream = np.std(bill_depth_dream)
    bill_depth_var_dream = np.var(bill_depth_dream)

    print("Average bill depth dream: " + str(bill_depth_avg_dream) + "mm")
    print("Median bill depth dream: " + str(bill_depth_median_dream) + "mm")
    print("Standard Deviation bill depth dream: " + str(bill_depth_std_dream) + "mm")
    print("Variance bill depth dream: " + str(bill_depth_var_dream) + "mm²\n")

    # Flipper length Dream
    flipper_length_dream = dataset.loc[dataset['island'] == 'Dream', ['flipper_length_mm']]
    flipper_length_avg_dream = np.average(flipper_length_dream)
    flipper_length_median_dream = np.median(flipper_length_dream)
    flipper_length_std_dream = np.std(flipper_length_dream)
    flipper_length_var_dream = np.var(flipper_length_dream)

    print("Average flipper length dream: " + str(flipper_length_avg_dream) + "mm")
    print("Median flipper length dream: " + str(flipper_length_median_dream) + "mm")
    print("Standard Deviation flipper length dream: " + str(flipper_length_std_dream) + "mm")
    print("Variance flipper length dream: " + str(flipper_length_var_dream) + "mm²\n")

    # Body mass Dream
    body_mass_dream = dataset.loc[dataset['island'] == 'Dream', ['body_mass_g']]
    body_mass_avg_dream = np.average(body_mass_dream)
    body_mass_median_dream = np.median(body_mass_dream)
    body_mass_std_dream = np.std(body_mass_dream)
    body_mass_var_dream = np.var(body_mass_dream)

    print("Average flipper length dream: " + str(body_mass_avg_dream) + "g")
    print("Median flipper length dream: " + str(body_mass_median_dream) + "g")
    print("Standard Deviation flipper length dream: " + str(body_mass_std_dream) + "g")
    print("Variance flipper length dream: " + str(body_mass_var_dream) + "g²\n")

import pandas as pd
import boxplots
import pie_plots
import scatter_plots
import statistical_values

plots_dir = "../plots"
data_file = "../data/penguins.csv"

dataset = pd.read_csv(data_file, sep=',', index_col=0)

# Remove NaN values
dataset.dropna(inplace=True)

boxplots.generate_boxplots(dataset, plots_dir)
pie_plots.generate_pie_plots(dataset, plots_dir)
scatter_plots.generate_scatter_plots(dataset, plots_dir)
statistical_values.calculate_statistical_values(dataset)

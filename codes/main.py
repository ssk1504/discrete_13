import matplotlib.pyplot as plt

def stem_plot_from_file(file_path, highlight_index=None):
    with open(file_path, 'r') as file:
        coordinates = [list(map(int, line.split())) for line in file]

    n_values, x_values = zip(*coordinates)

    plt.stem(n_values, x_values, linefmt='-', markerfmt='.', basefmt=' ')
    if highlight_index is not None:
        plt.stem(n_values[highlight_index], x_values[highlight_index], linefmt='r-', markerfmt='ro', basefmt=' ')

    plt.xlabel('n')
    plt.ylabel('x(n)')
    plt.title('Stem Plot of x(n) = 8 + 6n')
    plt.grid(True)
    plt.show()
    plt.savefig("plot.png")

# Call the function with the file path and highlight index
file_path = 'coordinates.txt'
highlight_index = 26
stem_plot_from_file(file_path, highlight_index)


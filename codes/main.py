import matplotlib.pyplot as plt

def stem_plot(x_values, y_values, highlight_index=None):
    plt.stem(x_values, y_values, linefmt='-', markerfmt='.', basefmt=' ')
    if highlight_index is not None:
        plt.stem(x_values[highlight_index], y_values[highlight_index], linefmt='r-', markerfmt='ro', basefmt=' ')

# Generate the sequence x(n) = 8 + 6n for n = 0 to 30
n_values = list(range(31))
x_values = [8 + 6 * n for n in n_values]

# Plot the stem plot with the highlighted point at n=26 in red
highlight_index = 26
stem_plot(n_values, x_values, highlight_index)

plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Plot of x(n) = 8 + 6n')
plt.grid(True)
plt.show()

#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("coordinates.txt", "w");

    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Calculate and save coordinates for x(n) = 8 + 6n for n = 0 to 30
    for (int n = 0; n <= 30; ++n) {
        fprintf(file, "%d %d\n", n, 8 + 6 * n);
    }

    fclose(file);

    return 0;
}


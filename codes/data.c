#include <stdio.h>

void calculate_and_save_coordinates(FILE *file, int a, int d, int n) {
    for (int i = 0; i <= n; ++i) {
        fprintf(file, "%d %d\n", i, a + d * i);
    }
}

int main() {
    FILE *file;
    file = fopen("coordinates.txt", "w");

    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Calculate and save coordinates for x(n) = a + dn for n = 0 to 30
    calculate_and_save_coordinates(file, 8, 6, 30);

    fclose(file);

    return 0;
}


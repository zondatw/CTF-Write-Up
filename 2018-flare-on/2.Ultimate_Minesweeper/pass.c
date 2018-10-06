#include <stdio.h>
#include <stdlib.h>

unsigned int VALLOC_TYPES[] = {
    4294966400,
    4294966657,
    4294967026
};
unsigned int VALLOC_NODE_LIMIT = 30;

unsigned int DeriveVallocType (int x, int y){
    return ~(x * VALLOC_NODE_LIMIT + y);
}

int main() {

    for (int x = 0; x < VALLOC_NODE_LIMIT; x++) {
        for (int y = 0; y < VALLOC_NODE_LIMIT; y++) {
            unsigned int result = DeriveVallocType(x+1, y+1);
            if (VALLOC_TYPES[0] == result || VALLOC_TYPES[1] == result || VALLOC_TYPES[2] == result) {
                printf("%d,%d\n", x, y);
            }
        }
    }

    return 0;
}
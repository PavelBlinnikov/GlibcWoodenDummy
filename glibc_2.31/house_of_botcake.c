#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>


int main()
{
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);

    intptr_t stack_var[4];

    intptr_t *x[7];
    for(int i=0; i<sizeof(x)/sizeof(intptr_t*); i++){
        x[i] = malloc(0x100);
    }

    intptr_t *prev = malloc(0x100);
    intptr_t *a = malloc(0x100);
    malloc(0x10);

    for(int i=0; i<7; i++){
        free(x[i]);
    }
    free(a);
    free(prev);
    malloc(0x100);
    free(a);

    intptr_t *b = malloc(0x120);
    b[0x120/8-2] = (long)stack_var;

    malloc(0x100);
    intptr_t *c = malloc(0x100);

    if (c==stack_var) {
      exit(228);
    } else {
      exit(227);
    }
}

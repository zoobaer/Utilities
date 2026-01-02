#include<stdio.h>

#include "logger.h"
#include "colors.h"

void error(FILE *stream, char *type, char *message) {
    if (type == NULL || message == NULL) {
	fprintf(stderr, RED "%s: %s", type, message);
	fprintf(stream, RESET"\n");
    }
    
    fprintf(stream, RED "%s: %s", type, message);
    fprintf(stream, RESET"\n");
}

void info(FILE *stream, char *type, char *message) {
    if (type == NULL || message == NULL) {
	fprintf(stderr, RED "%s: %s", "info_out", "type or message NULL");
	fprintf(stream, RESET"\n");
    }
    
    fprintf(stream, GREEN "%s: %s", type, message);
    fprintf(stream, RESET"\n");
}



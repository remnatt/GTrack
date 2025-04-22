// src/logger.c
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

void log_to_file(const char *filename, const char *action, const char *file, const char *message, int add_timestamp) {
    FILE *logfile = fopen(filename, "a");
    if (!logfile) return;

    if (add_timestamp) {
        time_t now = time(NULL);
        char *timestamp = ctime(&now);
        if (timestamp) timestamp[strcspn(timestamp, "\n")] = 0;
        fprintf(logfile, "[%s] ", timestamp);
    }

    fprintf(logfile, "%s | %s | %s\n", action, file, message);
    fclose(logfile);
}

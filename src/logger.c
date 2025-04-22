// src/logger.c
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

void log_to_file(const char *filename, const char *action, const char *file, const char *message) {
    FILE *logfile = fopen(filename, "a");
    if (!logfile) return;

    time_t now = time(NULL);
    char *timestamp = ctime(&now);
    if (timestamp) timestamp[strcspn(timestamp, "\n")] = 0;

    fprintf(logfile, "[%s] %s | %s | %s\n", timestamp, action, file, message);
    fclose(logfile);
}
// GTrack
// to be used via cython

# logger_wrapper.pyx
cdef extern from "logger.h":
    void log_to_file(const char *filename, const char *action, const char *file, const char *message, int add_timestamp)

def clog(str filename, str action, str file, str message, bool add_timestamp):
    log_to_file(filename.encode('utf-8'), action.encode('utf-8'), file.encode('utf-8'), message.encode('utf-8'), int(add_timestamp))

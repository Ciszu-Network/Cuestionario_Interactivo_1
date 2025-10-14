import sys

class DualLogger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

def start_log(filename):
    sys.stdout = DualLogger(filename)

def stop_log():
    sys.stdout.log.close()
    sys.stdout = sys.stdout.terminal
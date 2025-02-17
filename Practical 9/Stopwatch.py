import time

class Stopwatch:
    def __init__(self, start_time=0, end_time=0, elapsed_time=0):
        self.start_time = start_time
        self.end_time = end_time
        self.elapsed_time = elapsed_time

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()
        self.calculate_elapsed_time()

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def calculate_elapsed_time(self):
        self.elapsed_time = self.end_time - self.start_time
    
    def get_elapsed_time(self):
        return self.elapsed_time
    
    def get_hms(self):      
        hours, remainder = divmod(round(self.elapsed_time), 3600)
        minutes, seconds = divmod(remainder, 60)
        return hours, minutes, seconds
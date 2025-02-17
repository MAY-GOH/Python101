import time

start_time, end_time = 0, 0

def start():
    global start_time
   
    start_time = time.time()
    
    return start_time

def stop():
    global end_time
    
    end_time = time.time()
    
    return end_time

def get_elapsed_time(): 
    global start_time, end_time
    
    return get_hms(round(end_time - start_time))
    
def get_hms(elapsed_time):    
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return hours, minutes, seconds
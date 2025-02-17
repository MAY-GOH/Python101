def read_filename():
    prompt = "A filename consists of a name and its extension (e.g., document.txt)\nEnter a filename: "
    return input(prompt).strip()

def open_file(filename, mode):
    return open(filename, mode)

def read_file(file):
    return [line.strip() for line in file.readlines() if not is_header(line)]

def write_file(file, contents):
    file.writelines(contents) 

def is_header(row):
    # Basic checks for header characteristics
    # Modify this function based on your specific header criteria
    # Here we check if the row contains only strings (assuming headers are non-numeric)
    return all(cell.isalpha() or cell.isspace() for cell in row.split())
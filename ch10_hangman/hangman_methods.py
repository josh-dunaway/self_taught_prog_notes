from operator import truediv

def file_can_be_found(path: str) -> bool:
    import os
    if os.path.exists(path):
        return True
    return False

#should not be used for massive files - just those
#with a few hundred lines of text
def count_lines_in_txt_file(path: str) -> int:
    if(file_can_be_found(path)):
        with open(path, 'r') as f:
            num_lines = len(f.readlines())
        return num_lines
    return None

def get_random_line_from_file(path: str) -> str:
    num_lines = count_lines_in_txt_file(path)
    if num_lines == None:
        return None
    import random
    with open(path, 'r') as f:
        for i in range(random.randint(1, num_lines)):
            selected_word = f.readline()
    return selected_word
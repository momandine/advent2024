import os

def slurp(day: int):
    input_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(input_dir, f'input{day}.txt')


    with open(filename, 'r') as file:
        return file.read()

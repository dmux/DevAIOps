"""
Exemplo de código Python com vários code smells para análise de revisão.
"""
import os

def process_files(files):
    result = 0
    for f in files:
        if os.path.exists(f):
            with open(f) as file:
                for line in file:
                    if len(line) > 0:
                        if line.strip() != '':
                            if line.startswith('#'):
                                continue
                            else:
                                result += 1
    return result

def main():
    files = ['file1.txt', 'file2.txt', 'file3.txt']
    print(process_files(files))
    print(process_files(files))  # Duplicação
    print(process_files(files))  # Duplicação

if __name__ == "__main__":
    main()

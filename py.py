import os
import fnmatch

def read_files_in_directory(directory, output_file):
    # Расширения файлов изображений, которые мы хотим игнорировать
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff']
    
    # Создание паттерна для фильтрации изображений
    ignore_patterns = [pattern for ext in image_extensions for pattern in fnmatch.filter(os.listdir(directory), ext)]

    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Проход по всем файлам в директории
        for filename in os.listdir(directory):
            # Проверка, является ли файл изображением
            if filename not in ignore_patterns:
                file_path = os.path.join(directory, filename)
                
                # Проверка, является ли путь файлом
                if os.path.isfile(file_path):
                    # Чтение содержимого файла
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                        content = infile.read()
                    
                    # Запись в выходной файл
                    outfile.write(f"{file_path}\n\n{content}\n\n")

# Пример использования
directory = 'C:\\nediol.github.io'  # Укажите путь к вашей папке
output_file = 'read.txt'  # Имя выходного файла
read_files_in_directory(directory, output_file)

print(f"Содержимое всех файлов (кроме изображений) записано в {output_file}.")

import os
import json
import shutil

def rename_mafiles():
    # Создаем папки input и output, если они не существуют
    input_dir = "input"
    output_dir = "output"
    
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    # Перебираем все файлы в папке input
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        
        # Проверяем, что это файл
        if os.path.isfile(input_path):
            try:
                # Читаем содержимое файла
                with open(input_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                
                # Получаем значение account_name
                if 'account_name' in data:
                    account_name = data['account_name']
                    # Создаем новое имя файла
                    new_filename = f"{account_name}.maFile"
                    output_path = os.path.join(output_dir, new_filename)
                    
                    # Копируем файл с новым именем
                    shutil.copy2(input_path, output_path)
                    print(f"Файл {filename} успешно переименован в {new_filename}")
                else:
                    print(f"В файле {filename} отсутствует поле 'account_name'")
                    
            except json.JSONDecodeError:
                print(f"Ошибка при чтении JSON из файла {filename}")
            except Exception as e:
                print(f"Произошла ошибка при обработке файла {filename}: {str(e)}")

if __name__ == "__main__":
    rename_mafiles()

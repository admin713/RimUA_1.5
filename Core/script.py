import os

def rename_files(directory='.'):
    for root, _, files in os.walk(directory):
        for file in files:
            if "_RWUAB" in file:
                base, ext = os.path.splitext(file)
                new_name = base.replace("_RWUAB", "") + ext
                try:
                    os.rename(os.path.join(root, file), os.path.join(root, new_name))
                except Exception as error:
                    print(f"Не вдалося перейменувати файл {os.path.join(root, file)}. Помилка: {error}")

try:
    rename_files()
except Exception as error:
    print(f"Виникла помилка при виконанні скрипта: {error}")

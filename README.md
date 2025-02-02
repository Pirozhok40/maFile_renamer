# MaFile Renamer для Dropler-GUI

Этот скрипт предназначен для автоматического массового переименования maFile файлов на основе содержащегося в них поля "account_name". Скрипт создан для удобной подготовки файлов для работы с [Dropler-GUI](https://github.com/Pirozhok40/Dropler-GUI).

## Описание

Скрипт автоматически:
- Читает maFile файлы из папки `input`
- Извлекает значение поля "account_name" из каждого файла
- Создает копию файла в папке `output` с именем в формате `{account_name}.maFile`

## Требования

- Python 3.6 или выше
- Стандартные библиотеки Python (os, json, shutil)

## Установка

1. Скачайте файл `renamer.py`
2. Создайте папку `input` и `output` в той же директории, где находится скрипт

## Использование

1. Поместите ваши maFile файлы в папку `input`
2. Запустите скрипт командой:
   ```
   python renamer.py
   ```
3. Переименованные файлы появятся в папке `output`

## Структура файлов

```
├── renamer.py
├── input/
│   ├── maFile1
│   ├── maFile2
│   └── ...
└── output/
    ├── account_name1.maFile
    ├── account_name2.maFile
    └── ...
```

## Обработка ошибок

Скрипт включает обработку следующих ошибок:
- Отсутствие поля "account_name" в файле
- Некорректный JSON формат
- Общие ошибки чтения/записи файлов

## Примечание

Этот скрипт создан специально для работы с [Dropler-GUI](https://github.com/Pirozhok40/Dropler-GUI) и обеспечивает правильное именование файлов для корректной работы программы.

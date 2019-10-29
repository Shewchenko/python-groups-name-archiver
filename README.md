# Архиватор и чекер на Python #
> (Поддержка python 3.^)

### Описание ###
`files_to_zip.py` - этот скрипт находит все файлы с одинаковым названием. Группирует их   
и добавляет в один архив взяв название файла.
#### Пример работы ####
* Список файлов в каталоге  
name1.png  
name1.jpg  
name1.txt  
name2.png  
name2.jpg  
* После выполнения скрипта  
name1.zip (в середине: name1.png, name1.jpg, name1.txt)  
name2.zip (в середине: name2.png, name2.jpg)  
  
`check_archves.py` - этот скрипт находит все архивы `*.zip` и выводит
 информацию о содержимом архива в командную строку, а также сохраняет в файл `check_output_list`
#### Пример работы ####
* Список архивов в каталоге  
name1.zip  
name2.zip  
* После выполнения скрипта  
name: name1.zip --> count files: 3  
name: name2.zip --> count files: 2  

## Пример использования ##
* Нужно либо скачать портативный Python
> [Прямая ссылка для скачивания портативного Python для Windows (python-3.7.5rc1)](https://www.python.org/ftp/python/3.7.5/python-3.7.5rc1-embed-amd64.zip)  
либо инсталятор   
> [Скачать Python для Windows](https://www.python.org/downloads/windows/)

на ваш компьютер.

* Положить `files_to_zip.py`, `check_archves.py` в папку с файлами
* Открыть командную строку (Windows: win->cmd)
* Перейти в папку с файлами `cd /your/path/folder`
* Выполнить команду для архивации `/your/path/to/python/python.exe files_to_zip.py`
* Выполнить команду для проверки `/your/path/to/python/python.exe check_archves.py`


-Python3 предустановлен
-Создать директорию для проекта, перейти в каталог
-создать виртуальное окружение,можно командой  python -m venv 
-активировать окружение Scripts/activate 
-установить фреймворк Django и библиотеки, используя requirements.txt ,  pip install requirements.txt

-командой django-admin startproject yalantis создать проект
-командой django-admin startapp courses создать приложение
-загрузить файлы с репозитория git clone <repository url>

-в файле настроек проекта settings.py в строке с "INSTALLED_APPS" добавить имя созданного приложения, courses 

-выполнить python manage.py makemigrations, python manage.py migrate
-командой python manage.py runserver запустить приложение




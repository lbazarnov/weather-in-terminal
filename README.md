# weather-in-terminal

## Описание проекта

Скрипт позволяет просматривать погоду прямо в терминале для трёх локаций: Лондона, Шереметьева и Череповца.

## Установка и запуск скрипта

Для запуска скрипта необходимо установить [poetry](https://python-poetry.org/docs/master#installation) и [python](https://www.python.org) версии не ниже 3.8.

После этого:

1. Склонировать репозиторий к себе на компьютер

   ```
   $ git clone https://github.com/lbazarnov/weather-in-terminal.git
   ```

2. Последовательно запустить несколько команд
    ```
    $ сd weather-in-terminal
    $ make install # Для установки зависимостей проекта
    $ make build # Для сборки проекта
    $ make package-install # Для установки скрипта на компьютер
    ```

3. Запустить скрипт командой
    ```
    $ weatherapp
    ```

## Результат выполнения скрипта

[![asciicast](https://asciinema.org/a/wATg1OjSKZjVO84ho2redq1JX.svg)](https://asciinema.org/a/wATg1OjSKZjVO84ho2redq1JX)
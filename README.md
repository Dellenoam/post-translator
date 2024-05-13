# post-translator
Скрипт, который при запуске берет последний пост из telegram канала, переводит его и отправляет пользователю. Далее от этого поста уже будут искаться новые и также переводиться и отправляться пользователю с указанной в настройках переодичностью

## Установка

Для установки нужно создать виртуальное окружение

Windows
```bash
python -m venv .venv
```

Linux and MacOS
```bash
python3 -m venv .venv
```

Переходим в папку со скриптом и активируем это вирутальное окружение

Windows
```bash
.venv\Scripts\activate.bat
```

Linux and MacOS
```bash
source .venv/bin/activate
```

Далее нужно установить необходимые зависимости

```bash
pip install -r requirements.txt
```

Нужно будет получить API ID и API HASH. Сделать это можно на [my.telegram.org](https://my.telegram.org/)

Также нужно узнать id чата, куда будут отправляться переводы. Для этого можно воспользоваться данным ботом [@getmyid_bot](https://t.me/getmyid_bot)

## Запуск

Для запуска введите команду ниже

```bash
python main.py
```
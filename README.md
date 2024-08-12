# EN
**GenAternosMC** is a Python script designed to automate the process of keeping your Aternos Minecraft server online. This script uses undetected-chromedriver to interact with the Aternos website, ensuring your server stays up and running even when you are away.

## Features
- **Automated Server Management**: Automatically starts your Aternos server and keeps it online.
- **Ad Block Handling**: Manages ad pop-ups to ensure uninterrupted operation.
- **Customizable Configurations**: Uses a `config.json` file for easy configuration of server details.
- **Logging**: Logs actions and errors for monitoring and debugging.

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/geniuszlyy/GenAternosMC.git
   cd GenAternosMC
   ```
2. **Install Dependencies**\
Ensure you have Python 3.8 or higher installed. Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. **Create Config File**\
Create a `config.json` file in the project root directory with the following structure:
   ```json
   {
    "aternos_server": {
        "ip": "your_server_ip",
        "server_id": "your_server_id",
        "session_cookie": "your_session_cookie"
       }
   }
   ```
    Replace `your_server_ip`, `your_server_id`, and `your_session_cookie` with your server's actual details.

## How to Get Your Server ID, Session Cookie, and Server IP
### Server ID
1. Go to the Aternos website.
2. Log in to your account.
3. Navigate to the "Servers" tab.
4. Click on the server you want to manage.
5. The server ID will be part of the URL. It looks something like this: `https://aternos.org/server/#<server_id>`.(example - #rZRG9rGv7xTrC8CW)
### Session Cookie
1. Open the Aternos website and log in to your account.
2. Press `F12` to open the Developer Tools (or right-click and select "Inspect").
3. Go to the "Application" tab.
4. In the left sidebar, expand the "Cookies" section and select `https://aternos.org`.
5. Find the `ATERNOS_SESSION` cookie. The value is your session cookie.
### Server IP
1. Go to the Aternos website.
2. Log in to your account.
3. Navigate to the "Servers" tab.
4. Click on the server you want to manage.
5. The IP address will be displayed on the server dashboard.

## Usage
Run the script using the command line:
```bash
python GenAternosMC.py
```
## Instructions

![image](https://github.com/user-attachments/assets/8228e9bb-96a5-4832-99a5-2d7592ab95c3)


# RU
**GenAternosMC** - это Python-скрипт, предназначенный для автоматизации процесса поддержания вашего Minecraft-сервера на Aternos в онлайн-режиме. Этот скрипт использует undetected-chromedriver для взаимодействия с сайтом Aternos, чтобы ваш сервер оставался запущенным, даже когда вас нет на месте.

## Возможности
- **Автоматическое управление сервером**: Автоматически запускает сервер на Aternos и поддерживает его онлайн.
- **Обработка рекламы**: Управляет всплывающими окнами рекламы для обеспечения бесперебойной работы.
- **Настраиваемые конфигурации**: Использует файл `config.json` для легкой настройки параметров сервера.
- **Логирование**: Записывает действия и ошибки для мониторинга и отладки.

## Установка
1. **Клонирование репозитория**
   ```bash
   git clone https://github.com/geniuszlyy/GenAternosMC.git
   cd GenAternosMC
   ```
2. **Установка зависимостей**\
Убедитесь, что у вас установлена версия Python 3.8 или выше. Установите необходимые пакеты Python, используя pip:
   ```bash
   pip install -r requirements.txt
   ```
3. **Создание файла конфигурации**\
Создайте файл `config.json` в корневой директории проекта со следующей структурой:
   ```json
   {
    "aternos_server": {
        "ip": "ваш_ip_сервера",
        "server_id": "ваш_id_сервера",
        "session_cookie": "ваш_cookie_сессии"
       }
   }
   ```
   Замените `ваш_ip_сервера`, `ваш_id_сервера` и `ваш_cookie_сессии` на фактические данные вашего сервера.

## Как получить ID сервера, cookie сессии и IP сервера
### ID сервера
1. Перейдите на сайт Aternos.
2. Войдите в свой аккаунт.
3. Перейдите на вкладку "Серверы".
4. Нажмите на сервер, который хотите управлять.
5. ID сервера будет частью URL. Это выглядит примерно так: `https://aternos.org/server/#<server_id>`. (Например - #rZRG9rGv7xTrC8CW)
### Куки сессии
1. Откройте сайт Aternos и войдите в свой аккаунт.
2. Нажмите `F12` для открытия инструментов разработчика (или щелкните правой кнопкой мыши и выберите "Просмотр кода").
3. Перейдите на вкладку "Application".
4. В левой панели разверните раздел "Cookies" и выберите `https://aternos.org`.
5. Найдите куки `ATERNOS_SESSION`. Его значение — это ваша куки сессии.
### IP сервера
1. Перейдите на сайт Aternos.
2. Войдите в свой аккаунт.
3. Перейдите на вкладку "Серверы".
4. Нажмите на сервер, который хотите управлять.
5. IP-адрес будет отображен на панели управления сервером.

## Использование
Запустите скрипт с помощью командной строки:
```bash
python GenAternosMC.py
```

## Инструкции

![image](https://github.com/user-attachments/assets/b087c79e-0a60-4b93-8061-8a7239420ca6)

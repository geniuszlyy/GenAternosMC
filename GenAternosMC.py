import os
import undetected_chromedriver as uc
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import random
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Класс для логирования сообщений с отметками времени и записи их в файл
class LogManager:

    # Логгирование сообщений в файл
    def log_to_file(self, message=None, filename='activity_log.txt'):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(filename, 'a') as file:
            file.write(f'[{current_time}] {message}\n')

    # Функция паузы на заданное количество секунд
    def delay_execution(self, seconds):
        time.sleep(seconds)

# Настройка и инициализация драйвера Chrome с заданными опциями
def setup_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True
    chrome_options.add_argument("start-maximized")
    user_agent_str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    chrome_options.add_argument(f"--user-agent={user_agent_str}")
    return uc.Chrome(options=chrome_options)

# Функция поддержания активности сервера
def maintain_server_connection(driver):
    print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Инициализация поддержания активности сервера')
    while True:
        try:
            extend_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[@class="extend"]/button[@class="btn btn-tiny btn-success server-extend-end"]'))
            )
            extend_button.click()
            print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.GREEN}Соединение с сервером продлено{Style.RESET_ALL}')
        except KeyboardInterrupt:
            print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Получен сигнал прерывания (Ctrl+C)')
            break
        except Exception as e:
            timer_text = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="read-our-tos"]/main/section/div[3]/div[2]/div[1]/div/div/div[1]/div[1]/div'))
            ).text
            print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Таймер: {Fore.LIGHTGREEN_EX}{timer_text}{Style.RESET_ALL}')
            handle_ad_popup(driver)
            time.sleep(random.randint(1, 7))

# Функция обработки всплывающего окна с рекламой
def handle_ad_popup(driver):
    try:
        ad_popup_button = driver.find_element(By.XPATH, '//div[contains(text(), "Всё равно продолжить с блокировщиком рекламы")]')
        ad_popup_button.click()
        time.sleep(4)
        return True
    except:
        return False

# логотип программы
def show_logo():
    logo_art = f"""
{Fore.LIGHTRED_EX}
   _____                    _                            __  __  _____ 
  / ____|              /\  | |                          |  \/  |/ ____|
 | |  __  ___ _ __    /  \ | |_ ___ _ __ _ __   ___  ___| \  / | |     
 | | |_ |/ _ \ '_ \  / /\ \| __/ _ \ '__| '_ \ / _ \/ __| |\/| | |     
 | |__| |  __/ | | |/ ____ \ ||  __/ |  | | | | (_) \__ \ |  | | |____ 
  \_____|\___|_| |_/_/    \_\__\___|_|  |_| |_|\___/|___/_|  |_|\_____|
                                                                                                                                        
    """
    for line in logo_art.split('\n'):
        print(line)
        time.sleep(0.2)

# Функция запуска сервера и управления его состоянием
def start_server(session_cookie, server_id, server_ip):
    driver = setup_chrome_driver()
    try:
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Chrome драйвер запущен')
        time.sleep(3)
        driver.get('https://aternos.org/servers/')
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Инициализация сервера...')
        driver.add_cookie({'name': 'ATERNOS_SESSION', 'value': session_cookie})
        driver.add_cookie({'name': "ATERNOS_SERVER", 'value': server_id})
        time.sleep(1)
        driver.get('https://aternos.org/server/')
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Переход на страницу управления сервером')
        driver.refresh()
        handle_ad_popup(driver)
        driver.refresh()
        handle_ad_popup(driver)
        time.sleep(3)
        server_status_element = driver.find_element(By.XPATH,
                                                    '//*[@id="read-our-tos"]/main/section/div[3]/div[2]/div[1]/div/span[1]/span')
        server_status = server_status_element.text

        if "Оффлайн" in server_status:
            print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Сервер {Fore.LIGHTRED_EX}оффлайн{Style.RESET_ALL}, пробуем запустить...')
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="start"]').click()
            print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Сервер {Fore.LIGHTYELLOW_EX}запускается{Style.RESET_ALL}...')
        elif 'Запуск' in server_status:
            time.sleep(3)
            print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Сервер в процессе запуска...')
            time.sleep(35)
            if 'Онлайн' in driver.find_element(By.XPATH, 
                                               '//*[@id="read-our-tos"]/main/section/div[3]/div[2]/div[1]/div/span[1]/span').text:
                print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Сервер {Fore.LIGHTGREEN_EX}онлайн{Fore.LIGHTBLUE_EX}, поддержание соединения...')
                maintain_server_connection(driver)
        elif 'Онлайн' in server_status:
            print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Сервер уже {Fore.LIGHTGREEN_EX}онлайн{Fore.LIGHTBLUE_EX}, поддержание соединения...')
            maintain_server_connection(driver)
    except KeyboardInterrupt:
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Нажата комбинация клавиш CTRL+C, завершение работы...{Style.RESET_ALL}')
    except Exception as e:
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Произошла ошибка: {Fore.LIGHTRED_EX}{e}')
    finally:
        driver.quit()
        driver.close()

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    show_logo()

    # Вывод инструкций по использованию
    print(f"""
{Fore.LIGHTYELLOW_EX}╭─────────────────────────────────━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─────────────────────────────╮
| {Fore.LIGHTGREEN_EX}Использование » {Fore.LIGHTWHITE_EX}python {os.path.basename(__file__)} [session_cookie] [server_id] [server_ip]           {Fore.LIGHTYELLOW_EX}|
| {Fore.LIGHTGREEN_EX}Пример » {Fore.LIGHTBLUE_EX}python {os.path.basename(__file__)} my_cookie my_server_id 192.168.0.1                        {Fore.LIGHTYELLOW_EX}|
| {Fore.LIGHTGREEN_EX}Описание » Скрипт для автоматической загрузки сервера на Aternos                          {Fore.LIGHTYELLOW_EX}|
╰─────────────────────────────────━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─────────────────────────────╯
""")

    log_manager = LogManager()
    config_path = 'config.json'

    # Загрузка конфигурации из JSON-файла
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
        ip_address = config['aternos_server']['ip']
        server_identifier = config['aternos_server']['server_id']
        session_id = config['aternos_server']['session_cookie']

    print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTWHITE_EX}Получен IP: {Fore.LIGHTGREEN_EX}{ip_address}{Style.RESET_ALL}')
    print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTWHITE_EX}Получен идентификатор сервера: {Fore.LIGHTGREEN_EX}{server_identifier}{Style.RESET_ALL}')
    print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenAternosMC {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTWHITE_EX}Получен идентификатор сессии: {Fore.LIGHTGREEN_EX}{session_id}{Style.RESET_ALL}')

    start_server(session_id, server_identifier, ip_address)

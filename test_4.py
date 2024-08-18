import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = "https://www.google.ru/"
driver.get(base_url)
driver.maximize_window()
input_search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@name='q']")))
input_search.send_keys("Byndyusoft")
input_search.send_keys(Keys.RETURN)

"""Выбираем именно первую ссылку и делаем по ней клик"""
url_number1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//h3[contains(text(), 'Byndyusoft')])[1]"))).click()
driver.switch_to.window(driver.window_handles[1])       #переход на новую вкладку
time.sleep(5)                                            #пауза для загрузки стр
get_url1 = driver.current_url
print(f"Текущая url - {get_url1}")
good_url1 = "https://byndyusoft.com/"
try:
    assert get_url1 == good_url1
    print(f"Переход осуществлен верно, текущая url - {good_url1}")
except AssertionError:
    print(f"ОШИБКА!!!! Фактический url - {get_url1} не совпадает с ожидаемым {good_url1}")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")    #скролл к подвалу страницы
element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(), 'Заказать презентацию')])[4]")))
element.click()
print("Элемент найден")

tg_contact = (WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='popup-callback__contacts-tg'])"))))
tg_contact.click()
driver.switch_to.window(driver.window_handles[2])
get_url2 = driver.current_url
print(f"Текущая url - {get_url2}")
good_url2 = "http://t.me/alexanderbyndyu"
print(good_url2)
try:
    assert get_url2 == good_url2
    print(f"Переход осуществлен верно, текущая url - {good_url2}")
except AssertionError:
    print(f"ОШИБКА!!!! Фактический url - {get_url2} не совпадает с ожидаемым {good_url2}")
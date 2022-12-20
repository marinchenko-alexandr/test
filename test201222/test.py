
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestAbs(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("https://goo.su/page/sokratit_ssilku_vk?ysclid=lbwgcqr53d162840628")

    # Тест проверяет, что при переходе по сокращенной ссылке, открывается нужная веб-страница
    def test_link_shortening(self):

        browser = self.browser
    # Находим поле ввода ссылки

        link_input_string = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "long_url_input"))
        )
    # Вводим первоначальную ссылку дял сокращения

        link_input_string.send_keys('www.youtube.com/watch?v=YeIhVHKkoRc')
        link_shortening_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "shorten-it"))
        )
    # Кликаем на кнопку сократить

        link_shortening_button.click()

    # Сохраняем дескриптор первоначального окна браузера

        window_before = browser.window_handles[0]

    # Выбираем сокращенную ссылку и кликаем на нее

        short_link = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id = "user-links"]/div[1]/div/a'))
        )
        short_link.click()
        time.sleep(1)

    # Сохраняем дескриптор вновь открытого окна браузера

        window_after = browser.window_handles[1]
        time.sleep(1)

    # Переключаем на новое окно браузера

        browser.switch_to.window(window_after)

    # Проверяем, что при переходе по сокращенной ссылке открывается нужная веб-страница

        old_url = 'https://www.youtube.com/watch?v=YeIhVHKkoRc'
        new_url = browser.current_url
        assert new_url == old_url
        browser.quit()


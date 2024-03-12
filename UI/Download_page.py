from selenium import webdriver as wd
from selenium.webdriver.common.by import By


class DownloadPage():

    section = {
        'СБИС Отчетность': '[data-id="ereport"]',
        'СБИС Плагин': '[data-id="plugin"]',
        'СБИС Розница': '[data-id="retail"]',
        'СБИС Presto': '[data-id="presto"]',
        'СБИС Киоск': '[data-id="kiosk"]',
        'СБИС Архив': '[data-id="archive"]',
        'Для 1С': '[data-id="1c"]',
        'Удаленный помощник': '[data-id="support"]',
        'Сертификаты ЭП': '[data-id="certificates"]',
        'Средства криптозащиты': '[data-id="crypto"]'
    }

    def __init__(self, driver):
        self.driver = driver

    def select_section(self, name):
        self.driver.find_element(By.CSS_SELECTOR, self.section[name]).click()

    def check_select_section(self, name):
        elem = self.driver.find_element(By.CSS_SELECTOR, self.section[name])
        assert elem.value_of_css_property('border-left-color') == 'rgba(255, 112, 51, 1)', 'Раздел не выбран'
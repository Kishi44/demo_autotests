from selenium import webdriver as wd
from selenium.webdriver.common.by import By


class MainPage():
    driver = wd.Chrome()
    url = 'https://sbis.ru/'

    def open_site(self):
        self.driver.get(self.url)
        assert self.driver.title == 'СБИС — экосистема для бизнеса: учет, управление и коммуникации', 'Не открыли сайт'

    def open_tab(self, tab_name: str):
        self.driver.find_element(By.LINK_TEXT, tab_name).click()
        assert tab_name in self.driver.title, 'Не верная вкладка'


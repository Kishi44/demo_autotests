from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage():
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://sbis.ru/'
        self.wait = WebDriverWait(self.driver, 5)


    def open_site(self):
        self.driver.get(self.url)
        assert self.driver.title == 'СБИС — экосистема для бизнеса: учет, управление и коммуникации', 'Не открыли сайт'

    def open_tab(self, tab_name: str):
        header_menu = self.driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
        self.wait.until(EC.element_to_be_clickable(header_menu))
        self.driver.find_element(By.LINK_TEXT, tab_name).click()
        assert tab_name in self.driver.title, 'Не верная вкладка'


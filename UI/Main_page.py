from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage():
    """
    Главная страница 'https://sbis.ru/'
    """
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://sbis.ru/'
        self.wait = WebDriverWait(self.driver, 5)

    def open_site(self):
        """
        Открытие главно страницы
        """
        self.driver.get(self.url)
        assert self.driver.title == 'СБИС — экосистема для бизнеса: учет, управление и коммуникации', 'Не открыли сайт'

    def open_tab(self, tab_name: str):
        """
        Переход на вкладку на главной странице
        :param tab_name: название вкладки
        """
        header_menu = self.driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
        self.wait.until(EC.element_to_be_clickable(header_menu))
        self.driver.find_element(By.LINK_TEXT, tab_name).click()
        assert tab_name in self.driver.title, 'Не верная вкладка'


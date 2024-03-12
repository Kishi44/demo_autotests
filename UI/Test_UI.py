import allure
from selenium import webdriver
from UI.Main_page import MainPage
from UI.Support_page import SupportPage
from UI.Download_page import DownloadPage


class TestUI:

    page_name = 'Скачать СБИС и дополнительное ПО'

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(driver=self.driver)
        self.support_page = SupportPage(driver=self.driver)


    def test_download_links(self):
        with allure.step('Открываем страницу и переходим на нужную вкладку'):
            self.main_page.open_site()
            self.main_page.open_tab('Поддержка')
        with allure.step('Переходим в раздел для скачивания. проверяем что перешли в нужный раздел'):
            self.support_page.open_downloads_page('Скачать')
            assert self.page_name in self.driver.title, 'Не верная страница'
        with allure.step('Проверяем что на нужном разделе'):
            download_page = DownloadPage(self.driver)
            download_page.check_select_section('СБИС Отчетность')


    def teardown_method(self):
        self.driver.quit()


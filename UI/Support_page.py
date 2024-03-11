from selenium import webdriver as wd
from selenium.webdriver.common.by import By


class SupportPage():
    driver = wd.Chrome()
    downloads_pages_links = driver.find_elements(By.CSS_SELECTOR, '.s-Grid-col [title="Перейти"]')
    support_section = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Support-section')

    def open_downloads_page(self, name: str):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.support_section[1])
        if name == 'Мастер установки':
            self.downloads_pages_links[0].click()
        if name == 'Мобильные приложения':
            self.downloads_pages_links[1].click()
        if name == 'Скачать':
            self.downloads_pages_links[2].click()
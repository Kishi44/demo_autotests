from selenium.webdriver.common.by import By


class SupportPage():

    def __init__(self, driver):
        self.driver = driver

    def open_downloads_page(self, name: str):
        downloads_pages_links = self.driver.find_elements(By.CSS_SELECTOR, '.s-Grid-col [title="Перейти"]')
        support_section = self.driver.find_elements(By.CSS_SELECTOR, '.sbisru-Support-section')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", support_section[1])
        if name == 'Мастер установки':
            downloads_pages_links[0].click()
        if name == 'Мобильные приложения':
            downloads_pages_links[1].click()
        if name == 'Скачать':
            downloads_pages_links[2].click()
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from config.configuration import Configuration


class Cards:

    login_button = "//a[@href='/login'][starts-with(@class, 'Buttonsstyles__Button')]"
    boards_link = "//a[contains(@href, 'boards')]"
    my_board = "//div[@title='MyFirstBoard']"
    add_card = "//a[contains(@class, 'open-card-composer')][1]"
    card_title_input = "//div[contains(@class, 'list-card js-composer')]/div/textarea"
    add_card_button = "//input[contains(@type, 'submit')][contains(@value, 'Add card')]"
    created_card_title_input = "//h2[contains(@id, 'js-dialog-title')]/../textarea"
    exit_card = "//a[contains(@aria-label, 'Close dialog')]"
    confirm_delete_button = "//input[@value = 'Delete']"
    all_cards_list = "//div[starts-with(@class, 'list-cards')][1]/a"

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.configuration = Configuration()

    def go_to_homepage(self):
        url = self.configuration.get_url()
        self.driver.get(url)

    def login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()
        self.driver.find_element(By.NAME, "user").send_keys(self.configuration.get_username())
        self.driver.find_element(By.ID, "login").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "password").send_keys(self.configuration.get_password())
        self.driver.find_element(By.ID, 'login-submit').click()

    def go_to_board(self):
        self.driver.find_element(By.XPATH, self.boards_link).click()
        self.driver.find_element(By.XPATH, self.my_board).click()
        time.sleep(1)

    def create_card(self, card_title):
        self.driver.find_element(By.XPATH, self.add_card).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.card_title_input).send_keys(
            card_title)
        self.driver.find_element(By.XPATH, self.add_card_button).click()

    def edit_card(self, card_title, change):
        self.driver.find_element(By.LINK_TEXT, card_title).click()
        title = self.driver.find_element(By.XPATH, self.created_card_title_input)
        title.click()
        title.clear()
        title.send_keys(change + card_title, Keys.ENTER)
        self.driver.find_element(By.XPATH, self.exit_card).click()

    def delete_card(self, card_title):
        self.driver.find_element(By.LINK_TEXT, card_title).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.LINK_TEXT, 'Archive').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, 'Delete').click()
        self.driver.find_element(By.XPATH, self.confirm_delete_button).click()
        time.sleep(2)

    def get_card_title(self, card_name):
        return self.driver.find_element(By.LINK_TEXT, card_name).text

    def card_deleted(self, card_name):
        all_cards = self.driver.find_elements(By.XPATH, self.all_cards_list)
        for card in all_cards:
            if card.text == card_name:
                return True
        return False

    def __del__(self):
        self.driver.quit()








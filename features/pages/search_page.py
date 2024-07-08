import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from features.environment import write_test_result
import time


class SearchPage:
    def __init__(self, browser):
        self.browser = browser
        self.search_job_input = (By.NAME, "job_search")
        self.search_city_input = (By.NAME, "location[search]")
        self.main_container_xpath = '//*[@id="jobboard-jobboard-0"]/div/div/div[6]/div[1]/div'
        self.container_jobs = './div'
        self.present = (By.XPATH, '//*[@id="tarteaucitronPersonalize2"]')

    def open(self):
        self.browser.get("https://www.alten.es/")

    def click_if_present(self, testName):
        try:
            button = WebDriverWait(self.browser, 1).until(
                EC.element_to_be_clickable(self.present)
            )
            actions = ActionChains(self.browser)
            actions.move_to_element_with_offset(button, -5, 5).perform()
            actions.click().perform()

        except ElementClickInterceptedException:
            logging.error(f'{testName} "Pass" "The user has already accepted the terms and conditions."')
            write_test_result(testName, "Pass", "The user has already accepted the terms and conditions.")

        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f'{testName} "Pass" "The user has already accepted the terms and conditions."')
            write_test_result(testName, "Pass", "The user has already accepted the terms and conditions.")

    def enter_search_term(self, term):
        search_box = WebDriverWait(self.browser, 1).until(
            EC.presence_of_element_located(self.search_job_input)
        )
        search_box.clear()
        search_box.send_keys(term + Keys.RETURN)

    def enter_search_city(self, term):
        search_box = WebDriverWait(self.browser, 1).until(
            EC.presence_of_element_located(self.search_city_input)
        )

        search_box.clear()
        search_box.send_keys(term)

        action = ActionChains(self.browser)
        action.send_keys(Keys.RETURN)

        time.sleep(1)

        action.perform()

    def get_job_offer_elements(self):
        main_container = self.browser.find_element(By.XPATH, self.main_container_xpath)

        child_divs = main_container.find_elements(By.XPATH, self.container_jobs)

        texts = [div.text.replace('\n', ' ').strip().lower() for div in child_divs]

        return texts

    def scroll_to_jobs(self, xpath):
        element = self.browser.find_element(By.XPATH, xpath)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

        self.browser.execute_script("arguments[0].style.border='3px solid red'", element)

    def save_capture(self):
        self.scroll_to_jobs(self.main_container_xpath)

        hora = time.strftime("%Y-%m-%d_%H-%M-%S")

        self.browser.save_screenshot(f'screenshots/screenshot_{hora}.png')

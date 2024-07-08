import csv
from selenium import webdriver
from datetime import datetime
import logging
import logging.config
import os

def write_test_result(test_name, result, error_description=''):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'reports/test_results.csv'
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([test_name, timestamp, result, error_description])

def setup_logging():

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

def before_all(context):
    setup_logging()
    logging.info("Starting test execution")
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()


def after_step(context, step):

    if step.status == 'Status.passed':
        screenshot_path = os.path.join(os.path.dirname(__file__), '..', 'screenshots', ".png")
        context.browser.save_screenshot(screenshot_path)
        logging.error(f"Step failed: {step.exception}")
    else:
        logging.info(f"Step passed")


def after_all(context):
    logging.info("Test execution completed")
    context.browser.quit()
from behave import given, then
from pages.search_page import SearchPage
from features.environment import write_test_result
import logging
import time


def _verify_search_results(context, search_term=None, city=None, testName=None):
    try:
        job_offers = context.search_page.get_job_offer_elements()
        assert job_offers, "No job offers found in the search results"

        for offer in job_offers:
            if search_term:
                assert search_term.lower() in offer, f"term '{search_term.lower()}' not found in '{offer}'"
            if city:
                assert city.lower() in offer, f"city '{city.lower()}' not found in '{offer}'"

        write_test_result(testName, "Pass")
        logging.info(f'{testName} "Pass" ')

    except AssertionError as e:
        logging.error(f'{testName} "Fail" "{e}"')
        write_test_result(testName, "Fail", str(e))
        raise
    except Exception as e:
        logging.error(f'{testName} "Fail" "{e}"')
        write_test_result(testName, "Fail", str(e))
        raise


@given('the user is on "https://www.alten.es/#empleo"')
def access_alten_website(context):
    testName = 'the user is on "https://www.alten.es/#empleo"'
    try:
        context.search_page = SearchPage(context.browser)
        context.search_page.open()
        logging.info(f'{testName} "Pass" ')
        write_test_result(testName, "Pass")
    except Exception as e:
        logging.error(f'{testName} "Pass" "{e}"')
        write_test_result(testName, "Pass", str(e))


@given(u'the user accepts the terms and conditions if they do not exist')
def accept_terms_and_conditions(context):
    testName = 'the user accepts the terms and conditions if they do not exist'
    try:
        time.sleep(3)
        context.search_page.click_if_present(testName)
        logging.info(f'{testName} "Pass" ')
        write_test_result(testName, "Pass")
    except Exception as e:
        logging.error(f'{testName} "Fail" "{e}"')
        write_test_result(testName, "Fail", str(e))


@given('the user writes "{search_term}" in the position or search term field')
def write_search_term(context, search_term):
    testName = f'the user writes "{search_term}" in the position or search term field'
    try:
        context.search_page.enter_search_term(search_term)
        context.search_page.save_capture()
        logging.info(f'{testName} "Pass" ')
        write_test_result(testName, "Pass")
    except Exception as e:
        logging.info(f'{testName} "Pass" ')
        logging.error(f'{testName} "Fail" "{e}"')
        write_test_result(testName, "Fail", str(e))
        raise


@given('the user writes "{city}" in the city or postal code field')
def write_search_term_city(context, city):
    testName = f'the user writes "{city}" in the city or postal code field'
    try:
        context.search_page.enter_search_city(city)
        context.search_page.save_capture()
        logging.info(f'{testName} "Pass" ')
        write_test_result(testName, "Pass")
    except Exception as e:
        logging.error(f'{testName} "Fail" "{e}"')
        write_test_result(testName, "Fail", str(e))
        raise


@then('the table should display job offers that match the search "{search_term}" and "{city}"')
def verify_search_results(context, search_term, city):
    testName = f'the table should display job offers that match the search "{search_term}" and "{city}"'
    _verify_search_results(context, search_term, city, testName)


@then('the table should display job offers that match the search term:"{search_term}"')
def verify_search_results_by_term(context, search_term):
    testName = f'the table should display job offers that match the search term:"{search_term}"'
    _verify_search_results(context, search_term, testName=testName)


@then('the table should display job offers that match the search city:"{city}"')
def verify_search_results_by_city(context, city):
    testName = f'the table should display job offers that match the search city:"{city}"'
    _verify_search_results(context, city=city, testName=testName)

import pytest
from selene.support.shared import browser
from selene import be, have

url = 'https://google.com'
search_input_element = '[name="q"]'
result_element = '[id="search"]'


@pytest.fixture(scope='function', autouse=True)
def config_chrome():
    browser.open(url).driver.set_window_size(600, 600)
    return browser


def check_query(query, expected_result):
    browser.element(search_input_element).should(be.blank).type(query).press_enter()
    browser.element(result_element).should(have.text(expected_result))


def test_positive():
    check_query(query='selene python', expected_result='Selene - User-oriented Web UI browser tests in Python')


def test_negative():
    check_query(query='<<-4341lsdfsdfsdfswer34', expected_result='')

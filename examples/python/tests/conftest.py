import logging
import os
import tempfile
from datetime import datetime

import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def chromedriver_path():
    service = webdriver.chrome.service.Service()
    options = webdriver.ChromeOptions()
    return webdriver.common.driver_finder.DriverFinder().get_path(service=service, options=options)


@pytest.fixture(scope='function')
def log_path():
    suffix = datetime.now().strftime("%y%m%d_%H%M%S")
    log_path = 'log_file_' + suffix + '.log'

    yield log_path

    logger = logging.getLogger('selenium')
    for handler in logger.handlers:
        logger.removeHandler(handler)
        handler.close()

    os.remove(log_path)


@pytest.fixture(scope='function')
def temp_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture(scope='function')
def firefox_driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def log_path():
    suffix = datetime.now().strftime("%y%m%d_%H%M%S")
    log_path = 'log_file_' + suffix + '.log'

    yield log_path

    logger = logging.getLogger('selenium')
    for handler in logger.handlers:
        logger.removeHandler(handler)
        handler.close()

    os.remove(log_path)


@pytest.fixture(scope='function')
def addon_path():
    if os.path.abspath("").endswith("tests"):
        path = os.path.abspath("extensions/webextensions-selenium-example.xpi")
    else:
        path = os.path.abspath("tests/extensions/webextensions-selenium-example.xpi")

    yield path

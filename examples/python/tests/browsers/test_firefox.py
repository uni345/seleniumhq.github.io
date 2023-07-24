import os
import subprocess

import pytest
from selenium import webdriver


def test_basic_options():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)

    driver.quit()


def test_arguments():
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")

    driver = webdriver.Firefox(options=options)
    driver.quit()


@pytest.mark.skip(reason="implemented in 4.11")
def test_log_to_file(log_path):
    service = webdriver.firefox.service.Service(log_path=log_path, service_args=['--log', 'debug'])

    driver = webdriver.Firefox(service=service)
    driver.get("https://www.selenium.dev")

    with open(log_path, 'r') as fp:
        assert "geckodriver	INFO	Listening on" in fp.readline()

    driver.quit()


@pytest.mark.skip(reason="implemented in 4.11")
def test_log_to_stdout(capfd):
    service = webdriver.firefox.service.Service(log_output=subprocess.STDOUT)

    driver = webdriver.Firefox(service=service)

    out, err = capfd.readouterr()
    assert "geckodriver	INFO	Listening on" in out

    driver.quit()


@pytest.mark.skip(reason="broken in 4.10 fixed in 4.11")
def test_log_level(log_path):
    service = webdriver.firefox.service.Service(service_args=['--log', 'debug'])

    driver = webdriver.Firefox(service=service)

    with open(log_path, 'r') as f:
        assert '\tDEBUG' in f.read()

    driver.quit()


@pytest.mark.skip(reason="implemented in 4.11")
def test_log_truncation(log_path):
    service = webdriver.firefox.service.Service(service_args=['--log-no-truncate', '--log', 'debug'], log_path=log_path)

    driver = webdriver.Firefox(service=service)

    with open(log_path, 'r') as f:
        assert ' ... ' not in f.read()

    driver.quit()


def test_profile_location(temp_dir):
    service = webdriver.firefox.service.Service(service_args=['--profile-root', temp_dir])

    driver = webdriver.Firefox(service=service)
    profile_name = driver.capabilities.get('moz:profile').replace('\\', '/').split('/')[-1]

    assert profile_name in os.listdir(temp_dir)

    driver.quit()


def test_install_addon(firefox_driver, addon_path):
    driver = firefox_driver

    driver.install_addon(addon_path)

    driver.get("https://www.selenium.dev/selenium/web/blank.html")
    injected = driver.find_element(webdriver.common.by.By.ID, "webextensions-selenium-example")

    assert injected.text == "Content injected by webextensions-selenium-example"


def test_uninstall_addon(firefox_driver, addon_path):
    driver = firefox_driver

    id = driver.install_addon(addon_path)
    driver.uninstall_addon(id)

    driver.get("https://www.selenium.dev/selenium/web/blank.html")
    assert len(driver.find_elements(webdriver.common.by.By.ID, "webextensions-selenium-example")) == 0


def test_install_unsigned_addon_directory(firefox_driver, addon_path):
    driver = firefox_driver

    driver.install_addon(addon_path, temporary=True)

    driver.get("https://www.selenium.dev/selenium/web/blank.html")
    injected = driver.find_element(webdriver.common.by.By.ID, "webextensions-selenium-example")

    assert injected.text == "Content injected by webextensions-selenium-example"

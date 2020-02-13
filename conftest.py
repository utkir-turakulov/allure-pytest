import pytest
from selenium import webdriver
from selenium.webdriver import Chrome


@pytest.fixture(scope="function")
def setup(request):
    driver = Chrome("drivers/chromedriver.exe")
    request.cls.driver = driver
    yield driver

    driver.quit()


@pytest.fixture(scope="class")
def setup_class(request):
    driver = Chrome("drivers/chromedriver.exe")
    request.cls.driver = driver
    yield driver

    driver.quit()
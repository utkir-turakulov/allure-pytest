import pytest
from selenium import webdriver
from selenium.webdriver import Chrome


@pytest.fixture(scope="function")
def setup(request):
    print (request.fixturename)
    print (request.scope)
    print (request.function.__name__)
    print (request.cls)
    print (request.module.__name__)
    print (request.fspath)
    driver = Chrome("drivers/chromedriver.exe")
    request.driver = driver
    yield driver

    driver.quit()


@pytest.fixture(scope="class")
def setup_class(request):
    print (request.fixturename)
    print (request.scope)
    print (request.function.__name__)
    print (request.cls)
    print (request.module.__name__)
    print (request.fspath)
    driver = Chrome("drivers/chromedriver.exe")
    request.cls.driver = driver
    yield driver

    driver.quit()
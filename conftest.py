import pytest
from selenium import webdriver
from selenium.webdriver import Chrome


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture
def setup(request):
    driver = Chrome("drivers/chromedriver.exe")
    request.cls.driver = driver
    yield driver
    print('результат ',request.node.rep_setup.failed)

    if request.node.setup.failed:
        # Make the screen-shot if test failed:
        try:
            driver.execute_script("document.body.bgColor = 'white';")

            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
            print('made screenshot')
        except:
            pass # just ignore


    # Close browser window:
    driver.quit()


@pytest.fixture(scope="class")
def setup_class(request):
    driver = Chrome("drivers/chromedriver.exe")
    request.cls.driver = driver
    yield driver

    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def test_debug_log(request):
    def test_result():
        if request.node.rep_setup.failed:
            print ("setting up a test failed!", request.node.nodeid)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                print ("executing test failed", request.node.nodeid)
    request.addfinalizer(test_result)
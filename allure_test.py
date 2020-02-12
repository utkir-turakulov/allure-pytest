from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import allure
import pytest




@pytest.mark.usefixtures('setup_class')
class GoogleTests:
    def test_google_1(self):
        driver = self.driver
        driver.get('http://google.com')

    #@pytest.allure.testcase('google test case')
@pytest.mark.usefixtures('setup')
def xtest_google_search():
    #  Открыть браузер
    #print(request)
    
    #  Переход на страницу
    driver.get('https://google.com')
    search_input = driver.find_element_by_name('q')
    #  Ввод текста
    search_input.send_keys('Selenium')
    search_input.submit()
      
    #  Проверка результатов поиска
    search_result = driver.find_elements(
        by=By.CSS_SELECTOR,
        value='#rso .srg div.g'
        )
    assert len(search_result) > 0
    for result in search_result:
        title_text = result.find_element_by_tag_name('h3').text
        assert 'Selenium' in title_text

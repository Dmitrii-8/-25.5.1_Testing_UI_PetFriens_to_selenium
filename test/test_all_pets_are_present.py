import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_are_present(go_to_my_pets):
   '''Проверяем что на странице со списком моих питомцев присутствуют все питомцы'''

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   # В переменную statistic сохраняем элементы статистики
   statistic = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   # Сохраняем в переменную pets элементы карточек питомцев
   pets = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

   # из данных статистики получаем количество питомцев
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   # получаем количество карточек питомцев
   number_of_pets = len(pets)

   # Проверяем, что количество питомцев из статистики совпадает с количеством карточек питомцев
   assert number == number_of_pets


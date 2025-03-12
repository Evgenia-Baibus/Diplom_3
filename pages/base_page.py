import allure
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout = 3):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait_for_element(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys_to_input(self, locator, value):
        self.wait_for_element(locator).send_keys(value)

    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    @allure.step('JS скрипт для метода перетаскивания')
    def drag_and_drop(self, source_locator, target_locator):
        from_element = self.wait_for_element(source_locator)
        to_element = self.wait_for_element(target_locator)

        self.driver.execute_script("""
                const [from_element, to_element] = arguments;
                const dataTransfer = new DataTransfer();
                ['dragstart', 'dragover', 'drop', 'dragend'].forEach(eventType => {
                    const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });
                    (eventType === 'dragstart' ? from_element : to_element).dispatchEvent(event);
                });
            """, from_element, to_element)
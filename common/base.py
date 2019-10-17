from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from random import choice
from time import sleep

def open_browser(browser: str = "chrome"):
    """打开浏览器"""
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()

    elif browser.lower() == "ie":
        driver = webdriver.Ie()

    else:
        print("输入的浏览器名称错误")
        driver = None
        return driver

    return driver


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    # 打开网址
    def get_url(self, url):
        self.driver.get(url)


    # 退出浏览器
    def quit(self):
        self.driver.quit()

    # 定位单个元素
    def __find_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    # 定位多个元素
    def __find_elements(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    # 判断文本是否包含于元素
    def is_text_in_element(self, locator, text, timeout=5):
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    # 判断value是否包含于元素value
    def is_value_in_element(self, locator, value, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(locator, value))
        except:
            return False

    # 点击元素
    def click(self, locator):
        element = self.__find_element(locator)
        element.click()

    # 点击多个元素中的某一个
    def click_one_in_elements(self, locator, index):
        self.__find_elements(locator)[index-1].click()

    # 元素输入
    def send_keys(self, locator, text):
        element = self.__find_element(locator)
        ActionChains(self.driver).double_click(element).perform()
        element.clear()
        element.send_keys(text)

    # 判断元素是否已选
    def ele_is_selected(self, locator):
        try:
            result = self.__find_element(locator).is_selected()
            if result:
                return result
        except:
            return False

    # 确认弹窗
    def accept_alert(self, text="你确认要删除该收货地址吗？"):
        assert self.driver.switch_to.alert.text == text
        sleep(1)
        self.driver.switch_to.alert.accept()

    # 获取重名标签的个数
    def get_length_of_elements(self, locator):
        length = len(self.__find_elements(locator))
        return length

    # 鼠标悬停
    def move_to_element(self, locator):
        self.driver.move_to_element(self.__find_element(locator))

    # 通过选项顺序选择下拉菜单选项
    def select_by_num(self, locator):
        selects = self.__find_elements(locator)
        del selects[0]
        select = choice(selects)
        select.click()
        sleep(1)


    # 聚焦元素
    def focus_element(self, locator):
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, self.__find_element(locator))


if __name__ == '__main__':
    """测试代码"""
    from time import sleep

    base = Base(open_browser())
    base.get_url("http://192.168.244.130/ecshop/user.php?act=address_list")
    base.send_keys(("name", "username"), "admin")
    base.send_keys(("name", "password"), "123456")
    base.click(("class name", "us_Submit"))
    # select = base.get_length_of_elements(("css selector", "#selCountries_0"))
    # print(base._Base__find_element(("css selector", "#selCountries_3")).get_attribute("outerHTML"))
    sleep(3)
    print(base.is_text_in_element(("class name", "f4_b"), "admin"))

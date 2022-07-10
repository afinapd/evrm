from selenium.webdriver.common.by import By
class Locator:
    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector

    def parameterize(self, *args):
        self.selector = self.selector.format(*args)

class LocatorDashboardPage:
    SIGNIN_BUTTON = Locator(By.LINK_TEXT, "Masuk")

class LocatorSignInPage:
    NOHP_TEXTFIELD = Locator(By.XPATH, "//div[@id='__layout']/div/div/form/label/span[2]/input")
    PASSWORD_TEXTFIELD = Locator(By.XPATH, "//div[@id='__layout']/div/div/form/label[2]/span[2]/input")
    SIGNIN_BUTTON = Locator(By.XPATH, "//button[contains(.,'Masuk')]")

class LocatorHomePage:
    BERANDA_NAVBAR = Locator(By.XPATH, "//span[contains(.,'Beranda')]")
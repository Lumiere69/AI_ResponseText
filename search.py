import time
from selenium import webdriver
class Parser:
    def google_parser(self, massive):
        url = [f"https://www.google.com/search?q={el}&ref=opensearch" for el in massive]
        driver = webdriver.Chrome(
            executable_path=r"C:\final_prj\chromedriver.exe")

        try:
            for i, u in enumerate(url):
                driver.get(url=u)
                driver.save_screenshot(f"screen/url{i}_g.png")

        except Exception as ex:
            print(ex)

        finally:
            driver.close()
            driver.quit()
    def bing_parser(self, massive):
        url = [f"https://www.bing.com/search?q={el}&ref=opensearch" for el in massive]
        driver = webdriver.Chrome(
            executable_path=r"C:\final_prj\chromedriver.exe")

        try:
            for i, u in enumerate(url):
                driver.get(url=u)
                driver.save_screenshot(f"screen/url{i}_b.png")

        except Exception as ex:
            print(ex)

        finally:
            driver.close()
            driver.quit()
    def yandex_parser(self, massive):
        url = [f"https://www.yandex.ru/search/?text={el}&ref=opensearch" for el in massive]
        driver = webdriver.Chrome(
            executable_path=r"C:\final_prj\chromedriver.exe")

        try:
            for i, u in enumerate(url):
                driver.get(url=u)
                driver.save_screenshot(f"screen/url{i}_y.png")

        except Exception as ex:
            print(ex)

        finally:
            driver.close()
            driver.quit()
    def duckgo_parser(self, massive):
        url = [f"https://duckduckgo.com/?q={el}&ref=opensearch" for el in massive]
        driver = webdriver.Chrome(
            executable_path=r"C:\final_prj\chromedriver.exe")

        try:
            for i, u in enumerate(url):
                driver.get(url=u)
                driver.save_screenshot(f"screen/url{i}_d.png")

        except Exception as ex:
            print(ex)

        finally:
            driver.close()
            driver.quit()
    def mailru_parser(self, massive):
        url = [f"https://go.mail.ru/search?q={el}&ref=opensearch" for el in massive]
        driver = webdriver.Chrome(
            executable_path=r"C:\final_prj\chromedriver.exe")

        try:
            for i, u in enumerate(url):
                driver.get(url=u)
                driver.save_screenshot(f"screen/url{i}_m.png")

        except Exception as ex:
            print(ex)

        finally:
            driver.close()
            driver.quit()
    def all(self, massive):
        self.google_parser(massive)
        self.bing_parser(massive)
        self.yandex_parser(massive)
        self.duckgo_parser(massive)
        self.mailru_parser(massive)

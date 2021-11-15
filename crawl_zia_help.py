import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.relative_locator import locate_with

# Driver init config
options = Options()
# options.add_argument("-headless")

# driver: webdriver = webdriver.Firefox(options=options)
driver: webdriver = webdriver.Firefox()


def crawl_certificate_pinning_ssl_inspection(driver: webdriver) -> None:
    driver.get("https://help.zscaler.com/zia/certificate-pinning-and-ssl-inspection")
    # row_group = driver.find_elements(locate_with(By.CLASS_NAME, "article-page"))
    # for row in row_group:
    #     print(row.text)

    # driver.find_element(
    #     locate_with(By.XPATH, '//*[@id="ag-4"]/span[2]/div[3]')
    #     # locate_with(By.CLASS_NAME, "optanon-alert-box-bottom-top")
    # ).click()

    time.sleep(2)
    # row_group = driver.find_elements(locate_with(By.CLASS_NAME, "z-custom-grid"))
    row_group = driver.find_elements(locate_with(By.CLASS_NAME, "ag-body-viewport"))

    for row in row_group:
        print(row.text)

    time.sleep(3)

    test = driver.find_elements(locate_with(By.CLASS_NAME, "ag-paging-button"))
    [print(row) for row in test]

    # ag-paging-button


if __name__ == "__main__":
    crawl_certificate_pinning_ssl_inspection(driver)
    driver.quit()

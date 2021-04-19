from selenium import webdriver
from selenium.webdriver.common.by import By


def test_addmember():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.find_element_by_id("menu_contacts").click()
    # ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    # print(*ele)
    # WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable(ele))
    # driver.find_element_by_css_selector(".ww_operationBar .js_add_member").click()
    while True:
        # 解元组
        # driver.find_element(*ele).click()
        driver.find_element_by_css_selector(".ww_operationBar .js_add_member").click()
        ele_num = len(driver.find_elements(By.ID, "username"))
        if ele_num > 0:
            break
    driver.find_element(By.ID, "username").send_keys("zhangsan01")
    driver.find_element(By.ID, "memberAdd_acctid").send_keys("041901")
    driver.find_element(By.ID, "memberAdd_phone").send_keys("18800000000")
    driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()

    ele_phones = driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
    for value in ele_phones:
        if value.get_attribute("title") == "18800000000":
            return True

import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()

driverFile_path = r'D:\application\edgedriver_win64\msedgedriver.exe'
driver = webdriver.Edge(executable_path=driverFile_path)
# 这行代码的作用是将webdriver这个属性置为undefined
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                       {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
                       )

driver.get(r'https://www.wjx.top/vm/hJzQinm.aspx')
driver.implicitly_wait(10)
driver.maximize_window()

actions = webdriver.ActionChains(driver)

input1 = driver.find_element(by=By.NAME, value="q1")
input1.send_keys('欧光业')

for i in range(3, 5):
    my_input = Select(driver.find_element(by=By.NAME, value='q' + str(i)))
    my_input.select_by_index(1)

input5 = driver.find_element(by=By.NAME, value='q5')
input5.send_keys('202030430134')

input5 = driver.find_element(by=By.NAME, value='q6')
input5.send_keys('13414970411')

input2 = driver.find_element(by=By.NAME, value="q2")
input2.click()

time.sleep(1)

iframe = driver.find_element(by=By.ID, value='layui-layer1')
# driver.switch_to.frame(iframe)

input2_hidden1 = driver.find_element(by=By.XPATH,
                                     value="/html/body/div[3]/div[2]/div/div/div[1]/div/select")
Select(input2_hidden1).select_by_index(2)

input2_hidden2 = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div/div[2]/div/select')
Select(input2_hidden2).select_by_index(15)

input2_hidden_button = driver.find_element(by=By.CLASS_NAME, value='button_a')
input2_hidden_button.click()

submit_button = driver.find_element(by=By.ID, value='ctlNext')
submit_button.click()

# 后面可能会存在智能验证码进行验证
sleep(1)
test_button = driver.find_element(by=By.CLASS_NAME, value='layui-layer-btn0')
test_button.click()

verify_button = driver.find_element(by=By.ID, value='SM_BTN_WRAPPER_1')
verify_button.click()

# sleep(3)

# driver.quit()

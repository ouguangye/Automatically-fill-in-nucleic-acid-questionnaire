from time import sleep
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# 读取配置文件的信息
config = configparser.ConfigParser()
config.read('config.ini',encoding="utf-8")


# 忽略无用的日志
options = webdriver.EdgeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

# 这里可以选择自己合适的浏览器驱动， 我这里选择的是Edge Driver
driverFile_path = config.get('info','broswersDriverPath')
print("path", driverFile_path)
driver = webdriver.Edge(executable_path=driverFile_path)

# 这行代码的作用是将webdriver这个属性置为undefined， 避免验证失败
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                       {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
                       )

driver.get(r'https://www.wjx.top/vm/hJzQinm.aspx')
driver.implicitly_wait(10)
driver.maximize_window()

# 输入姓名
name = driver.find_element(by=By.NAME, value="q1")
name.send_keys(config.get('info','name'))

# 选择类别， 1： 本科生
type = Select(driver.find_element(by=By.NAME, value='q3'))
type.select_by_index(int(config.get('info','type')))


# 选择常住校区
loc = Select(driver.find_element(by=By.NAME, value='q3'))
loc.select_by_index(int(config.get('info','residentCampus')))


# 输入学号
student_number = driver.find_element(by=By.NAME, value='q5')
student_number.send_keys(config.get('info','studentNumber'))

# 输入手机号
input5 = driver.find_element(by=By.NAME, value='q6')
input5.send_keys(config.get('info','phoneNumber'))


'''
    选择单位, 点击之后会出现弹窗，选择 单位类型 和  单位部门， 最后点击确认按钮
'''
input2 = driver.find_element(by=By.NAME, value="q2")
input2.click()

# 等待 弹窗出来
sleep(1)

# 选择单位类型 2： 院系
organization_type = driver.find_element(by=By.XPATH,
                                     value="/html/body/div[3]/div[2]/div/div/div[1]/div/select")
Select(organization_type).select_by_index(int(config.get('info','organizationType')))


# 选择单位名称， 15: 计算机科学与工程学院
organization_name = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div/div[2]/div/select')
Select(organization_name).select_by_index(int(config.get('info','organizationName')))

input2_hidden_button = driver.find_element(by=By.CLASS_NAME, value='button_a')
input2_hidden_button.click()

# 点击提交按钮
submit_button = driver.find_element(by=By.ID, value='ctlNext')
submit_button.click()

# 后面可能会存在智能验证码进行验证
sleep(1)
test_button = driver.find_element(by=By.CLASS_NAME, value='layui-layer-btn0')
test_button.click()
verify_button = driver.find_element(by=By.ID, value='SM_BTN_WRAPPER_1')
verify_button.click()

sleep(3)
driver.quit()
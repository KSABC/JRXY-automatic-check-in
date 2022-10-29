# coding:utf-8
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import logging
import time
'''
这里用selenium库的By的方法选择元素
但最好还是用appium库的By方法。
'''

desired_caps = {
  'platformName': 'Android',
  'platformVersion': '11',
  'deviceName': 'xxx',
  'appPackage': 'com.wisedu.cpdaily',
  'appActivity': 'com.wisorg.wisedu.login.WelcomeActivity',
  'unicodeKeyboard': True,
  'resetKeyboard': True,
  'noReset': True,
  'newCommandTimeout': 6000,
  'automationName': 'UiAutomator2',
  'unlockType': 'password',
  'unlockKey': '123456',
  'autoGrantPermissions': True
}
# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

logger = logging.getLogger('签到记录')
handler = logging.FileHandler('签到记录本')
formatter = logging.Formatter('%(asctime)s   %(name)s   %(levelname)s   %(message)s   %(lineno)d')
handler.setLevel(level=logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)


def execute_process():
    try:
        driver.implicitly_wait(20)
        fir_step = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/androidx.appcompat.widget.LinearLayoutCompat[1]/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView")
        fir_step.click()
        driver.implicitly_wait(20)
        sec_step = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]')
        sec_step.click()
        thi_step = WebDriverWait(driver, 20).until(lambda _: driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.Image[2]'))
        thi_step.click()
        driver.implicitly_wait(20)
        final_step = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.app.Dialog/android.view.View[4]/android.widget.Button[2]')
        final_step.click()
        logger.info('签到成功！')
        global a
        a = 0
    except:
        logger.error('签到失败，等待下次重试。')
        time.sleep(300)
        execute_process()


a = 1
while not not a:
    execute_process()


driver.quit()

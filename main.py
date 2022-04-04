from lib2to3.pgen2 import driver

from appium import webdriver

import pytest
from appium.webdriver.common.appiumby import AppiumBy

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "8.1"
caps["browserName"] = ""
caps["appium:appiumVerson"] = "1.22.0"
caps["appium:deviceName"] = "Samsung Galaxy S9 Plus FHD GoogleAPI Emulator"
caps["appium:deviceOrientation"] = "portrait"
caps["appium:app"] = "storage:filename= Calculator_v8.1 (403424005)_apkpure.com .apk"
caps["appium:appPackage"] = "com.google.android.calculator"
caps["appium:appActivity"] = "com.android.calculator2.Calculator"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["sauce:options"] = {"name":"Appium Desktop Session -- Apr 3, 2022 9:58 PM"}
caps["appium:newCommandTimeout"] = 0
caps["appium:connectHardwareKeyboard"] = True

if __name__ == '__main__':
    #def testar_somar_dois_numeros():

    driver = webdriver.Remote("https://oauth-brian.saggini-e0e67:2ed4a561-2547-4de0-9ec4-f05b3dd9feea@ondemand.us-west-1.saucelabs.com:443/wd/hub", caps)

    resultado_esperado = '13'

    botao_8 = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_8")
    botao_8.click()
    botao_somar = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="plus")
    botao_somar.click()
    botao_5 = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_5")
    botao_5.click()
    botao_igual = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="equals")
    botao_igual.click()
    resultado_final = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/result_final")
    print(f'resultado final = {resultado_final.text} \n resultado esperado = {resultado_esperado}')
    assert resultado_final.text == resultado_esperado

    driver.quit()
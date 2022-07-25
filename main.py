# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time, urllib
options = Options()
options.add_argument('--headless')
voicerlist = """0 四国めたん(あまあま)
1 ずんだもん(あまあま)
2 四国めたん(ノーマル)
3 ずんだもん(ノーマル)
4 四国めたん(セクシー)
5 ずんだもん(セクシー)
6 四国めたん(ツンツン)
7 ずんだもん(ツンツン)

無能過ぎて疲れて書く気力失った"""
def yomu(outputword):
    driver = webdriver.Chrome(options=options)
    driver.get("https://voicevox.su-shiki.com/vertical/")
    dropdown = driver.find_element_by_name("speaker")
    select = Select(dropdown)
    aaa = input("番号:")
    select.select_by_value(aaa)
    word = outputword
    element = driver.find_element_by_xpath("/html/body/form/span/a[2]")
    aTag    = element.find_element_by_tag_name("a")
    url     = aTag.get_attribute("href")
    driver.quit()
    return url
a = yomu("こんにちは")
print(a)

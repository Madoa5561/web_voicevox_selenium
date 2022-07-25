
#WindowsでSeleniumを動かすまでの手順
#Step１
#Pythonをインストールします。
#Pythonの公式サイトからPythonをダウンロードしてインストールします。
#
#Step２
#Seleniumをインストールします。
#コマンドプロンプトを立ち上げて、以下を実行します。
#
#pip install selenium
#Step３
#Seleniumからブラウザ（Chrome）を操作するためのドライバーをダウンロードし、パスを通します。
#ChromeDriverの公式サイトからChromeDriver 73.0.3683.68をダウンロードします。
#
#ダウンロードしたzipファイルを解凍します。
#
#適当な場所にzipの中にあるexeファイルを置きます(例：C:\Program Files\chromedriver)。
#
#「環境変数を編集」を実行して(Winキーを押して「環境変数を編集」と検索すれば出てきます)、「Path」に上記のフォルダを追加します。
#
#コマンドプロンプトを起動し、以下のコマンドを実行して、起動できればOKです。
#
#> chromedriver
#Starting ChromeDriver 73.0.3683.68 (47787ec04b6e38e22703e856e101e840b65afe72) on port 9515
#Only local connections are allowed.
#Please protect ports used by ChromeDriver and related test frameworks to prevent access by malicious code.

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

あとは自分で書いてくれ"""
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

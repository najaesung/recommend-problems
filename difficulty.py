from asyncio.windows_events import NULL
from types import NoneType
import pymysql
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup as bs

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)


db=pymysql.connect(host='localhost',port=3306,user='root',passwd='0000',db='recodb',charset='utf8')
cursor=db.cursor()

sql=f"select code,group_concat(tag separator', ') as tag from problems group by code order by id ;"
cursor.execute(sql)
result=cursor.fetchall()


for count,element in enumerate(result):
    code=element[0]
    driver.get("https://www.codechef.com/problems/"+code)
    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/span[2]'))
    )
    html=driver.page_source
    soup=bs(html,'html.parser')
    try:
        diff=soup.select_one('#root > div > div._pageContainer_x1ji1_2 > div > div > div._problem-banner__container_bvg0e_387 > div._navigate-button__container_bvg0e_450 > div._navigation-left-wrapper_bvg0e_459 > div._difficulty-ratings__box_bvg0e_516 > span._value_bvg0e_521').get_text()
    except:
        diff=soup.select_one('#root > div > div._pageContainer_x1ji1_2 > div > div > div._problem-banner__container_bvg0e_387 > div._navigate-button__container_bvg0e_450 > div._navigation-left-wrapper_bvg0e_459 > div._difficulty-ratings__box_bvg0e_516 > span._value_bvg0e_521').get_text()
    print(code,diff,count)
    sql="update problems set difficulty = %s where code = %s"
    data=(diff,code)
    cursor.execute(sql,data)
    db.commit()

db.commit()
db.close()
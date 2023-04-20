
from collections import defaultdict
from types import NoneType
import pymysql
import time
import matplotlib.pyplot as plt
import math
tag_dict={}
prob_dict=defaultdict(list)
f=open('tag.txt','a',encoding='UTF-8')
db=pymysql.connect(host='localhost',port=3306,user='root',passwd='0000',db='recodb',charset='utf8')
cursor=db.cursor()
diff=[]
sql=f"select code,tag from tmp;"
cursor.execute(sql)
result=cursor.fetchall()


for idx,res in enumerate(result):
    full_tag=res[1]
    tag=res[1].split(' ')
    code=res[0]
    tmp=''
    print(code, tag)
    for word in tag:
        tmp=tmp+' '+word.capitalize()
    
    sql=f"update tmp set tag=\"{tmp[1:]}\" where code=\"{code}\" and tag=\"{full_tag}\";"
    
    cursor.execute(sql)
    if(idx%100==0):
        print(idx)
db.commit()
db.close()

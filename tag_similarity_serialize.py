from collections import defaultdict
from dis import code_info
from turtle import color
from types import CodeType, NoneType
import pickle
import pymysql
from openpyxl import load_workbook
import random
code_index=defaultdict(int)
code_tagsim=defaultdict(list)
db=pymysql.connect(host='localhost',port=3306,user='root',passwd='0000',db='recodb',charset='utf8')
cursor=db.cursor()
min=3500



with open (file="code_code_tagsim_sorted.pickle",mode="rb") as f:
    code_tagsim=pickle.load(f)


for idx,(code,list) in enumerate(code_tagsim.items()):
    max=0
    length=len(list)
    #finding the max index where similarity is 0
    for index,item in enumerate(list):
        if item[1]>0:
            max=index-1
            break
    
    count=0
    i=1
    #saving most similar 5 problems to the DB
    while True:
        if count==5:
            break
        if list[length-i][0]==code:
            i+=1
        else:
            sql="insert into tag_sim (pcode,ccode,similar) values (%s,%s,%s)"
            values=(code,list[length-i][0],"yes")
            cursor.execute(sql,values)
            count+=1
            i+=1
    #saving random 200 problems which have similarity 0 to the DB
    index_list = random.sample(range(0,max),200)
    for i in index_list:
        sql="insert into tag_sim (pcode,ccode,similar) values (%s,%s,%s)"
        values=(code,list[i][0],"no")
        cursor.execute(sql,values)
    print("idx: ",idx)
    

db.commit()




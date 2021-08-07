# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 09:06:33 2021

@author: JU-HUA
"""
import pandas as pd
# import numpy as np
#数据加载
df=pd.read_csv('./car_complain.csv')
# print(df)
# df.to_excel('./car_complain.xlsx',index=False)
df=df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))
df.to_excel('./car_complain.xlsx',index=False)
# print(df)

#按品牌统计
#用自定义函数进行数据清洗,将别名合并
def f(x):
    x=x.replace('一汽-大众','一汽大众')
    return x
df['brand']=df['brand'].apply(f)

#按照brand统计 投诉总数
result=df.groupby(['brand'])['id'].agg(['count'])
# df.to_excel('./car_complain1.xlsx',index=False)
print(result)
# print(df.columns)

#不同problem类型的总数
tags=df.columns[7:]
result2=df.groupby(['brand'])[tags].agg(['sum'])
# df.to_excel('./car_complain1.xlsx',index=False)
print(result2)

#按照投诉总数进行排序result2
result2=result.merge(result2,left_index=True,right_index=True,how='left')
print(result2)

#恢复result2索引
result2.reset_index(inplace=True)
result2
print(result2)

#按照车型统计 投诉总数
result3=df.groupby(['car_model'])['id'].agg(['count'])
# df.to_excel('./car_complain1.xlsx',index=False)
print('按车型统计',result3)
result3=result3.sort_values('count',ascending=False)
result3.to_excel("./car_model_analyse_result.xlsx")
# print(df.columns)

result4=df.groupby(['brand','car_model'])['id'].agg('count')
print (result4)

#按照count,从大到小进行排序ascending=False,True从小到大
result2=result2.sort_values('count',ascending=False)
print(result2)
result2.to_excel("./result1.xlsx")

# query=('A11','sum')
# print(result2.sort_values(query,ascending=False))







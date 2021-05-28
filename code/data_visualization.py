#######################################
#    School of Software Technology    #
#   Dalian University of Technology   #
#             yang lifan              #
#          2862506026@qq.com          #
#######################################
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

pr=pd.read_csv("E:\大二下\人工智能基础\crawl\lol\data\clean_lol_role_data_length.csv")
pr.columns = [ 'heroId','name','alias','title','roles','attack', 'defense', 'magic', 'difficulty','couponPrice','goldPrice','isWeekFree']
# print(pr)

''' *—————— 统计职业比例—————— * '''
fighter=0# 战士==0
mage=0# 法师==1
tank=0# 坦克==2
assassin=0# 刺客==3
support=0# 辅助==4
marksman=0# adc==5

# 统计不同职业数量
for roles in pr['roles']:
    if roles==0:
        fighter+=1
    elif roles==1:
        mage+=1
    elif roles==2:
        tank+=1
    elif roles==3:
        assassin+=1
    elif roles==4:
        support+=1
    elif roles==5:
        marksman+=1
# 绘制饼状图 
labels=['FIGHTER','MAGE','TANK','ASSASSIN','SUPPORT','MARKSMAN']
# 绘图显示的标签
values=[fighter,mage,tank,assassin,support,marksman]
colors=['y','m','b','r','g','deeppink']
explode=[0.1,0.1,0.1,0.1,0.1,0.1]
plt.title("Roles ratio",fontsize=25)
plt.pie(values,labels=labels,explode=explode,colors=colors,
        startangle = 180,
        shadow=True,autopct='%1.1f%%')
plt.axis('equal')
plt.savefig('E:\\大二下\\人工智能基础\\crawl\\lol\\pic\\roles_ratio.png')
plt.show()

''' **—————— 统计上手难度 ——————** '''
df = pd.read_csv("E:\大二下\人工智能基础\crawl\lol\data\clean_lol_role_data.csv")
df.columns = [ 'heroId','name','alias','title','attack', 'defense', 'magic', 'difficulty','couponPrice',
               'goldPrice','isWeekFree','marksman','tank','mage','fighter','assassin','support']
s=0
a=0
b=0
c=0
d=0
for i in df['difficulty']:
    if i==10 or i==9:
        s+=1
    elif i==8 or i==7:
        a+=1
    elif i==6 or i==5:
        b+=1
    elif i==4 or i==3:
        c+=1
    else:
        d+=1
# 绘图
index=['S','A','B','C','D']
values=[s,a,b,c,d]
plt.title("difficulty distribution",fontsize=25)
plt.bar(index,values)
plt.savefig('E:\\大二下\\人工智能基础\\crawl\\lol\\pic\\diff_distribution.png')
plt.show()

''' ***—————— 不同职业攻击力和物抗关系 ——————*** '''
data = pd.read_csv("E:\\大二下\\人工智能基础\\crawl\\lol\\data\\roles.csv")
data.columns = [ 'roles','attack', 'defense', 'magic', 'difficulty']
plt.title("attack and defense",fontsize=25)
sns.lineplot(x="attack",y="defense",hue='roles',data=data)
plt.savefig('E:\\大二下\\人工智能基础\\crawl\\lol\\pic\\attack_and_defense.png')
plt.show()

#######################################
#    School of Software Technology    #
#   Dalian University of Technology   #
#             yang lifan              #
#          2862506026@qq.com          #
#######################################
import numpy as np
import pandas as pd

df = pd.read_excel(r"lol\data\first_lol_role_data.xls")

''' *—————— 处理一英雄多角色的第一种方法——将一列变多列 ——————* '''
temp_list = [eval(x) for x in  df["职业"].tolist()]  
tag_all =  set([j for i in temp_list for j in i])  
print(tag_all)

zeros_data = pd.DataFrame(np.zeros((df.shape[0], len(tag_all))), columns=list(tag_all))
for i in range(df.shape[0]):
    zeros_data.loc[i, temp_list[i]] = 1
data = pd.concat([df, zeros_data], axis=1).drop(labels="职业", axis=1)
data.to_csv("lol\\data\\clean_lol_role_data.csv",index=False)


''' **—————— 处理一英雄多角色的第二种方法——将一行变多行 ——————** '''
df.head()
df['职业']=df['职业'].map(lambda x:x.split(','))
df_new=df.explode('职业')
# 建立字典
roles_mapping = {'战士':0 ,'法师':1 , '坦克':2 ,'刺客':3 ,'辅助':4 ,'ADC':5,
                ' 战士':0 ,' 法师':1 , ' 坦克':2 ,' 刺客':3 ,' 辅助':4 ,' ADC':5}
# 替换特殊字符    
df_new['职业'] = df_new['职业'].str.replace("'","")
df_new['职业'] = df_new['职业'].str.replace("[","")
df_new['职业'] = df_new['职业'].str.replace("]","")
# 替换
df_new['职业'] = df_new['职业'].map(roles_mapping)
df_new.to_csv("lol\\data\\clean_lol_role_data_length.csv",index=False)


''' ***—————— 方便机器学习分析进行的数据清洗 ——————***'''
# print(df_new)
# 去除不要的数据
df_new = df_new.drop(columns = ['编号'])
df_new = df_new.drop(columns = ['名称'])
df_new = df_new.drop(columns = ['英文名'])
df_new = df_new.drop(columns = ['中文名'])
df_new = df_new.drop(columns = ['点卷价格'])
df_new = df_new.drop(columns = ['蓝色精粹'])
df_new = df_new.drop(columns = ['周免'])
# 建立字典
roles_mapping = {0:'fighter' ,1:'mage' , 2:'tank' ,3:'assassin' ,4:'support' ,5:'marksman'}
# 替换
df_new['职业'] = df_new['职业'].map(roles_mapping)
df_new.to_csv("lol\\data\\roles.csv", index=False, header=False)


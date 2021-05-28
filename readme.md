#### 一、 code

 此文件夹内为全部代码

1. ###### crawl_lol.py 

   1. 此文件为爬虫部分全部代码
   2. 主要功能：爬取了官网的英雄的信息
   3. 生成一个xls文件：
      1. first_lol_role_data.xls

2. data_wash.py

   1. 此文件为数据清洗全部代码
   2. 主要功能：将爬虫得到的原始数据编码成方便计算的csv文件
   3. 共生成三个csv文件：
      1. clean_lol_role_data.csv
      2. clean_lol_role_data_length.csv
      3. roles.csv                                  

3. data_visualization.py

   1. 此文件为数据可视化代码
   2. 主要功能：对清洗后的数据进行可视化分析
   3. 生成饼状图一张，柱形图一张和折线图一张:
      1. roles_ratio.png
      2. diff_distribution.png
      3. attack_and_defense.png

4. classification.py

   1. 此文件：使用决策树对不用职业进行分类
   2. 主要功能：
      1. 对roles.csv数据可视化
      2. 对roles.csv数据中不同的职业进行分类
      3. 生成决策树
   3. 生成决策树图一张及数据散点图：
      1.  roles_dataset.png
      2. roles_dtc.png

#### 二、data

此文件内为全部的数据

1. first_lol_role_data.xls

   爬虫得到的第一数据

2. clean_lol_role_data.csv

   处理一英雄多角色的第一种方法——将一列变多列

3. clean_lol_role_data_length.csv

   处理一英雄多角色的第二种方法——将一行变多行

4. roles.csv 

   1. 在clean_lol_role_data_length.csv基础上，方便机器学习分析进行的数据清洗
   2. 主要借鉴了iris数据集格式

#### 三、pic

 此文件夹内为全部的可视化图片

1. roles_ratio.png

   统计职业比例

2. diff_distribution.png

   统计上手难度

3. roles_dataset.png

   分析使用数据集散点图

4. roles_dtc.png

   决策树图

5. attack_and_defense.png

   不同职业攻击力和物抗关系折线图

#### 四、注意
如有人使用，请将代码中的路径更改好。

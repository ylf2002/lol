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

#### 四：crawl_baidubaike_version

1. 最初的第一版爬虫，爬取百度百科页面版本
2. 写到一半，作废

#### 五：参考

1. https://blog.csdn.net/New_Yao/article/details/104633562
2. https://blog.csdn.net/y1534414425/article/details/107247322/?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_utm_term-1&spm=1001.2101.3001.4242
3. https://blog.csdn.net/qq_42768234/article/details/104355755?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_utm_term-1&spm=1001.2101.3001.4242
4. [https://blog.csdn.net/badder2/article/details/85089328?ops_request_misc=&request_id=&biz_id=102&utm_term=csv%E6%95%B0%E6%8D%AE%E5%8F%AF%E8%A7%86%E5%8C%96%E7%94%BB%E6%9F%B1%E5%BD%A2%E5%9B%BE&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-9-85089328.first_rank_v2_pc_rank_v29&spm=1018.2226.3001.4187](https://blog.csdn.net/badder2/article/details/85089328?ops_request_misc=&request_id=&biz_id=102&utm_term=csv数据可视化画柱形图&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-9-85089328.first_rank_v2_pc_rank_v29&spm=1018.2226.3001.4187)
5. [https://blog.csdn.net/badder2/article/details/85095631?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-3.baidujs&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-3.baidujs](https://blog.csdn.net/badder2/article/details/85095631?utm_medium=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromMachineLearnPai2~default-3.baidujs&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromMachineLearnPai2~default-3.baidujs)
6. [https://blog.csdn.net/qq754772661/article/details/107206123?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161977933116780271591515%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=161977933116780271591515&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v29-1-107206123.first_rank_v2_pc_rank_v29&utm_term=%E7%87%95%E5%B0%BE%E8%8A%B1%E6%95%B0%E6%8D%AE%E5%88%86%E7%B1%BB%E5%8F%8A%E5%8F%AF%E8%A7%86%E5%8C%96&spm=1018.2226.3001.4187](https://blog.csdn.net/qq754772661/article/details/107206123?ops_request_misc=%7B%22request%5Fid%22%3A%22161977933116780271591515%22%2C%22scm%22%3A%2220140713.130102334.pc%5Fall.%22%7D&request_id=161977933116780271591515&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v29-1-107206123.first_rank_v2_pc_rank_v29&utm_term=燕尾花数据分类及可视化&spm=1018.2226.3001.4187)
7. https://blog.csdn.net/ABin_203/article/details/105992098?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_utm_term-0&spm=1001.2101.3001.4242
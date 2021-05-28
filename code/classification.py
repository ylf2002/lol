#######################################
#    School of Software Technology    #
#   Dalian University of Technology   #
#             yang lifan              #
#          2862506026@qq.com          #
#######################################
import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn import tree

# 读入数据
roles = pd.read_csv('E:\\大二下\\人工智能基础\\crawl\\lol\\data\\roles.csv')
# 给每列命名
roles.columns = [ 'roles','attack', 'defense', 'magic', 'difficulty']
columns = [ 'roles','attack', 'defense', 'magic', 'difficulty']

''' *—————— 对数据进行可视化 ——————* '''
df_data = roles.values
plt.figure(figsize=(15,15),dpi=60)
for i in range(4):
    for j in range(4):
        plt.subplot(4,4,i*4+j+1)
        if i==0:
            plt.title(columns[j+1])
        if j==0:
            plt.ylabel(columns[i+1])
        if i == j:
            plt.text(0.3,0.4,columns[i+1],fontsize = 15)
            continue       
        plt.scatter(df_data[:,j],df_data[:,i],c= df_data[:,-1],cmap='brg')
        
plt.tight_layout(rect=[0,0,1,0.9])
plt.suptitle('roles\nfighter | mage | tank | assassin | support | marksman', fontsize = 20)
plt.savefig('E:\\大二下\\人工智能基础\\crawl\\lol\\pic\\roles_dataset.png', bbox_inches='tight', pad_inches=0.0)
#plt.show()

''' **—————— 对数据进行切分，分出训练集和测试集—————— ** '''
all_inputs = roles[['attack','defense',
                 'magic','difficulty']].values
all_classes = roles['roles'].values
X_train, X_test, Y_train, Y_test = train_test_split(all_inputs,
                                                 all_classes, train_size=0.8, random_state=1)
 
''' ***—————— 使用决策树算法进行训练—————— *** '''
# 定义决策树对象
dtc = tree.DecisionTreeClassifier(criterion='entropy',min_samples_leaf=8)
# 训练模型
model = dtc.fit(X_train, Y_train)
# 输出所得模型的准确性
print(dtc.score(X_test, Y_test))# 测试集
print(dtc.score(X_train, Y_train))# 训练集
print(dtc.score(all_inputs, all_classes))

''' ****—————— 决策树的可视化 ——————**** '''
font2 = {'weight': 'normal',
         'size': 20,}
mpl.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(20,20))
tree.plot_tree(dtc,filled='True',
               feature_names=['attack', 'defense', 'magic', 'difficulty'],
               class_names=['fighter', 'mage', 'tank','assassin','support','marksman'])
#plt.savefig('E:\\大二下\\人工智能基础\\crawl\\lol\\pic\\roles_dtc.png', bbox_inches='tight', pad_inches=0.0)
#plt.show()

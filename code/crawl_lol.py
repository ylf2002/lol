#######################################
#    School of Software Technology    #
#   Dalian University of Technology   #
#             yang lifan              #
#          2862506026@qq.com          #
#######################################
import json
import requests
import xlwt

# 设置头部信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"
response = requests.get(url=url, headers=headers).text
loads = json.loads(response)
dic = loads['hero']
# 创建一个workbook 设置编码
workbook = xlwt.Workbook('gbk')
# 创建一个worksheet
worksheet = workbook.add_sheet('LOL')
try:
    for i in range(len(dic)):
        # 设置单元格宽度大小
        worksheet.col(i).width = 4000
        # 设置单元格高度大小
        style = xlwt.easyxf('font:height 300')
        worksheet.row(i).set_style(style)
        # 第一行用于写入表头
        if i == 0:
            worksheet.write(i, 0, '编号')
            worksheet.write(i, 1, '名称')
            worksheet.write(i, 2, '英文名')
            worksheet.write(i, 3, '中文名')
            worksheet.write(i, 4, '职业')
            worksheet.write(i, 5, '物攻')
            worksheet.write(i, 6, '物防')
            worksheet.write(i, 7, '魔攻')
            worksheet.write(i, 8, '上手难度')
            worksheet.write(i, 9, '点卷价格')
            worksheet.write(i, 10, '蓝色精粹')
            worksheet.write(i, 11, '周免')
            continue
        # 写入
        worksheet.write(i, 0, dic[i - 1]['heroId'])
        worksheet.write(i, 1, dic[i - 1]['name'])
        worksheet.write(i, 2, dic[i - 1]['alias'])
        worksheet.write(i, 3, dic[i - 1]['title'])
        roles_ = dic[i - 1]['roles']
        roles = []
        for data in roles_:
            if 'mage' == data:
                roles.append('法师')
            if 'tank' == data:
                roles.append('坦克')
            if 'fighter' == data:
                roles.append('战士')
            if 'marksman' == data:
                roles.append('ADC')
            if 'assassin' == data:
                roles.append('刺客')
            if 'support' == data:
                roles.append('辅助')
        worksheet.write(i, 4, str(roles))
        worksheet.write(i, 5, dic[i - 1]['attack'])
        worksheet.write(i, 6, dic[i - 1]['defense'])
        worksheet.write(i, 7, dic[i - 1]['magic'])
        worksheet.write(i, 8, dic[i - 1]['difficulty'])
        worksheet.write(i, 9, dic[i - 1]['couponPrice'])
        worksheet.write(i, 10, dic[i - 1]['goldPrice'])
        worksheet.write(i, 11, dic[i - 1]['isWeekFree'])
        # 保存
    workbook.save('E:\\大二下\\人工智能基础\\crawl\\lol\\data/first_lol_role_data.xls')
except Exception as e:
    print(e)

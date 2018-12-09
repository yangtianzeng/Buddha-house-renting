import sqlite3
import pandas as pd
from pyecharts import Bar
def meanpri_city(city):
    # 连接数据库
    sqlite_cn = sqlite3.connect('data/home-new.sqlite3')
    houseinfos = pd.read_sql('select * from houseinfo', con=sqlite_cn)

    houseinfos['price'] = houseinfos['price'].astype('float')
    # 取出数据、处理
    city = city
    region_price_mean = houseinfos[houseinfos['city'] == city].loc[:, ['region', 'price']].groupby('region').mean()[
        'price'].sort_values(ascending=False)
    for i in region_price_mean.index:
        if len(i) >= 5 or len(i) <= 1 or i == 'null':
            print(i)
            region_price_mean = region_price_mean.drop(i)

    region_index = region_price_mean.index
    region_data = list(region_price_mean.astype(int))
    # 制图
    attr1 = region_index
    v1 = region_data
    title = "{}各区平均价格".format(city)
    bar = Bar(title)
    bar.add("",
            attr1,
            v1,
            is_datazoom_show=True,
            datazoom_type="both",
            datazoom_range=[0, 50], )
    # html = '{}.html'.format(city)
    bar.render('App/city.html')

def tttt():
    return 'qwe'

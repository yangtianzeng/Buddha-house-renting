import numpy as np
import pandas as pd
import sqlite3


def price_mean():
    #平均价格最低的10个城市
    print(houseinfos.loc[:,['city', 'price']].groupby('city').mean()['price'].sort_values(ascending=False)[-11:-1])
    #平均价格最高的10个城市
    print(houseinfos.loc[:,['city', 'price']].groupby('city').mean()['price'].sort_values(ascending=False)[:10])

    #房子数量前10的城市
    print(houseinfos.groupby('city').size().sort_values(ascending=False)[:10])

def mean_area():

    for i in range(0, len(houseinfos)):
        houseinfos.loc[i, 'area'] = houseinfos.loc[i, 'area'][:-2]

    houseinfos['area'] = houseinfos['area'].astype('int')
    #平均面积最大的10个城市
    print(houseinfos.loc[:,['city', 'area']].groupby('city').mean()['area'].sort_values(ascending=False)[:10])
    #平均面积最小的10个城市
    print(houseinfos.loc[:,['city', 'area']].groupby('city').mean()['area'].sort_values(ascending=False)[-11:-1])

    houseinfos['p/a'] = houseinfos['price'] / houseinfos['area']
    #价格/面积最高的前10个城市
    print(houseinfos.loc[:,['city', 'p/a']].groupby('city').mean()['p/a'].sort_values(ascending=False)[:10])
    #价格/面积最高的前10个城市
    print(houseinfos.loc[:,['city', 'p/a']].groupby('city').mean()['p/a'].sort_values(ascending=False)[-11:-1])

def high_citys():
    #价格前500的房子都是哪些城市（饼图）
    print(houseinfos.loc[:, ['city', 'price']].sort_values(by='price', ascending=False)[:500]['city'].value_counts())
    print('~~~~~~~~~~~~~~~~~')
    #价格后500的房子都是哪些城市（饼图）
    print(houseinfos.loc[:, ['city', 'price']].sort_values(by='price', ascending=False)[-501:-1]['city'].value_counts())


def main():
    high_citys()


if __name__ == '__main__':
    sqlite_cn = sqlite3.connect('home (1).sqlite3')

    houseinfos = pd.read_sql('select * from houseinfo;', con=sqlite_cn)

    houseinfos['price'] = houseinfos['price'].astype('int')


    main()

    sqlite_cn.close()

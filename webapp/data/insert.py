import sqlite3

conn = sqlite3.connect('home-new.sqlite3')
conn1 = sqlite3.connect('/home/z/PycharmProjects/house/db.sqlite3')

c = conn.cursor()
c1 = conn1.cursor()

cursor = c.execute("select distinct city from houseinfo")
city_list = []
citys = cursor.fetchall()
for i in citys:
    city_list.append(i[0])

    add_city = c1.execute("insert into App_citymodel(citys) values('{}')".format(i[0]))
    conn1.commit()

cursor = c.execute("select distinct region, city from houseinfo")
regions_list = []
regions = cursor.fetchall()
for i in regions:
    region = i[0]
    cityid = city_list.index(i[1]) + 1
    regions_list.append(region)
    add_region = c1.execute("insert into App_regionmodel(regions, city_id) VALUES('{}', '{}')".format(region, cityid))
    conn1.commit()

cursor = c.execute("select * from houseinfo")

infos = cursor.fetchall()
for i in infos:
    print(i)
    regionid = regions_list.index(i[9]) + 1
    title = i[2]
    price = i[3]
    paytype = i[4]
    renttype = i[5]
    hometype = i[6]
    area = i[7]
    decorade = i[8]
    address = i[10]
    linkman = i[11]
    phone = i[12]
    img = i[13]
    features = i[14]
    sql = "insert into App_housemodel(region_id, title, price, paytype, renttype, hometype, area, decorade, address, linkman, phone, img, features) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)"
    params = (
        regionid, title, price, paytype, renttype, hometype, area, decorade, address, linkman, phone, img, features)
    c1.execute(sql, params)
    conn1.commit()

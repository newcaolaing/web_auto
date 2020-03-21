# from test_demo.test2 import orcs

a = [('201904', '长沙市第一医院', '2.1', '医疗收入', '75968700'), ('201904', '长沙市第一医院', '2.1.1', '门诊收入', '16638200')]
b=[('111','111','2.1','21312412'),('111','111','2.1.1','21312412')]
res = []
for x in  a:
    for xx in b:
        if x[2] == xx[2]:
            res.append(x+(xx[0],))

print(res)

# sql ="""
#
# select to_char(sum("IHS03.01.001")) z,org_code,org_name,'7.6.2'  dh from MV_ZT_YLFW_YLFWQK_ORG where
# datasource='1' and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
# select case  when sum("IHS03.01.023") > 0 then '是' else '否' end     z,org_code,org_name,'7.5.8'  dh from MV_ZT_YLFW_ZYFW_SS_ORG where
# datasource='1' and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
# select to_char(sum("GHS03.03.029")) z ,org_code,org_name ,'7.1.1' dh from MV_ZT_YLFW_YLFWZL_ORG where
# datasource='1' and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
#
# select to_char(sum("IHS03.03.002.01")) z ,org_code,org_name,'3.4'  dh from MV_ZT_YLFW_YLFWZL_JZJG_ORG where
# DATASOURCE ='1' and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
# select to_char(sum("IHS03.01.012")) z ,org_code,org_name,'3.3'  dh from MV_ZT_YLFW_ZYFW_ORG where
# DATASOURCE ='1' and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
# select to_char(sum("GHS03.01.035")) z ,org_code,org_name,'3.1.1.2'  dh from MV_ZT_YLFW_MZFWQK_ORG where
# DATASOURCE ='1' and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
#
# select to_char(sum("IHS03.01.002")) z ,org_code,org_name,'3.1.1'  dh from MV_ZT_YLFW_MZFWQK_ORG where
# DATASOURCE ='1' and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
# select to_char(sum("IHS03.01.001")) z ,org_code,org_name,'3.1'  dh from MV_ZT_YLFW_YLFWQK_ORG where
# DATASOURCE ='1' and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name
# union all
# select to_char(sum(cy)) z,org_code,org_name,'2.1.3'  dh from (
# select sum("GHS03.01.016.03") cy ,org_code,org_name   from MV_ZT_YLFW_MZFWQK_MZFYGC_ORG where
# DATASOURCE ='1' and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name
# union all
# select sum("GHS03.04.032") cy  ,org_code,org_name   from MV_ZT_YLFW_ZYFWQK_ZYFYGC_ORG where
# DATASOURCE ='1' and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name)
# group by org_code,org_name union all
#
#
#
# select to_char(sum("IHS04.01.018.02")) z ,org_code,org_name,'2.1.2.4'  dh from MV_ZT_YPYCL_YPSY_ORG where
# DATASOURCE ='1'
# and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
# select to_char(sum("IHS06.02.013.79")) z ,org_code,org_name ,'2.1.2.3' dh from MV_ZT_YLFW_ZYFWQK_ZYFYCWFL_ORG where
# DATASOURCE ='1'
# and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
#
# select to_char(sum("GHS03.04.026")) z ,org_code,org_name,'2.1.2.2'  dh from MV_ZT_YLFW_ZYFWQK_ZYFYGC_ORG where
# DATASOURCE ='1'
# and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
# select to_char(sum("GHS03.04.002.21")) z ,org_code,org_name,'2.1.2.1'  dh from MV_ZT_YLFW_ZYFWQK_ZYFYGC_ORG where
# DATASOURCE ='1'
# and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
#
# select to_char(sum("IHS06.02.013.16")) z ,org_code,org_name,'2.1.2'  dh from MV_ZT_YLFW_ZYFWQK_ZYFYCWFL_ORG where
# DATASOURCE ='1'
# and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
# select to_char(sum("IHS06.02.013.10")) z ,org_code,org_name,'2.1.1.4'  dh from MV_ZT_YLFW_MZFWQK_MZFYGC_ORG where
# DATASOURCE ='1'
# and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
# select to_char(sum("IHS06.02.013.06")) z ,org_code,org_name,'2.1.1.2'  dh from MV_ZT_YLFW_MZFWQK_MZFYGC_ORG where
# DATASOURCE ='1'
# and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
# select to_char(sum("IHS06.02.013.04")) z ,org_code,org_name,'2.1.1.1'  dh from MV_ZT_YLFW_MZFWQK_MZFYGC_ORG where
# DATASOURCE ='1'
# and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
# select to_char(sum("IHS06.02.013.01")) z ,org_code,org_name,'2.1.1'  dh from MV_ZT_YLFW_MZFWQK_MZFYGC_ORG where
# DATASOURCE ='1'
# and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name union all
#
#
# select to_char(sum(sr)) z,org_code,org_name,'2.1' dh from (
# select sum("IHS06.02.013.01") sr   ,org_code,org_name   from MV_ZT_YLFW_MZFWQK_MZFYGC_ORG where
# DATASOURCE ='1'
# and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name
# union all
# select sum("IHS06.02.013.16") sr ,org_code,org_name   from MV_ZT_YLFW_ZYFWQK_ZYFYCWFL_ORG where
# DATASOURCE ='1'
# and dates like '{dates}%'
# and substr(org_code,0,9) = '{code}'
# and ld='D'
# group by org_code,org_name)group by org_code,org_name
# """

# a=orcs(sql.format(dates="201901",code="444907375"))
# print(a)
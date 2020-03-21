import web
import cx_Oracle
from DBUtils.PooledDB import PooledDB

urls=(
    '/wt/','readFile',
    '/','wt'
)
app = web.application(urls,globals())
render = web.template.frender("templates/index.html")



class readFile:
    def __init__(self):
        self.xt = """
        
select to_char(sum("IHS03.01.001")) z,org_code,org_name,'7.6.2'  dh from MV_ZT_YLFW_YLFWQK_ORG where 
datasource='1' and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all
    

select case  when sum("IHS03.01.023") > 0 then '是' else '否' end     z,org_code,org_name,'7.5.8'  dh from MV_ZT_YLFW_ZYFW_SS_ORG where 
datasource='1' and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all


select to_char(sum("GHS03.03.029")) z ,org_code,org_name ,'7.1.1' dh from MV_ZT_YLFW_YLFWZL_ORG where 
datasource='1' and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all



select to_char(sum("IHS03.03.002.01")) z ,org_code,org_name,'3.4'  dh from MV_ZT_YLFW_YLFWZL_JZJG_ORG where 
DATASOURCE ='1' and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all


select to_char(sum("IHS03.01.012")) z ,org_code,org_name,'3.3'  dh from MV_ZT_YLFW_ZYFW_ORG where 
DATASOURCE ='1' and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all


select to_char(sum("GHS03.01.035")) z ,org_code,org_name,'3.1.1.2'  dh from MV_ZT_YLFW_MZFWQK_ORG where 
DATASOURCE ='1' and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all



select to_char(sum("IHS03.01.002")) z ,org_code,org_name,'3.1.1'  dh from MV_ZT_YLFW_MZFWQK_ORG where 
DATASOURCE ='1' and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all


select to_char(sum("IHS03.01.001")) z ,org_code,org_name,'3.1'  dh from MV_ZT_YLFW_YLFWQK_ORG where 
DATASOURCE ='1' and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name 
union all
select to_char(sum(cy)) z,org_code,org_name,'2.1.3'  dh from (
select sum("GHS03.01.016.03") cy ,org_code,org_name   from MV_ZT_YLFW_MZFWQK_MZFYGC_ORG where 
DATASOURCE ='1' and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name
union all
select sum("GHS03.04.032") cy  ,org_code,org_name   from MV_ZT_YLFW_ZYFWQK_ZYFYGC_ORG where 
DATASOURCE ='1' and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name)
group by org_code,org_name union all



select to_char(sum("IHS04.01.018.02")) z ,org_code,org_name,'2.1.2.4'  dh from MV_ZT_YPYCL_YPSY_ORG where 
DATASOURCE ='1' 
and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all


select to_char(sum("IHS06.02.013.79")) z ,org_code,org_name ,'2.1.2.3' dh from MV_ZT_YLFW_ZYFWQK_ZYFYCWFL_ORG where 
DATASOURCE ='1' 
and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all



select to_char(sum("GHS03.04.026")) z ,org_code,org_name,'2.1.2.2'  dh from MV_ZT_YLFW_ZYFWQK_ZYFYGC_ORG where 
DATASOURCE ='1' 
and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all


select to_char(sum("GHS03.04.002.21")) z ,org_code,org_name,'2.1.2.1'  dh from MV_ZT_YLFW_ZYFWQK_ZYFYGC_ORG where 
DATASOURCE ='1' 
and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all



select to_char(sum("IHS06.02.013.16")) z ,org_code,org_name,'2.1.2'  dh from MV_ZT_YLFW_ZYFWQK_ZYFYCWFL_ORG where 
DATASOURCE ='1' 
and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all


select to_char(sum("IHS06.02.013.10")) z ,org_code,org_name,'2.1.1.4'  dh from MV_ZT_YLFW_MZFWQK_MZFYGC_ORG where 
DATASOURCE ='1' 
and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all


select to_char(sum("IHS06.02.013.06")) z ,org_code,org_name,'2.1.1.2'  dh from MV_ZT_YLFW_MZFWQK_MZFYGC_ORG where 
DATASOURCE ='1' 
and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all


select to_char(sum("IHS06.02.013.04")) z ,org_code,org_name,'2.1.1.1'  dh from MV_ZT_YLFW_MZFWQK_MZFYGC_ORG where 
DATASOURCE ='1' 
and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all


select to_char(sum("IHS06.02.013.01")) z ,org_code,org_name,'2.1.1'  dh from MV_ZT_YLFW_MZFWQK_MZFYGC_ORG where 
DATASOURCE ='1' 
and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name union all


select to_char(sum(sr)) z,org_code,org_name,'2.1' dh from (
select sum("IHS06.02.013.01") sr   ,org_code,org_name   from MV_ZT_YLFW_MZFWQK_MZFYGC_ORG where 
DATASOURCE ='1' 
and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name
union all
select sum("IHS06.02.013.16") sr ,org_code,org_name   from MV_ZT_YLFW_ZYFWQK_ZYFYCWFL_ORG where 
DATASOURCE ='1' 
and dates like '{dates}%'  
and substr(org_code,0,9) = '{code}' 
and ld='D'
group by org_code,org_name)group by org_code,org_name 
        """
    def GET(self):
        result=[]
        web.header('Content-Type', 'text/html;charset=UTF-8')
        i=web.input()
        try:
            yy,yf,md=i.yy,i.yf,i.md
            mds = md.split(",")
            sql_md = "dh like '{}%' ".format(mds[0]) if len(mds) < 2  else "dh like '{}%' or dh like '{}%' ".format(mds[0],mds[1])
        except:
            return render([('','','','',''),[yy,yf,md]])
        sql="select t.rq,case  t.jgdm when '444907391' THEN  '长沙市第三医院'when '444907404' THEN  '长沙市第四医院' when '444907375' THEN  '长沙市第一医院' when '444907455' THEN  '长沙市妇幼保健院' when '444907447' THEN  '长沙市口腔医院' when '444984442' THEN  '长沙市望城区人民医院' when '444907439' THEN  '长沙市中心医院' when '444907412' THEN  '长沙市中医院（市八医院）' when '444947676' THEN  '长沙县第二人民医院' when '444947668' THEN  '长沙县第一人民医院' when '444947705' THEN  '长沙县妇幼保健院' when '444947844' THEN  '长沙县星沙医院' when '444947684' THEN  '长沙县中医院' when '44511780X' THEN  '宁乡市人民医院' when '445117818' THEN  '宁乡市中医医院'when '445117842' THEN  '宁乡县妇幼保健院' when '444984522' THEN  '望城区妇幼保健计划生育服务中心' when '445011773' THEN  '浏阳市妇幼保健院' when '445011749' THEN  '浏阳市人民医院' when '445011757' THEN  '浏阳市中医医院' end jgdm, t.dh,t.zbmc,t.BQ " \
            "from wt.WT_18_2 t inner join wt.wt_org o on  t.jgdm = o.wt_jgdm inner join rrs_organization@hbf orr on o.p_jgdm = orr.org_code " \
            "where o.wt_jgdm in ('444907447','444907391','444907404','444907375','444907439','444907455','444984522','444947844','444907412','444947684','444947676','444947705','445117818','44511780X','445011749','445011773','445011757','445117842','444984442','444947668') " \
            "and  o.wt_jgdm = '{}' and rq = '{}' and( {}) order by dh"
        print("——————————卫统sql——————————")
        result_wt = oracle(sql.format(yy,yf,sql_md))
        print("——————————系统sql——————————")
        result_xt = oracle(self.xt.format(dates=yf,code=yy))
        print(result_wt)
        print(result_xt)
        if result_xt:
            for x in result_wt:
                isadd = False
                for y in result_xt:
                    if x[2] == y[-1]:
                        result.append(x+(y[0],))
                        isadd =True
                if not isadd:
                    result.append(x+("-",))

        results = [result,[yy,yf,md]]
        print(results)
        return  render(results)


def mysql_connection():
    maxconnections = 15  # 最大连接数
    # pool = PooledDB(
    #     pymysql,
    #     maxconnections,
    #     host='192.168.11.111',
    #     user='root',
    #     port=3306,
    #     passwd='123456',
    #     db='bf',
    #     use_unicode=True)
    dsn = cx_Oracle.makedsn('172.16.139.8', 1534, sid='hnsdb14')
    pool = PooledDB(cx_Oracle,mincached=20,blocking=True,user='rhip_hispss_css',password='123456',dsn=dsn)
    return pool

po = mysql_connection()
def oracle(sql):
    con = po.connection()
    cur = con.cursor()
    print(sql)
    result= cur.execute(sql)
    lists = result.fetchall()
    cur.close()
    con.close()
    return lists


class wt():
    def GET(self):
        web.header('Content-Type', 'text/html;charset=UTF-8')
        render = web.template.frender("templates/test.html")
        return render()

def orcs(sql):
    user = "rhip_hispss_css"
    pw = "123456"
    dsn = "172.16.139.8:1534/hnsdb14"

    conn = cx_Oracle.connect(user, pw, dsn)
    cr=conn.cursor()
    result = cr.execute(sql)
    ls = result.fetchall()
    return ls
    # return result





if __name__ == '__main__':
    # sql="select * from wt.WT_18_2 where zbmc = '药品加成情况' and rq='201901'  and jgdm='444907391' "
    # orcs(sql)
    app.run()
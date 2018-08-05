#coding:utf8
'''
网站SEO数据一键批量统计  开发者：李亚涛 wx:841483350
数据库名称为：seo  数据表名称举例 网址为liyatao.com则数据表名称为：liyatao_com
网址为：www.xiaoshiseo.com  则数据表名称为：www_xiaoshiseo_com
'''
import requests,re,MySQLdb,time
conn=MySQLdb.connect(host="localhost",user="root",passwd='',db="seo" ,port=3306,charset="utf8")  #连接数据库
cursor=conn.cursor()  #定位一个指针
from requests.packages.urllib3.exceptions import InsecureRequestWarning   # 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
headers_pc={"User-Agent":"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html）"}
def seo(url):
    date=time.strftime('%Y-%m-%d')  #日期
    url_zhanzhang="http://seo.chinaz.com/%s"%url
    html_zhanzhang=requests.get(url_zhanzhang).content
    baidu_rank=re.findall('/tools/images/public/baiduapp/(\d)\.gif" />',html_zhanzhang)[0]#百度权重
    word_num=re.findall('title="关键词库">(.*?)</a></div>',html_zhanzhang)[0].decode('utf8')
    about_ip=re.findall('<li class="bbn">\s+<div class="Ma01LiRow w10-7"><a href=".*?" target="_blank">(.*?)</a></div>\s+<div class="Ma01LiRow w10-7"><a href=".*?" target="_blank" title="关键词库">',html_zhanzhang)[0].decode('utf8')
    t_now=int(time.time())
    url_archive="http://www.baidu.com/s?wd=site:%s"%url  #百度总收录ULR
    url_archiv_1="http://www.baidu.com/s?wd=site:%s&lm=1&gpc=stf=%s,%s|stftype=1"%(url,t_now-86400,t_now)  #1天收录URL
    url_archiv_7="http://www.baidu.com/s?wd=site:%s&lm=7&gpc=stf=%s,%s|stftype=1"%(url,t_now-604800,t_now) #7天收录URL
    url_archiv_30="http://www.baidu.com/s?wd=site:%s&lm=30&gpc=stf=%s,%s|stftype=1"%(url,t_now-2592000,t_now)#30天收录URL

    url_archive_360="http://www.so.com/s?q=site:%s"%url   #360收录量
    url_archive_sogo="http://www.sogou.com/web?query=site:%s"%url   #搜狗收录量


    html_archive_360=requests.get(url_archive_360,verify=False).content   #360查询收录页面源代码

    html_archive_sogo=requests.get(url_archive_sogo,headers_pc).content   #搜狗查询收录页面源代码


    html_archive=requests.get(url_archive).content   #百度查询收录页面源代码
    html_archive_1=requests.get(url_archiv_1).content
    html_archive_7=requests.get(url_archiv_7).content
    html_archive_30=requests.get(url_archiv_30).content

    if '个网页被360搜索收录' in html_archive_360:
        site_360=re.findall('该网站约(.*?)个网页被360搜索收录',html_archive_360)[0]
        site_360=re.sub(',','',site_360).decode('utf8')
    elif '找到相关结果约' in html_archive_360:
        site_360=re.findall('<p class="ws-total">找到相关结果约(.*?)个</p>',html_archive_360)[0]
        site_360=re.sub(',','',site_360).decode('utf8')
    else:
        site_360=0

    site_sogo=re.findall('<p class="sr-num">找到约(.*?)条结果</p>',html_archive_sogo)[0]
    site_sogo=re.sub(',','',site_sogo).decode('utf8')

    if '个网页被百度收录' in html_archive:
        baidu_site=re.findall('该网站共有\s+<b style="color:#333">(.*?)</b>\s+个网页被百度收录',html_archive)[0]
    elif '找到相关结果数约' in html_archive:
        baidu_site=re.findall('<div class="c-border c-row site_tip"><div class="c-span21 c-span-last"><p><b>找到相关结果数约(.*?)个</b></p><p class="c-gap-top">数字为估算值',html_archive)[0]
    else:
        baidu_site=0
    baidu_site=re.sub(',','',baidu_site).decode('utf8')

    if '个网页被百度收录' in html_archive_1:
        baidu_site1=re.findall('该网站共有\s+<b style="color:#333">(.*?)</b>\s+个网页被百度收录',html_archive_1)[0]
        baidu_site1=re.sub(',','',baidu_site1).decode('utf8')
    elif '找到相关结果数约' in html_archive_1:
        baidu_site1=re.findall('<div class="c-border c-row site_tip"><div class="c-span21 c-span-last"><p><b>找到相关结果数约(.*?)个</b></p><p class="c-gap-top">数字为估算值',html_archive_1)[0]
        baidu_site1=re.sub(',','',baidu_site1).decode('utf8')
    else:
        baidu_site1=0

    if '个网页被百度收录' in html_archive_7:
        baidu_site7=re.findall('该网站共有\s+<b style="color:#333">(.*?)</b>\s+个网页被百度收录',html_archive_7)[0]
        baidu_site7=re.sub(',','',baidu_site7).decode('utf8')
    elif '找到相关结果数约' in html_archive_7:
        baidu_site7=re.findall('<div class="c-border c-row site_tip"><div class="c-span21 c-span-last"><p><b>找到相关结果数约(.*?)个</b></p><p class="c-gap-top">数字为估算值',html_archive_7)[0]
        baidu_site7=re.sub(',','',baidu_site7).decode('utf8')
    else:
        baidu_site7=0

    if '个网页被百度收录' in html_archive_30:
        baidu_site30=re.findall('该网站共有\s+<b style="color:#333">(.*?)</b>\s+个网页被百度收录',html_archive_30)[0]
        baidu_site30=re.sub(',','',baidu_site30).decode('utf8')
    elif '找到相关结果数约' in html_archive_30:
        baidu_site30=re.findall('<div class="c-border c-row site_tip"><div class="c-span21 c-span-last"><p><b>找到相关结果数约(.*?)个</b></p><p class="c-gap-top">数字为估算值',html_archive_30)[0]
        baidu_site30=re.sub(',','',baidu_site30).decode('utf8')
    else:
        baidu_site30=0


    print '日期：'.decode('utf8'),date    #日期
    print '网站网址：'.decode('utf8'),url   #网站网址
    print '百度权重：'.decode('utf8'),baidu_rank  #百度权重
    print '关键词数量：'.decode('utf8'),word_num   #关键词数量
    print '预估流量：'.decode('utf8'),about_ip   #预估流量
    print '百度总收录：'.decode('utf8'),baidu_site  #百度总收录量
    print '百度最近一日收录：'.decode('utf8'),baidu_site1 #最度最近1天收录量
    print '百度最近一周收录：'.decode('utf8'),baidu_site7  #最度最近1周收录量
    print '百度最近一月收录：'.decode('utf8'),baidu_site30 #最度最近1月收录量
    print '360收录：'.decode('utf8'),site_360  #360收录蛳
    print '搜狗收录：'.decode('utf8'),site_sogo  #搜狗收录量
    try:
        cursor.execute("insert into %s(date,url,baidu_rank,word_num,about_ip,baidu_site,baidu_site1,baidu_site7,baidu_site30,site_360,site_sogo) VALUE ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(url_db,date,url,baidu_rank,word_num,about_ip,baidu_site,baidu_site1,baidu_site7,baidu_site30,site_360,''))
        conn.commit()
        print url,'今日SEO数据收集成功'.decode('utf8'),date
    except Exception,ex:
        print Exception,":",ex
        print url,'插入数据库失败,可能今日数量已更新过了'.decode('utf8'),date

if __name__=="__main__":
    urls=["liyatao.com","www.xiaoshiseo.com"]  #网站列表
    for url in urls:
        print '正在查询',url,'的网站seo数据：'
        url_db=re.sub('\.','_',url) #数据库名称 ，比如网址是 hz.xhj.com 就要建一个名字为hz_xhj_com的数据库
        seo(url)

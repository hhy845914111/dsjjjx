import urllib
import myplot

def ReadResults(url):
    k = []
    conn = urllib.urlopen(url)
    for line in conn.fp:
        t = CleanLine(line)
        if t:
            k.append(float(t))
    nums=len(k)  
    M2={}
    M1={}   
    M0={}
    for i in range(nums/3):
        M2[i]=k[i]
        M1[i]=k[i+nums/3]
        M0[i]=k[i+nums*2/3]    
    return M0, M1, M2

def CleanLine(line):
    t = line.split('\"')
    if len(t) !=4 :
        return None
    elif '.' not in t[2] or '\\' in t[2] or '/' in t[2] or '<' in t[0]:
        return None
    else:        
        return t[2]
    
def ReadYear(year=2015):
    '''
    2016:http://www.pbc.gov.cn/diaochatongjisi/resource/cms/2016/09/2016091416275440096.htm
    2015:http://www.pbc.gov.cn/diaochatongjisi/resource/cms/2016/01/2016011818584510775.htm
    2014:"http://www.pbc.gov.cn/eportal/fileDir/defaultCurSite/resource/cms/2015/07/2014s07.htm",
    2013:"http://www.pbc.gov.cn/eportal/fileDir/defaultCurSite/resource/cms/2015/07/2013s07.htm",    
    '''
    url={2016:"http://sdibc.nju.edu.cn/zg/2016091416275440096.htm",
         2015:"http://sdibc.nju.edu.cn/zg/2016011818584510775.htm",
         2014:"http://sdibc.nju.edu.cn/zg/2014s07.htm",
         2013:"http://sdibc.nju.edu.cn/zg/2013s07.htm",  
         }    
    M0, M1, M2=ReadResults(url[year])
    return  M0, M1, M2        

def split(M_1, M):
    x=[]
    y=[]
    c=len(M)
    for i in range(1,c):
        x.append(i+1)
        y.append((M[i]-M_1[i])/M[i]*100)
    return x,y

if __name__=="__main__":
    M0, M1, M2=ReadYear(2016)
    M0_1, M1_1, M2_1 = ReadYear(2015)

    m0x,m0y=split(M0_1, M0)
    m1x,m1y=split(M1_1, M1)
    m2x,m2y=split(M2_1, M2)
    myplot.plot(m0x,m0y,label="M0")
    myplot.plot(m1x,m1y,label="M1")
    myplot.plot(m2x,m2y,label="M2")
    myplot.Show(title=str(2016)+u'货币供应量同比增长率M0，M1与M2对比', xlabel=u'月份', ylabel=u'月环比增长率',legend=True)

    

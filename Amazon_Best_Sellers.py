import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import json
import pandas as pd
import datetime

today = datetime.datetime.now()
h={
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'no-cache',
'cookie': 'session-id=262-8119683-1953160; i18n-prefs=INR; ubid-acbin=259-9680533-5589125; lc-acbin=en_IN; session-token=RrIQQPAAwIh/p5n+tLnpQlqWBZL+afpZI027NCISFJCv647rSx2UK8RykcGNnPeoXFayl3Jty6ZmDNTWESleefibiVRuS05yQjJBgr1n+G72utQPl6g0oKnpwl3bWb/irmo+hUP5yfIipGJCAxGgwrTA7rX20Ap1yWI3frj+AQqdugYR8kwXDiQK8ZNDfYAOgqxraq0m9swJMnIFBFHPn98zIm5GNuUw; csm-hit=tb:CDAKZF3EYTAR6R8CNS0P+s-CDAKZF3EYTAR6R8CNS0P|1663569022624&t:1663569022624&adb:adblk_no; session-id-time=2082787201l',
'device-memory': '8',
'downlink': '10',
'dpr': '1',
'ect': '4g',
'pragma': 'no-cache',
'rtt': '50',
'sec-ch-device-memory': '8',
'sec-ch-dpr': '1',
'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-ch-viewport-width': '1366',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'service-worker-navigation-preload': 'true',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
'viewport-width': '1366'
   }
h2={
'accept': 'text/html, application/json',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'no-cache',
'content-length': '1948',
'content-type': 'application/json',
'cookie': 'session-id=262-8119683-1953160; i18n-prefs=INR; ubid-acbin=259-9680533-5589125; lc-acbin=en_IN; s_cc=true; s_nr=1663673457080-New; s_vnum=2095673457081%26vn%3D1; s_dslv=1663673457084; s_sq=%5B%5BB%5D%5D; s_ppv=56; session-token=xCwLRfYCFsHL48vi2XpTWbV687ibfNdJc2Hfxewz2A2Ex3TJlWIxlDbk+grRwkO371bRq1KaR2wJhrmAyvCp/CT1O7gO9DP4YgDPTO1/eJajITmAxrOOahOaY3HrFrNyg44Zx5hzzRgxs/Vu4vbQeeBhwleEIJJ/dGbxoAPKyPWBGlpGxuqp3y0jD0lraaAaUO3LlAVkPCm0AqRV476E5Ba50TInyBRc; csm-hit=tb:s-4PNE47XK425JGP3GEZM4|1663823455616&t:1663823455880&adb:adblk_no; session-id-time=2082758401l',
'device-memory': '8',
'downlink': '10',
'dpr': '1',
'ect': '4g',
'origin': 'https://www.amazon.in',
'pragma': 'no-cache',
'rtt': '50',
'sec-ch-device-memory': '8',
'sec-ch-dpr': '1',
'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-ch-viewport-width': '1366',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
'viewport-width': '1366',
'x-amz-acp-params': 'tok=n3hM_UljhJbt74Ojmc5jhj0uBA8oUzN64WLyFl7UNLw;ts=1663823454967;rid=4PNE47XK425JGP3GEZM4;d1=160;d2=0',
'x-requested-with': 'XMLHttpRequest'
                }
test_url = 'https://www.amazon.in/gp/bestsellers/grocery/4859508031'
pg =requests.get(test_url)
s1 = bs(pg.content,'html.parser')
url3 = 'https://www.amazon.in'+s1.find('div',{'data-card-metrics-id':'p13n-zg-list-grid-desktop_zeitgeist-lists_2'})['data-acp-path']+'nextPage?page-type=zeitgeist&stamp=1713156676700'
print(url3)
aurl=['https://www.amazon.in/gp/bestsellers/grocery/',
      'https://www.amazon.in/gp/bestsellers/electronics/',
      'https://www.amazon.in/gp/bestsellers/beauty/',
      'https://www.amazon.in/gp/bestsellers/hpc/',
      'https://www.amazon.in/gp/bestsellers/baby/']
ati=['Grocery & Gourmet Foods',
     'Electronics',
     'Beauty',
     'Health & Personal Care',
     'Baby Products']
end=[]
emli=[]

def check_get(url):
    n=1
    while n<5:
        try:
            pg3 = requests.get(url, headers=h)
            return pg3
        except:
            print('Connection Sleeping........')
            sleep(10*n)

def check_post(url3,da):
    n=1
    while n<5:
        try:
            pg3 = requests.post(url3, headers=h2,data=json.dumps(da))
            return pg3
        except:
            print('Connection Sleeping........')
            sleep(10*n)
            
def all_cat(cali,cat):
    tag = cat.find('div',{'class':'_p13n-zg-nav-tree-all_style_zg-browse-group__88fbz'})
    cali.append(cat.find('div',{'role':'treeitem'}).find('a').text)
    if tag.get('role'):
        cali.append(tag.find('span').text)
        cali.extend(['N/A']*(8-len(cali)))
        return cali
    else:
        return all_cat(cali,tag)

def data_scrap(rda):
    if not rda:
        return []
    dali=[]
    da = {
          "faceoutkataname": "GeneralFaceout",
          "ids": '}${'.join(json.dumps(rda)[1:-1].split('}, {')).split('$'),
          "reftagprefix": "zg_bs_g"
        }
    n=1
    while n<5:
        try:
            pg3 = check_post(url3,da)
            s5 = bs(pg3.content,'html.parser')
            s6 = s5.find('div',{'class':'p13n-gridRow _cDEzb_grid-row_3Cywl'}).findAll('div',{'id':'gridItemRoot'})
            break
        except:
            print('Sleeping.....')
            sleep(5*n)
    for k in s6:
        ra=na=star=peo=pr=img=pid='N/A'
        try:ra=k.find('span',{'class':'zg-bdg-text'}).text.replace('#','')#rank
        except:pass
        try:na=k.find('div',{'class':'p13n-sc-uncoverable-faceout'}).find('span').text.strip('- ').encode("ascii", "ignore").decode()#name
        except:pass
        try:star=k.find('span',{'class':'a-icon-alt'}).text.replace(' out of 5 stars','')#star
        except:pass
        try:peo=k.find('div',{'class':'a-icon-row'}).find('span',{'class':'a-size-small'}).text#people
        except:pass
        try:pr=float(k.find('span',{'class':'_cDEzb_p13n-sc-price_3mJ9Z'}).text.encode("ascii", "ignore").decode().replace(',',''))#prize
        except:pass
        try:img=k.find('img')['src']#Image
        except:pass
        try:pid=k.find('div',{'class':'p13n-sc-uncoverable-faceout'})['id']#product Id
        except:pass
        dali.append([pid,ra,na,star,peo,pr,img])
    return dali

def get_data(curl,rid):
    url2=curl+rid
    if rid in emli:
        return pd.DataFrame()
    emli.append(rid)
    all_data=[]
    cali=[]
    for j in range(1,3):
        print(url2+f'/?pg={j}')
        n=1
        while n<5:
            try:
                pg2=check_get(url2+f'/?pg={j}')
                s3 = bs(pg2.content,'html.parser')
                if j==1:    
                    cat = s3.find('div',{'class':'_p13n-zg-nav-tree-all_style_zg-browse-group__88fbz'})
                    ca=all_cat(cali, cat)
                s4 = eval(s3.find('div',{'class':'p13n-desktop-grid'})['data-client-recs-list'])
                break
            except:
                print('Sleeping.......')
                sleep(5*n)
        # print(ca)
        # return 0
        page_data=data_scrap(s4[:25])  # 1st 25 Rank data getting
        page_data.extend(data_scrap(s4[25:]))  #2nd 25 Rank data getting
        all_data.extend(page_data)
        
    df=pd.concat(
    [pd.DataFrame(
    [ca]*len(all_data),
    columns=['Category','Sub_Category_1','Sub_Category_2','Sub_Category_3','Sub_Category_4','Sub_Category_5','Sub_Category_6','Sub_Category_7'])
    ,pd.DataFrame(all_data,columns=['Product_Id','Rank','Name','Rating','People','Prize','Image_Link'])],axis=1)
    return df

def root(curl,rid):
    n=1
    while n<5:
        pg = check_get(curl+rid)
        s1 = bs(pg.content,'html.parser')
        s2 = s1.find('div',{'role':'group'})
        # print(curl,rid)
        try:
            span = s2.find('span')
            break
        except AttributeError:
            print('Sleeping.........')
            sleep(5*n)
    if span:
        # print(rid,span.text,curl)
        return get_data(curl, rid)
    else:
        lis = dict(map(lambda x:(x.find('a')['href'].split('/')[-2],x.text),s2.findAll('div',{'role':'treeitem'})))
        # print(lis)
        for i in lis:
            end.append(root(curl,i))
            
for url,ti in zip(aurl,ati):
    root(url, '')
df2=pd.concat(end)
eli=df2.Rank.to_list()
for i in range(len(eli)):
    try:    
        eli.insert(i,int(eli[i]))
        eli.pop(i+1)
    except:
        eli.insert(i,int(eli[i-1])+1)
        eli.pop(i+1)
df2['Rank']=eli
df2=df2.drop_duplicates()
df2 = df2[(df2.Category==ati[0]) | (df2.Category==ati[1])| (df2.Category==ati[2])| (df2.Category==ati[3])| (df2.Category==ati[4])]
df2.to_csv(fr'D:\Sethu\Amazon Updated\Amazon_Best_Sellers({today.day}.{today.month}.{today.year}).csv',index=False)
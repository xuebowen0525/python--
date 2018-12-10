import requests
from bs4 import BeautifulSoup
import xlsxwriter
import os,stat
def writeExcel(row=0):  
       if row ==0:
           worksheet.write(row,0,'书名')
           worksheet.write(row,1,'作者')
           worksheet.write(row,2,'评分')
           worksheet.write(row,3,'描述')
       else:
           worksheet.write(row,0,list[row-1][0])
           worksheet.write(row,1,list[row-1][1])
           worksheet.write(row,2,list[row-1][2])
           worksheet.write(row,3,list[row-1][3])
           
       
def get_info(url):
    html = requests.get(url).text
    Soup = BeautifulSoup(html,'lxml')
    data = Soup.find('ul',{'class':'subject-list'}).find_all('li')
    for info in data:
        #标题
        titles = info.find('div',{'class':'info'}).find('a')
        title = titles.get_text(strip=True).replace(' ','')
        #作者
        authors = info.find('div',{'class':'pub'})
        author = authors.get_text(strip=True).split('/')[0].replace(' ','')
        #评价
        rating_nums = info.find('span',{'class':'rating_nums'})
        rating_num = rating_nums.get_text(strip=True)
        #描述
        descs = info.find('div',{'class':'info'}).find_all('p')
        desc = descs[0].get_text()
        list.append([title,author,rating_num,desc])
    return list
   

if __name__ =='__main__':
    workbook = xlsxwriter.Workbook("豆瓣读书.xlsx")
    worksheet = workbook.add_worksheet('小说')
    list=[]
    page =0
    #url中start参数的值
    i = 0
    #要爬取的页数
    y = 1
    writeExcel(row=0)
    while i <=(y-1)*20:
        url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start='+ str(i) + '&type=T'
        get_info(url)
        page +=1
        i = page*20
    row = 1 
    #将getinfo()返回的list中的数据保存到excle中
    while row <= len(list):        
        writeExcel(row=row)
        row = row +1
    workbook.close()

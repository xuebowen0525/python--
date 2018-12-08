import requests
from bs4 import BeautifulSoup
import xlsxwriter
import os
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
        titles = info.find('div',{'class':'info'})
        title = str(titles.find('a').text).replace(' ', '')
        #作者
        authors = info.find('div',{'class':'pub'})
        author = authors.text.replace(' ','').split('/')[0]
        #评价
        rating_nums = info.find('div',{'class':'star clearfix'})
        rating_num = rating_nums.find('span',{'class':'rating_nums'}).text
        #描述
        descs = info.find('p')
        desc = descs.text.replace('\u2022','').replace('\u2027','').replace('\u22ef','')
        list.append([title,author,rating_num,desc])
    return list
   

if __name__ =='__main__':
    workbook = xlsxwriter.Workbook("C:\\Users\\Administrator\\Desktop\\python\\豆瓣读书.xlsx")
    worksheet = workbook.add_worksheet('小说')
    list=[]
    page =0
    writeExcel(row=0)
    while page <= 20:
        url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start='+ str(page) + '&type=T'
        get_info(url)
        page = (page+1)*20
    row = 1
    while row <= len(list):        
        writeExcel(row=row)
        row = row +1
    workbook.close()
    

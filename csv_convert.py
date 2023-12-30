import os
import re
import bs4
import csv

class CsvConverter:
    def __init__(self,path):
        self.path = path
        self.dump_path = os.path.basename(path).replace('.html','.csv').replace(' ','')
        print(self.dump_path)
    
    def dump(self):
        soup = bs4.BeautifulSoup(open(self.path), 'html.parser')
        table = soup.find('table')

        data_list = []        
        trs = table.findAll('tr')
        for tr in trs:
            tds = tr.findAll('td')
            if len(tds) != 6:
                continue
            a,b,_,d,_,_ = tr.findAll('td')
            image = a.find('img').get('src').replace('SS135','SL1217')
            title = b.text.replace('\n','').replace('\t','').replace(' ','').replace('|','')
            price = 0
            if '-' not in d.text:
                price = int(re.search(r'\d+', d.text).group())
            data = {
                'buy': 'No',
                'importance': '★★★',
                'Name': title,
                'Tag':'本',
                'brand' : '',
                'reference price': price,
                'purchase price':'',
                'image': image,
                'title': title,
            }
            data_list.append(data)


        f = open(self.dump_path, "w")
        writecsv = csv.DictWriter(f, fieldnames=data_list[0].keys(), lineterminator='\n')
        writecsv.writeheader()
        writecsv.writerows(data_list)
        f.close() 

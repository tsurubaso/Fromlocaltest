    def search1(self,adress1, adress2, nbrBoucle, eraseName, nameCsv):
        nbrBoucle=int(nbrBoucle)
        for i in range (1,nbrBoucle,1):
            gribou=adress1+str(i)
            result2 = requests.get (gribou)
            a=result2.status_code
            print (a)
            soup = BeautifulSoup(result2.text, 'html.parser')
            for a in soup.find_all('a'):
                fullstring= a.get('href')
                if fullstring is None:
                    continue
                if substring in fullstring:
                    my_list.append(adress2+fullstring)

        df = pd.DataFrame(my_list, columns = ['col1'])
        df.sort_values(by=['col1'])
        df.drop_duplicates(keep='first', inplace=True)
        count_row = df.shape[0]  # gives number of row count
        count_col = df.shape[1]
        print (count_row )
        print (count_col )
        print (len(my_list))
        #df.to_csv('HopitalList.csv', index=False)

        df2 = pd.DataFrame(columns=['Name', 'Phone','post code','adress','Url','Client Adress'])
        for i in range (1,len(my_list),1):
            url = my_list[i]
            page=urllib.request.urlopen(url)
            soup = BeautifulSoup(page, 'html.parser')
            bloublou4=soup.find_all('td')
            print('                         ')
            bloublou2=soup.find('h1',attrs={"class":"page_title"})
            if bloublou2 is None:
                bloublou2='None'
            else:
                bloublou2=bloublou2.text
                bloublou2=bloublou2.replace(eraseName, '')
            
            if bloublou4[0] is None:
                bloublou4[0]='None'
            else:
                bloublou4[0]=bloublou4[0].text
                bloublou4[0]=bloublou4[0].replace('地図を見る', '')
                bloublou4a=bloublou4[0][10:]
                bloublou4b=bloublou4[0][:9]

            if bloublou4[1] is None:
                bloublou4[1]='None'
            else:
                bloublou4[1]=bloublou4[1].text
                bloublou4[1]=bloublou4[1][:13]
            
            if len(bloublou4) <31:
                glagla='None'
            try:
                glagla=bloublou4[31].text.strip()
        
            except IndexError:
                glagla='None'

            df2.loc[i] = [ bloublou2,bloublou4[1], bloublou4b,bloublou4a, glagla, url]
            
        df2.sort_values(by=['Name'])
        df2.drop_duplicates(keep='first', inplace=True)
        df2.to_csv(nameCsv+".csv", index=False, encoding="utf_8_sig")
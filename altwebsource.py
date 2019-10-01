##Cookie cutter code for alternative source to retrieve data from  -- 

import requests
from bs4 import BeautifulSoup
import codecs
import sys


'''
This version is now ready for primetime deployment
'''


f = codecs.open('phonetics.txt','a','utf-8')

while True:

    try:
        word = input(str('Enter a word to fetch phonetics :\t'))
        if word=='hackerman64':
            f.close()
            quit()
            
        URL = 'https://www.merriam-webster.com/dictionary/'+word

        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/75.0.3770.100 Safari/537.36'}

        page = requests.get(URL,headers=headers)

        soup = BeautifulSoup(page.content,'html.parser')

        phonetics = soup.find("span",{"class":"pr"})

        phonestr = str(phonetics)

        lst = phonestr.split('<')
        str1 = lst[1]
        ipa = str1.split('>')[1]

        ##Finally working correctly
        ipa = ipa.encode('utf-8')
        word_and_phonetics = word+" "+ipa.decode()
        print(word_and_phonetics,end="\n")

        f.write(word_and_phonetics+"\n")
    
    except:
        ipa = ''
        ipa = ipa.encode('utf-8')
        word_and_phonetics = word+" "+ipa.decode()
        print(word_and_phonetics,end="\n")

        f.write(word_and_phonetics+"\n")


f.close()

import requests
from bs4 import BeautifulSoup
import codecs

'''
Call phonetics using Free Dictionary scraper
'''

def ipa_fd(word):
    try:

        URL = 'https://www.merriam-webster.com/dictionary/'+word

        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/75.0.3770.100 Safari/537.36'}

        page = requests.get(URL,headers=headers)

        soup = BeautifulSoup(page.content,'html.parser')

        phonetics = soup.find("span",{"class":"pron"})

        phonestr = str(phonetics)

        lst = phonestr.split('(')
        #print(lst)
        str1 = lst[2]
        ipa = str1.split(')')[0]

        ##Finally working correctly
        ipa = ipa.encode('utf-8')
        ipa = ipa.decode()
        ipa_list = ipa.split(',')
        word_and_phonetics = (word,ipa_list)
        return(word_and_phonetics)

    except:
        ipa = '-----'
        ipa = ipa.encode('utf-8')
        word_and_phonetics = (word,[ipa.decode()])
        return(word_and_phonetics)
        

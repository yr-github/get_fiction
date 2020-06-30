import requests
from bs4 import BeautifulSoup
import mail

class GetFiction:
    host="https://www.biquge.info/{fiction}/"
    def __init__(self,fiction_dict,config):
        self._fiction_dict = fiction_dict
        self.update_config_list=[]
        self.config = config
        return

    def check_update(self):
        for self.fiction,self.chapter in self._fiction_dict.items():
            resp = requests.get(self.host.format(fiction=self.fiction))
            bs = BeautifulSoup(resp.content,'html.parser')
            ddlist = bs.find_all('dd')
            #TODO 解决汉字章节的问题，初步判断可以通过dd数解决，这样就不用判断阿拉伯还是中文数字了
            count = -5
            for dd in ddlist[count:]:
                title = dd.contents[0].attrs['title']
                count += 1
                if self.chapter in title:
                    break
            if count:
                for dd in ddlist[count:]:
                    title = dd.contents[0].attrs['title']
                    self.get_content(self.host.format(fiction=self.fiction),dd.contents[0].attrs['href'],title)
        return

    def get_content(self,url,route,title):
        resp = requests.get(url+route)
        bs = BeautifulSoup(resp.content, 'html.parser')
        content = bs.find('div',id='content')
        if "正在手打中" in content.text:
            return None
        else:
            mail_obj = mail.SendEmail()
            mail_obj.sendemail(url+route+'\n'+content.text,title)
            self.chapter = title
    #        self.update_chapter()
            self.change_config()
        return

    # def update_chapter(self):
    #     self.update_config_list.append(self.fiction)
    #     return
    def change_config(self):
        section = "fiction_chapter"
        self.config[section][self.fiction] = self.chapter

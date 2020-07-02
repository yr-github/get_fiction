import requests
from bs4 import BeautifulSoup
import mail
import re
import fic_tools


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
            count = -5
            for dd in ddlist[count:]:
                title = dd.contents[0].attrs['title']
                count += 1
                if self.chapter in title:
                    break
            #TODO 如果一次更新六章则会导致永远不再更新
            if count:
                for dd in ddlist[count:]:
                    title = dd.contents[0].attrs['title']
                    self.get_content(self.host.format(fiction=self.fiction),dd.contents[0].attrs['href'],title)

        return

    def get_content(self,url,route,title):
        resp = requests.get(url+route)
        re_content = fic_tools.bytes_to_str(resp.content)
        chapter_content = re.findall(r'<!--go-->(.*)<!--over-->', re_content,re.DOTALL)
        if "正在手打中" in chapter_content[0]:
            return None
        else:
            mail_obj = mail.SendEmail()
            mail_obj.sendemail(url+route+'\n'+chapter_content[0],title)
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

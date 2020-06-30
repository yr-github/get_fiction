#自动获取网文更新并发送到邮箱中
import configparser
import fiction
import time

if __name__ == '__main__':
    while True:
        try:
            config = configparser.ConfigParser()
            config.read("config.ini",encoding='utf-8')
            section = "fiction_chapter"
            options = config.options(section)
            fiction_dict={}
            for option in options:
                 fiction_dict[option]=config[section][option]
            getfic_obj =  fiction.GetFiction(fiction_dict,config)
            getfic_obj.check_update()
            config.write(open("config.ini", "w",encoding='utf-8'))
            time.sleep(int(config['query_time']['time']))
        except:
            pass




from scrapy.cmdline import execute

import  sys
import  os

#print(os.path.dirname())
#文件地址
print(os.path.abspath(__file__))
#文件夫目录
print(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#运行命令行 scrapy crawl biquge
execute(['scrapy','crawl','biquge'])
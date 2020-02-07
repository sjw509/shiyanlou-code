import os
from pprint import pprint
import requests
from lxml import etree

class MeiZiTu(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
            'Referer': 'http://www.mzitu.com'
        }
        self.start_url = "https://www.mzitu.com/hot"
        self.imgs_list = list()

    def get_resquest_content(self, url): # 请求url,得到响应, 返回二进制内容
        response = requests.get(url, headers = self.headers)
        return response.content

    def wirte_content(self, content, item, index):
        with open("meizitu"+"/"+item["title"]+"/"+str(index)+".jpg", "wb") as f:
            f.write(content)


    def get_all_series(self, content): # 获得每个图集的标题和链接 每个字典都是一个新的图集
        html = etree.HTML(content)
        li_list = html.xpath('//div[@class="postlist"]/ul/li[not(@class="box")]') # 这里属性为box的是广告
        for li in li_list:
            item = {}
            item["imgs_list"] = [] # 专门用来保存下一页的Url
            item["href"] = li.xpath("./a/@href")[0]
            item["title"] = li.xpath("./a/img/@alt")[0]
            self.imgs_list.append(item)


    def download_all_pics(self):
        for item in self.imgs_list:
            try:
                os.mkdir("meizitu"+"/"+item["title"])
            except: # 如果走到这里 就表示文件夹已经存在 我们不做任何处理就行
                pass
            item["imgs_list"].append(item["href"]) # 将第一张图片的url放到列表中
            pprint(item)
            self.down_other_imgs(item["href"], item)  # 获取其他页码的图片 同样放到列表中

    def down_other_imgs(self, next_img_url, item): # 获取图集的每一页图片url 并且传给get_per_img方法
        content = self.get_resquest_content(next_img_url)
        response = etree.HTML(content)
        next_img_url_try = response.xpath('//span[text()="下一页»"]/../@href')
        if next_img_url_try:
            next_img_url = next_img_url_try[0]
            item["imgs_list"].append(next_img_url)
            img_content = self.get_resquest_content(next_img_url)
            self.down_other_imgs(next_img_url, item)
        else:
            # 到这里表示递归应该结束 因为没有下一页了 应该下载图片
            pprint("+"*10+str(item["imgs_list"]))
            for url in item["imgs_list"]:
                img_url = self.get_response_img_url(url)
                con = self.get_resquest_content(img_url)
                index = item["imgs_list"].index(url) + 1
                self.wirte_content(con,item, index)
                print("下载成功---%s"%(item["title"]+str(index)+".jpg"))
            return

    def get_response_img_url(self, url):
        # 提取详情页中的图片url并且返回
        content = self.get_resquest_content(url)
        response = etree.HTML(content)
        img_url = response.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
        return img_url

    def get_first_img(self, data, item):
        # 爬取该图集每一页的图片
        response = etree.HTML(data)
        img_url = response.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
        item["img_url"] = img_url
        item["img_name"] = response.xpath('//h2[@class="main-title"]/text()')[0]
        content = self.get_resquest_content(img_url)
        self.wirte_content(content, item)



    def mkdir_main(self):
        try:
            os.mkdir("meizitu")
        except:
            pass


meizi = MeiZiTu()
meizi.mkdir_main()
content = meizi.get_resquest_content(meizi.start_url)
meizi.get_all_series(content)
pprint(meizi.imgs_list)
meizi.download_all_pics()

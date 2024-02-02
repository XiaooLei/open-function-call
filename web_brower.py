import requests
from bs4 import BeautifulSoup

def baidu_search(query: str) -> str:
    url = """https://www.baidu.com/s?ie=utf-8
    &newi=1
    &mod=1
    &isbd=1
    &isid=e999b77a0002ae31
    &wd={}
    &rsv_spt=1
    &rsv_iqid=0xeeb2fe78000991f7
    &issp=1
    &f=8
    &rsv_bp=1
    &rsv_idx=2
    &ie=utf-8
    &rqlang=cn
    &tn=baiduhome_pg
    &rsv_dl=tb
    &rsv_enter=1
    &oq=%25E6%25BC%2595%25E6%25B2%25B3%25E6%25B3%25BE%25E5%2592%258C%25E5%25A5%2587%25E5%25B2%25B1%25E6%259D%25BE%25E4%25BB%2580%25E4%25B9%2588%25E5%2585%25B3%25E7%25B3%25BB
    &rsv_btype=t
    &inputT=2279
    &rsv_t=ccf336PHM5f7i7mYSB0zlr%2Fv7bwU0x%2B2TgWVTW9hr7sGV%2FPaeBzIKcMmpvaeDei337Xs
    &bs=%E6%BC%95%E6%B2%B3%E6%B3%BE%E5%92%8C%E5%A5%87%E5%B2%B1%E6%9D%BE%E4%BB%80%E4%B9%88%E5%85%B3%E7%B3%BB
    &rsv_sid=39227_39222_39285_39097_39261_39268_39240_39233_26350_39238_39224_39149
    &_ss=1
    &clist=
    &hsug=
    &f4s=1
    &csor=9
    &_cr1=54702
    """.format(query)
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": "www.baidu.com",
        "Is_pbs": "leopard",
        "Is_referer": "https://www.baidu.com/s?wd=leopard&rsv_spt=1&rsv_iqid=0xeeb2fe78000991f7&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_dl=tb&rsv_enter=1&oq=leopard&rsv_btype=t&inputT=21399&rsv_t=ea35alySZ%2FopOKleORpJhCxbSQTcstz0f84rA1qm9gpnHC47dge%2BWVsE6v5QJw%2BfBMcg&rsv_pq=882cc89e0000e7bc&rsv_sug3=84&rsv_sug1=72&rsv_sug7=101&rsv_sug2=0&rsv_sug4=21948&rsv_sug=1&bs=leopard",
        "Is_xhr": "1",
        "Ps-Dataurlconfigqid": "0xeeb2fe78000991f7",
        "Referer": "https://www.baidu.com/s?wd=%E6%BC%95%E6%B2%B3%E6%B3%BE&rsv_spt=1&rsv_iqid=0xeeb2fe78000991f7&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_dl=tb&rsv_enter=1&oq=leopard&rsv_btype=t&inputT=3073&rsv_t=8627%2BkI09PlWEzSd%2FLCjPxw0jib9CC7UJY3ZJ%2BXtOpSSQxrBAOPbiHJ8eo8KcLJGYyuV&rsv_pq=a18c099900001240&rsv_sug3=98&rsv_sug1=87&rsv_sug7=101&rsv_sug2=0&rsv_sug4=3918",
        "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"macOS\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    proxies = {
        'http': None,
        'https': None
    }

    # 发送GET请求
    response = requests.get(url, headers=headers, proxies=proxies)

    # 检查请求是否成功
    if response.status_code == 200:
        html = response.text
        # 处理获取到的HTML内容
    else:
        print("请求失败")

    # 创建BeautifulSoup对象
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    lines = [line.strip() for line in text.splitlines() if line.strip() and len(line) > 20]
    lines = lines[3:]

    cleaned_text = '\n'.join(lines)
    # print(cleaned_text)
    return cleaned_text

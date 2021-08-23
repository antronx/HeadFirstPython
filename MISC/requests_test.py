import requests

urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com')


def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url


for resp_len, status, url, in gen_from_urls(urls):
    print(resp_len, status, url, )

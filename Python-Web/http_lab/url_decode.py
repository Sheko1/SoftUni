from urllib import parse


def decode_url(url):
    return parse.unquote(url)


urls = [
    r"http://www.google.bg/search?q=C%23",
    r"https://mysite.com/show?n%40m3=p3%24h0",
    r"http://url-decoder.com/i%23de%25?id=23"
]


for url in urls:
    print(decode_url(url))

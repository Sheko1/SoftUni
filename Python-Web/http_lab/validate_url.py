from urllib import parse


def get_protocol(scheme):
    if scheme in ("http", "https"):
        return scheme
    return None


def get_host_and_port(netloc, scheme):
    if "." not in netloc:
        return (None, None)

    if ":" not in netloc:
        port = 80 if scheme == "http" else 443
        netloc = f"{netloc}:{port}"

    return netloc.split(":")


def get_path(path):
    return path or "/"


def validate_url(url):
    url = parse.urlparse(url)
    protocol = get_protocol(url.scheme)
    host, port = get_host_and_port(url.netloc, url.scheme)
    path = get_path(url.path)
    query = url.query
    fragment = url.fragment

    if None in (protocol, host, port, path):
        return "Invalid URL"

    return f"Protocol: {protocol}\nHost:{host}\nPort:{port}\nPath:{path}\nQuery:{query}\nFragment:{fragment}"


urls = [
    r"https://mysite:80/demo/index.aspx",
    r"somesite.com:80/search?",
    r"https/mysite.bg?id=2",
    r"http://mysite.com:80/demo/index.aspx",
    r"https://my-site.bg",
    r"https://mysite.bg/demo/search?id=22o#go"
]

for url in urls:
    print(validate_url(url))

# -*- coding: utf-8 -*-

# PROTOCOL - whether to enable getting certain protocol proxies (True or False).
# PROTOCOL_SOURCES - proxy lists URLs.
HTTP = True
HTTP_SOURCES = (
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
    "https://raw.githubusercontent.com/chipsed/proxies/main/proxies.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
    "https://raw.githubusercontent.com/KUTlime/ProxyList/main/ProxyList.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
    "https://raw.githubusercontent.com/proxiesmaster/Free-Proxy-List/main/proxies.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
)

# SOCKS proxies need PySocks library installed.
SOCKS4 = True
SOCKS4_SOURCES = (
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://www.proxy-list.download/api/v1/get?type=socks4",
)
SOCKS5 = True
SOCKS5_SOURCES = (
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://www.proxy-list.download/api/v1/get?type=socks5",
)

# Add geolocation info for each proxy (True or False).
# Output format is ip:port::Country Name::Region::City
GEOLOCATION = True

# Service for getting your IP address and checking if proxies are valid.
IP_SERVICE = "https://ident.me"

# How many seconds to wait for the proxy to make a connection.
# Lower value results in getting less proxies but they will be faster.
TIMEOUT = 5

# -*- coding: utf-8 -*-

# PROTOCOL - whether to enable getting certain protocol proxies (True or False).
# PROTOCOL_SOURCES - proxy lists URLs.
HTTP = True
HTTP_SOURCES = {
        "https://raw.githubusercontent.com/BlackSnowDot/proxylist-update-every-minute/main/http.txt",
        "http://olaf4snow.com/public/proxy.txt",
        "https://raw.githubusercontent.com/ItzRazvyy/ProxyList/main/http.txt",
        "https://raw.githubusercontent.com/ItzRazvyy/ProxyList/main/https.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt",
        "https://raw.githubusercontent.com/boldleadsdevelopment/lockdown/master/lists/blacklists/blocklist.de.ips",
        "https://raw.githubusercontent.com/securityscorecard/SSC-Threat-Intel-IoCs/master/KillNet-DDoS-Blocklist/proxylist.txt",
        "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://www.proxyscan.io/download?type=http",
        "http://spys.me/proxy.txt",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://api.openproxylist.xyz/http.txt",
        "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
        "http://alexa.lr2b.com/proxylist.txt",
        "http://rootjazz.com/proxies/proxies.txt",
        "https://www.freeproxychecker.com/result/http_proxies.txt",
        "http://proxysearcher.sourceforge.net/Proxy%20List.php?type=http",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
        "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
        "https://proxy-spider.com/api/proxies.example.txt",
        "https://multiproxy.org/txt_all/proxy.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
        "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt",
        "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt",
        'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt',
        'https://openproxy.space/list/http',
        'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
        'https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt',
        'https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt',
        'https://raw.githubusercontent.com/almroot/proxylist/master/list.txt',
        'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt',
        'https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt',
        'https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt',
        'https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt',
        'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
        'https://proxylist.live/nodes/free_1.php?page=1&showall=1',
}

# SOCKS proxies need PySocks library installed.
SOCKS4 = True
SOCKS4_SOURCES = {
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
}
SOCKS5 = True
SOCKS5_SOURCES = {
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
}

# Add geolocation info for each proxy (True or False).
# Output format is ip:port::Country::Region::City
GEOLOCATION = True

# Service for checking the IP address.
# For some people "https://checkip.amazonaws.com" is faster than "https://ident.me".
IP_SERVICE = "https://ident.me"

# How many seconds to wait for the proxy to make a connection.
# Lower value results in getting less proxies but they will be faster.
TIMEOUT = 15

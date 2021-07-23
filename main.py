#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ipaddress import IPv4Address
from os import mkdir, remove
from sys import stderr
from threading import Thread
from time import sleep
from typing import Dict, List, Tuple, Union

from loguru import logger
from maxminddb import open_database
from maxminddb.reader import Reader
from requests import get

import config


class ProxyScraperChecker(object):
    def __init__(
        self,
        geolite2_city_mmdb: str = None,
        http_sources: Union[Tuple[str, ...], str, None] = None,
        ip_service: str = "https://ident.me",
        socks4_sources: Union[Tuple[str, ...], str, None] = None,
        socks5_sources: Union[Tuple[str, ...], str, None] = None,
        timeout: float = 5,
    ) -> None:
        """Scrape and check proxies from sources and save them to a file.

        Args:
            geolite2_city_mmdb (str): Path to the GeoLite2-City.mmdb if you
                want to add location info for each proxy.
            ip_service (str): Service for getting your IP address and checking
                if proxies are valid.
            timeout (float): How many seconds to wait for the connection.
        """
        self.IP_SERVICE = ip_service.strip()
        self.MY_IP = get(self.IP_SERVICE).text.strip()
        self.sources = {}
        if http_sources:
            self.sources["http"] = self.prepare_sources(http_sources)
        if socks4_sources:
            self.sources["socks4"] = self.prepare_sources(socks4_sources)
        if socks5_sources:
            self.sources["socks5"] = self.prepare_sources(socks5_sources)
        self.protocols = self.sources.keys()
        self.all_proxies: Dict[str, List[str]] = {}
        # Dict[protocol, Dict[entry-node, exit-node]]
        self.working_proxies: Dict[str, Dict[str, str]] = {}
        for protocol in self.protocols:
            self.all_proxies[protocol] = []
            self.working_proxies[protocol] = {}
        self.TIMEOUT = timeout
        self.MMDB = geolite2_city_mmdb

    @staticmethod
    def prepare_sources(
        sources: Union[Tuple[str, ...], str]
    ) -> Tuple[str, ...]:
        """Remove duplicate sources or convert str to tuple."""
        return (sources,) if isinstance(sources, str) else tuple(set(sources))

    @staticmethod
    def is_ipv4(ip: str) -> bool:
        """Return True if ip is IPv4."""
        try:
            IPv4Address(ip)
        except Exception:
            return False
        return True

    @staticmethod
    def append_to_file(file_name: str, content: str) -> None:
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(f"{content}\n")

    @staticmethod
    def get_geolocation(ip: str, reader: Reader) -> str:
        """Get proxy's geolocation.

        Args:
            ip (str): Proxy's ip.
            reader (Reader): mmdb object.

        Returns:
            str: ::country::region::city
        """
        geolocation = reader.get(ip)
        try:
            country = geolocation.get("country")  # type: ignore
        except AttributeError:
            return "::None::None::None"
        if country is None:
            country = geolocation.get("continent")  # type: ignore
            if country is not None:
                country = country["names"]["en"]  # type: ignore
        else:
            country = country["names"]["en"]  # type: ignore
        region = geolocation.get("subdivisions")  # type: ignore
        if region is not None:
            region = region[0]["names"]["en"]  # type: ignore
        city = geolocation.get("city")  # type: ignore
        if city is not None:
            city = city["names"]["en"]  # type: ignore
        return f"::{country}::{region}::{city}"

    def start_threads(self, threads: List[Thread]) -> None:
        """Start and join threads."""
        for t in threads:
            try:
                t.start()
            except RuntimeError:
                sleep(self.TIMEOUT)
                t.start()
        for t in threads:
            t.join()

    def get_source(self, source: str, protocol: str) -> None:
        """Get proxies from source and append them to all_proxies.

        Args:
            source (str): Proxy list URL.
            protocol (str): http/socks4/socks5.
        """
        try:
            r = get(source.strip(), timeout=15)
        except Exception as e:
            logger.error(f"{source}: {e}")
            return
        status_code = r.status_code
        if status_code == 200:
            for proxy in r.text.splitlines():
                proxy = proxy.strip()
                if self.is_ipv4(proxy.split(":")[0]):
                    self.all_proxies[protocol].append(proxy)
        else:
            logger.error(f"{source} status code: {status_code}")

    def check_proxy(self, proxy: str, protocol: str) -> None:
        """Check proxy validity and append it to working_proxies.

        Args:
            proxy (str): ip:port.
            protocol (str): http/socks4/socks5.
        """
        proxy = proxy.replace(f"{protocol}://", "").replace("https://", "")
        try:
            ip = get(
                self.IP_SERVICE,
                proxies={
                    "http": f"{protocol}://{proxy}",
                    "https": f"{protocol}://{proxy}",
                },
                timeout=self.TIMEOUT,
            ).text.strip()
        except Exception:
            return
        if self.MY_IP != ip and self.is_ipv4(ip):
            self.working_proxies[protocol][proxy] = ip

    def get_all_sources(self) -> None:
        """Get proxies from sources and append them to all_proxies."""
        logger.info("Getting all sources")
        self.start_threads(
            [
                Thread(target=self.get_source, args=(source, protocol))
                for protocol in self.protocols
                for source in self.sources[protocol]
            ]
        )

    def check_all_proxies(self) -> None:
        """Check all_proxies and append working ones to working_proxies."""
        unique_proxies = {}
        for proto in self.protocols:
            unique_proxies[proto] = tuple(set(self.all_proxies[proto]))
            logger.info(
                "Checking {0} {1} proxies", len(unique_proxies[proto]), proto
            )
        self.start_threads(
            [
                Thread(target=self.check_proxy, args=(proxy, protocol))
                for protocol in self.protocols
                for proxy in unique_proxies[protocol]
            ]
        )

    def save_working_proxies(self) -> None:
        """Delete old proxies and save new ones."""
        for directory in (
            "proxies",
            "proxies_anonymous",
            "proxies_geolocation",
            "proxies_geolocation_anonymous",
        ):
            for file in ("http.txt", "socks4.txt", "socks5.txt"):
                try:
                    remove(f"{directory}/{file}")
                except FileNotFoundError:
                    try:
                        mkdir(directory)
                    except FileExistsError:
                        pass
        for protocol in self.protocols:
            self.working_proxies[protocol] = dict(
                sorted(
                    self.working_proxies[protocol].items(),
                    key=lambda x: tuple(
                        map(int, x[0].split(":")[0].split("."))
                    ),
                )
            )
            for proxy, ip in self.working_proxies[protocol].items():
                self.append_to_file(f"proxies/{protocol}.txt", proxy)
                if ip != proxy.split(":")[0]:
                    self.append_to_file(
                        f"proxies_anonymous/{protocol}.txt", proxy
                    )
        if self.MMDB:
            with open_database(self.MMDB) as reader:
                for protocol in self.protocols:
                    for proxy, ip in self.working_proxies[protocol].items():
                        line = proxy + self.get_geolocation(ip, reader)
                        self.append_to_file(
                            f"proxies_geolocation/{protocol}.txt", line
                        )
                        if ip != proxy.split(":")[0]:
                            self.append_to_file(
                                f"proxies_geolocation_anonymous/{protocol}.txt",
                                line,
                            )

    def main(self) -> None:
        self.get_all_sources()
        self.check_all_proxies()
        self.save_working_proxies()
        logger.success("Result:")
        for protocol in self.protocols:
            logger.info(
                "{0} {1} proxies",
                len(self.working_proxies[protocol]),
                protocol,
            )
        logger.success("Thank you for using proxy-scraper-checker :)")


def main() -> None:
    logger.remove()
    logger.add(
        stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{message}</level>",
        colorize=True,
    )
    client = ProxyScraperChecker(
        geolite2_city_mmdb="GeoLite2-City.mmdb"
        if config.GEOLOCATION
        else None,
        http_sources=config.HTTP_SOURCES if config.HTTP else None,
        ip_service=config.IP_SERVICE,
        socks4_sources=config.SOCKS4_SOURCES if config.SOCKS4 else None,
        socks5_sources=config.SOCKS5_SOURCES if config.SOCKS5 else None,
        timeout=config.TIMEOUT,
    )
    client.main()


if __name__ == "__main__":
    main()

# proxy-scraper-checker

Get and check free anonymous HTTP, SOCKS4, SOCKS5 proxies with geolocation info from different sources.

**You can get proxies obtained using this script in [monosans/proxy-list](https://github.com/monosans/proxy-list) (updated every ~15 minutes).**

## Note about git clone

To make `git clone` way faster use `--depth 1` flag.

## Usage

- Make sure `Python` version is 3.6 or higher.
- Install dependencies from `requirements.txt`.
- Edit `config.py` according to your preference.
- Run `main.py`.

## Folders description

When the script finishes running, the following folders will be created:

- `proxies` - proxies with any anonymity level.

- `proxies_anonymous` - anonymous proxies.

- `proxies_geolocation` - same as `proxies`, but including exit-node's geolocation.

- `proxies_geolocation_anonymous` - same as `proxies_anonymous`, but including exit-node's geolocation.

## Buy me a coffee

Ask for details in [Telegram](https://t.me/monosans) or [VK](https://vk.com/id607137534).

## License

Licensed under the MIT license.

This product includes GeoLite2 data created by MaxMind, available from http://www.maxmind.com.

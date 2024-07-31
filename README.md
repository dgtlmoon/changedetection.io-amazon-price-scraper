# Amazon price scraper plugin for changedetection.io

This small plugin enhances the **"Restock & Price detection"** website watch mode for amazon.com URLs.

A small scraper to get the price data from Amazon pages which can be used to improve the ["restock and price detection" mode in changedetection.io when monitoring Amazon prices](https://changedetection.io).

Because amazon.com does not use any normal/regular embedded product data (such as LD-JSON etc), this scraper will try to find the price by looking at the HTML.

This plugin only works with https://github.com/dgtlmoon/changedetection.io

Using this plugin you can see the Amazon product prices in your dashboard.

[![Dashboard screenshot of monitoring Amazon prices](https://raw.githubusercontent.com/dgtlmoon/changedetection.io/master/docs/restock-overview.png)](https://changedetection.io)

Then you can further set the different conditions to get notifications of price changes

[![Setting price change alerts](https://raw.githubusercontent.com/dgtlmoon/changedetection.io/master/docs/restock-settings.png)](https://changedetection.io)

Such as

- Minimum and maximum price alerts
- Threshold in % for price movement alerts

Then you can connect all your favourite notification services to get alerts when Amazon price changes such as Discord, Google Chat, Gotify, Line, Matrix, Microsoft teams, Microsoft Power, ntfy, Nextcloud, Office 365 and everythign else from https://github.com/caronc/apprise

It is _highly recommended_ to use the Chrome fetcher method with this plugin.

This plugin comes installed in changedetection.io since `0.46.03`



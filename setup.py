from setuptools import setup

setup(
    name="changedetection.io-amazon-price-scraper",
    version="0.031",
    packages=["cdio_amazon_restock_price_scraper"],
    long_description="A small scraper plugin to get the price data from Amazon pages which can be used to improve the 'restock and price detection' mode in changedetection.io",
    entry_points={
        "changedetectionio.restock_price_scraper": [
            "cdio_amazon_restock_price_scraper = cdio_amazon_restock_price_scraper.plugin:restock_price_scraper",
        ],
    },
)

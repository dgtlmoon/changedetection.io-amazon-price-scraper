from setuptools import setup

setup(
    name="changedetectionio_amazon_restock_price_scraper",
    version="0.1",
    packages=["cdio_amazon_restock_price_scraper"],
    entry_points={
        "changedetectionio.restock_price_scraper": [
            "cdio_amazon_restock_price_scraper = cdio_amazon_restock_price_scraper.plugin:restock_price_scraper",
        ],
    },
)

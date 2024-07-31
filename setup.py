from setuptools import setup

setup(
    name="changedetection.io-amazon-price-scraper",
    author="dgtlmoon",
    url='https://changedetection.io',
    author_email="dgtlmoon@gmail.com",
    version="0.035",
    packages=["cdio_amazon_restock_price_scraper"],
    install_requires=["changedetection.io"],
    python_requires=">= 3.10",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='amazon price restock detection notification price change alerts',
    entry_points={
        "changedetectionio.restock_price_scraper": [
            "cdio_amazon_restock_price_scraper = cdio_amazon_restock_price_scraper.plugin:restock_price_scraper",
        ],
    },
)

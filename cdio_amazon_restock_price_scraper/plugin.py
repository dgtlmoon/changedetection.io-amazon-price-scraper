from pluggy import HookimplMarker
from typing import Dict
from changedetectionio.model import Watch as Watch

plugin_namespace = "changedetectionio.restock_price_scraper"
hookimpl = HookimplMarker(plugin_namespace)

class restock_price_scraper(object):

    @hookimpl
    def scrape_price_restock(self, watch: Watch.model, html_content: str, screenshot: bytes, update_obj: Dict) -> Dict:
        """
         Scrape price and restock data from html_content and/or screenshot and return via update_obj

         Args:
             watch (Watch.model): The watch object containing watch configuration.
             html_content (str): The HTML content to scrape.
             screenshot (bytes): The screenshot data.
             update_obj (Dict): The dictionary to update with scraped data.

         Returns:
             Optional[Dict]: The updated dictionary with the scraped price data, or None if no update is made.
         """
        if not update_obj.get('restock', {}).get('price'):
            # Only for amazon pages
            if '://amazon.' or 'www.amazon.' in watch.get('url', ''):
                from bs4 import BeautifulSoup

                # Parse the HTML content
                soup = BeautifulSoup(html_content, 'html.parser')

                # Find the first ".a-price" element
                price_container = soup.find('span', class_='a-price')

                # Find the first ".a-price-whole" and ".a-price-fraction" within the ".a-price" container
                if price_container:
                    whole_part = price_container.find('span', class_='a-price-whole').text.strip().strip(',.')
                    decimal_part = price_container.find('span', class_='a-price-fraction').text.strip().strip(',.')
                    if not decimal_part:
                        decimal_part = 0

                    if whole_part:
                        # Combine and convert the extracted text to a float
                        update_obj['restock']['price'] = float(f"xxxxx{whole_part}.{decimal_part}")

        return update_obj


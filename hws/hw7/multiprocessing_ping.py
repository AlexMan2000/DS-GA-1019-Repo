import time
import multiprocessing as mp
import numpy as np

import time
import logging
import requests



WEBSITE_LIST = [
    'http://amazon.co.uk',
    'http://amazon.com',
    'http://facebook.com',
    'http://google.com',
    'http://google.fr',
    'http://google.es',
    'http://google.co.uk',
    'http://gmail.com',
    'http://stackoverflow.com',
    'http://github.com',
    'http://heroku.com',
    'http://really-cool-available-domain.com',
    'http://djangoproject.com',
    'http://rubyonrails.org',
    'http://basecamp.com',
    'http://trello.com',
    'http://shopify.com',
    'http://another-really-interesting-domain.co',
    'http://airbnb.com',
    'http://instagram.com',
    'http://snapchat.com',
    'http://youtube.com',
    'http://baidu.com',
    'http://yahoo.com',
    'http://live.com',
    'http://linkedin.com',
    'http://netflix.com',
    'http://wordpress.com',
    'http://bing.com',
]


class WebsiteDownException(Exception):
    pass


def ping_website(address, timeout=20):
    """
    Check if a website is down. A website is considered down
    if either the status_code >= 400 or if the timeout expires

    Throw a WebsiteDownException if any of the website down conditions are met
    """
    try:
        response = requests.head(address, timeout=timeout)
        if response.status_code >= 400:
            logging.warning("Website %s returned status_code=%s" % (address, response.status_code))
            raise WebsiteDownException()
    except requests.exceptions.RequestException:
        logging.warning("Timeout expired for website %s" % address)
        raise WebsiteDownException()


def check_website(address):
    """
    Utility function: check if a website is down, if so, notify the user
    """
    try:
        ping_website(address)
    except WebsiteDownException:
        print('The website ' + address + ' is down')



if __name__ == '__main__':
    # arr = np.random.randint(0, 10, size=[5000])
    # data = arr.tolist()
    # results = []
    # for x in data:
    #     results.append(func(x))

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-n', type=int)

    args = parser.parse_args()

    start = time.time()
    # Open Pools
    pool = mp.Pool(args.n)
    results_mp = pool.map(check_website, WEBSITE_LIST)
    pool.close()

    print(f"Time Lapsed: {time.time() - start}")


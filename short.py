#!/usr/bin/env python
# vim:fileencoding=utf-8
"""
Shorten public urls using Bit.ly
"""
try:
    import os
    import ConfigParser
    import argparse
    import bitly_api
    from urlparse import urlparse
except ImportError, e:
    raise Exception('Required module missing: %s' % e.args[0])


def get_bitly_connection(apikey):
    """Connect using the api connection"""
    try:
        bitly = bitly_api.Connection('ncbi', apikey)
        return bitly
    except: 
        print "Sorry, couldn't create the api connection"


def read_ini():
    """Read the ini file to get things like the bitly api key, etc."""
    try:
        conf = ConfigParser.ConfigParser()
        filename = os.path.join(os.path.dirname(__file__), 'short.ini')
        conf.readfp(open(filename))
        apikey = conf.get('bitly', 'api_key')
        return apikey

    except IOError, e:
        print "Sorry, couldn't read the short.ini file, %s" % e

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Shorten public urls using Bit.ly')
    parser.add_argument('url', metavar='url', type=urlparse, help='The url to be shortened')
    args = parser.parse_args()
    return args.url.geturl()


def shorten_url(url):
    """Main method to read ini, get connection, then shorten url"""
    apikey = read_ini()
    bitly = get_bitly_connection(apikey)
    short = bitly.shorten(url)
    return short


if __name__ == '__main__':
    url = parse_args()
    short = shorten_url(url)
    print "Your shortened version of\n\n%s\nis\n%s\n" % (url, short['url'])

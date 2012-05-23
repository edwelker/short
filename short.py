#!/usr/bin/env python
# vim:fileencoding=utf-8
"""
Shorten public urls using Bit.ly
"""
try:
    import ConfigParser
    import bitly_api
    import argparse
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
        conf.readfp(open('short.ini'))
        apikey = conf.get('bitly', 'api_key')
        return apikey

    except IOError:
        print "Sorry, couldn't read the short.ini file"

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Shorten public urls using Bit.ly')
    parser.add_argument('url', metavar='url', type=urlparse, help='The url to be shortened')
    args = parser.parse_args()
    return args.url.geturl()



if __name__ == '__main__':
    url = parse_args()
    apikey = read_ini()
    bitly = get_bitly_connection(apikey)
    short = bitly.shorten(url)
    print "Your shortened version of\n\n%s\nis\n%s\n" % (url, short['url'])

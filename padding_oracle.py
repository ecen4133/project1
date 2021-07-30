#!/usr/bin/python3

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage: %s ORACLE_URL CIPHERTEXT_HEX" % (sys.argv[0]), file=sys.stderr)
        sys.exit(-1)
    oracle_url = sys.argv[1]
    ciphertext = sys.argv[2]

    # Example check of ciphertext at the oracle URL:
    r = requests.get("%s?message=%s" % (oracle_url, bytes.fromhex(ciphertext).hex()))
    r.raise_for_status()
    obj = r.json()
    print(obj)


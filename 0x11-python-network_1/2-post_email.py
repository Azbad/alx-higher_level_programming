#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter
and displays the body of the response (decoded in utf-8).
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
        url = sys.argv[1]
            email = sys.argv[2]
                data = urllib.parse.urlencode({'email': email}).encode('ascii')

                    request = urllib.request.Request(url, data)

                        with urllib.request.urlopen(request) as response:
                                    body = response.read()
                                            print(body.decode('utf-8'))

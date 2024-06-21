# backend/security_check.py

import requests
from urllib.parse import urlparse
import ssl
import socket
import datetime

def is_https(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme == 'https'

def get_ssl_expiry_date(url):
    hostname = urlparse(url).hostname
    context = ssl.create_default_context()
    
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            ssl_info = ssock.getpeercert()
            expiry_date_str = ssl_info['notAfter']
            expiry_date = datetime.datetime.strptime(expiry_date_str, '%b %d %H:%M:%S %Y %Z')
            return expiry_date

def has_valid_ssl_certificate(url):
    try:
        expiry_date = get_ssl_expiry_date(url)
        return expiry_date > datetime.datetime.now()
    except Exception as e:
        print(f"SSL certificate check failed: {e}")
        return False

def get_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        return {
            'Strict-Transport-Security': headers.get('Strict-Transport-Security', None),
            'Content-Security-Policy': headers.get('Content-Security-Policy', None),
            'X-Content-Type-Options': headers.get('X-Content-Type-Options', None),
            'X-Frame-Options': headers.get('X-Frame-Options', None),
            'X-XSS-Protection': headers.get('X-XSS-Protection', None),
        }
    except Exception as e:
        print(f"Failed to fetch security headers: {e}")
        return {}

def check_website_security(url):
    results = {
        'is_https': is_https(url),
        'has_valid_ssl_certificate': has_valid_ssl_certificate(url),
        'security_headers': get_security_headers(url)
    }
    return results

import requests
import socket
from urllib.parse import urlparse, urlsplit
import os
import pandas as pd
import warnings


def get_len(url: str):
    return len(url)

def count_dots(url: str):
    return url.count('.')

def get_hostname(url):
    # Remove the scheme from the URL
    if "://" in url:
        url = url.split("://")[1]

    # Split the URL by slashes
    url_parts = url.split("/")

    # The hostname is the first part of the URL
    hostname = url_parts[0]

    return hostname

def get_path_level(url: str):
    path = urlsplit(url).path

    return len(path.split('/'))


def count_subdomains(url: str):
    # Split the hostname by dots
    hostname = get_hostname(url)
    parts = hostname.split(".")

    # The number of subdomains is equal to the number of parts minus one
    num_subdomains = len(parts) - 1

    return num_subdomains

def count_slash(url: str):
    return url.count('/')

def count_dash(url: str):
    return url.count('-')


def count_dash_hostname(url: str):
    hostname = get_hostname(url)

    return hostname.count('-')

def check_at_symbol(url: str):
    return '@' in url

def check_tilde_symbol(url: str):
    return '~' in url

def count_underscore(url: str):
    return url.count('_')

def count_percent(url: str):
    return url.count('%')

def count_query_components(url: str):
    # Find the start of the query string
    query_start = url.find("?")

    if query_start == -1:
        # There are no query components in the URL
        return 0

    # Extract the query string from the URL
    query_string = url[query_start+1:]

    # Split the query string into components
    query_components = query_string.split("&")

    # Count the number of query components
    num_query_components = len(query_components)

    return num_query_components

def count_ampersand(url: str):
    return url.count('&')

def count_hash(url: str):
    return url.count('#')

def count_digits(url: str):
    num_digits = 0
    for char in url:
        if char.isdigit():
            num_digits += 1

    return num_digits

def check_no_Https(url: str):
    if not url.startswith(('http://', 'https://', 'ftp://')):
        url = 'http://' + url

    try:
        req = requests.get(url, timeout=1).url
        return req.startswith('https')

    except requests.exceptions.ConnectionError:
        return True
    
    except requests.exceptions.ReadTimeout:
        return True
    

def check_IP_address(url: str):
    try:
        host = get_hostname(url)
        ip = socket.gethostbyname(host)
        return ip in url

    except socket.error:
        return str(None)


def is_tld_used_in_subdomain(url: str):
    hostname = url.split("//")[-1].split("/")[0]
    domain_parts = hostname.split(".")
    subdomain = domain_parts[0]
    tld = domain_parts[-1]
    cctld = domain_parts[-2] if len(domain_parts) > 2 else ""

    # Check if the TLD or ccTLD is used in the subdomain
    return subdomain.endswith("." + tld) or subdomain.endswith("." + cctld)


def is_tld_used_in_link(url: str):
    # Extract the domain and path from the URL
    domain = url.split("//")[-1].split("/")[0]
    path = url.split("//")[-1][len(domain):]

    # Extract the TLD and ccTLD from the domain
    tld = domain.split(".")[-1]
    cctld = domain.split(".")[-2] if len(domain.split(".")) > 1 else ""

    # Check if the TLD or ccTLD is used in the link
    return tld in path or cctld in path


def is_https_disordered(url: str, flag: bool):
    if flag == False:
        parsed_url = urlparse(url)

        hostname = parsed_url.hostname
        try:
            https_index = hostname.rfind('https')

            if https_index != -1:
                return True
            else:
                return False
        except AttributeError:
            return None

    return None

def get_hostname_length(url: str):
    hostname = get_hostname(url)
    return len(hostname)


def get_path_length(url: str):
    parsed_url = urlparse(url)
    return len(parsed_url.path)


def get_query_length(url):
    parsed_url = urlparse(url)
    return len(parsed_url.query)


def check_double_slash(url: str):
    return '//' in url

def get_type_url(url: str):
    if url == 'benign':
        return 0
    else:
        return 1

if __name__ == '__main__':
    dataset_folder = "\\datasets"
    dataset_file = "\\malicious_url_balanced.csv"
    features_df_dataset = "\\url_features.csv"

    if os.name != 'nt':
        dataset_folder = "/datasets"
        dataset_file = "/malicious_url_balanced.csv"
        features_df_dataset = "/url_features.csv"

    dataset_dir = os.path.dirname(os.path.abspath( __file__)) + dataset_folder + dataset_file
    features_dataset_dir = os.path.dirname(os.path.abspath(__file__)) + dataset_folder + features_df_dataset

    df = pd.read_csv(dataset_dir)

    features_df = pd.DataFrame({'numDots':[], 'subdomainLevel':[], 'pathLevel':[], 'urlLength':[],
                                'numDash':[], 'numDashHostname':[], 'atSymbol':[], 'tildeSymbol':[],
                                'numUnderscore':[], 'numPercent':[], 'numQueryComponents':[], 'numApersand':[],
                                'numHash':[], 'numNumericChars':[], 'noHttps':[], 'ipAddress':[], 
                                'domainInSubdomains':[], 'domainInPaths':[], 'httpsInHostname': [], 'hostNameLength': [],
                                'pathLength':[], 'queryLength': [], 'doubleSlash': [], 'type': []})
    
    for index, row in df.iterrows():
        warnings.filterwarnings('ignore')

        url_i = row['url']
        url_type_i = row['type']

        path_level = get_path_level(url_i)
        len_url = get_len(url_i)
        dots = count_dots(url_i)
        hostname = get_hostname(url_i)
        subdomains = count_subdomains(url_i)
        slash = count_slash(url_i)
        dash = count_dash(url_i)
        dash_hostname = count_dash_hostname(url_i)
        at_symbol = check_at_symbol(url_i)
        tile_symbol = check_tilde_symbol(url_i)
        undersocres = count_underscore(url_i)
        percents = count_percent(url_i)
        query_components = count_query_components(url_i)
        ampersands = count_ampersand(url_i)
        hashes = count_hash(url_i)
        digits = count_digits(url_i)
        no_https = check_no_Https(url_i)
        check_ip = check_IP_address(url_i)
        is_tld = is_tld_used_in_subdomain(url_i)
        is_link = is_tld_used_in_link(url_i)
        https_disordered = is_https_disordered(url_i,no_https)
        hostname_length = get_hostname_length(url_i)
        path_length = get_path_length(url_i)
        query_length = get_query_length(url_i)
        double_slash = check_double_slash(url_i)
        url_type = get_type_url(url_type_i)

        url_i_features = [dots, subdomains, path_level, len_url, dash, dash_hostname, 
                            at_symbol, tile_symbol, undersocres, percents, query_components,
                                ampersands, hashes, digits, no_https, check_ip, is_tld, is_link, 
                                    https_disordered, hostname_length, path_length, query_length, double_slash, url_type]
        
        print(url_i_features)
        features_df = features_df.append(pd.Series(url_i_features, index=features_df.columns), ignore_index = True)
        features_df.to_csv(features_dataset_dir)
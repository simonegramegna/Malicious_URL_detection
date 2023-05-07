import requests
import tldextract
from urllib.parse import urlparse, urlsplit
import os
import pandas as pd
import warnings


#
# Number of character '.' in URL
# Return: numeric
#
def count_dots(url: str):
    return url.count('.')


#
# Number of subdomain levels
# Return: numeric
#
def count_subdomains(url: str):
    subdomain = tldextract.extract(url).subdomain
    return len(subdomain.split('.')) if len(subdomain) != 0 else 0


#
# The depth of URL
# Return: numeric
#
def get_path_level(url: str):
    path = urlsplit(url).path
    path = path[1:] if len(path) > 0 and path[0] == '/' else path
    path = path[:-1] if len(path) > 0 and path[-1] == '/' else path
    return len(path.split('/')) if len(path) > 0 else 0


#
# The length of URL
# Return: numeric
#
def get_len(url: str):
    return len(url)


#
# Number of the dash character '-' in URL
# Return: numeric
#
def count_dash(url: str):
    return url.count('-')


#
# There exists a character '@' in URL
# Return: boolean
#
def check_at_symbol(url: str):
    return '@' in url


#
# There exists a character '~' in URL
# Return: boolean
#
def check_tilde_symbol(url: str):
    return '~' in url


#
# Number of the underscore character '_' in URL
# Return: numeric
#
def count_underscore(url: str):
    return url.count('_')


#
# Number of the percent character '%' in URL
# Return: numeric
#
def count_percent(url: str):
    return url.count('%')


#
# Number of the query components
# Return: numeric
#
def count_query_components(url: str):
    query_components = urlparse(url).query.split("&") if len(urlparse(url).query) > 0 else ''
    return len(query_components)


#
# Number of the ampersand character '&' in URL
# Return: numeric
#
def count_ampersand(url: str):
    return url.count('&')


#
# Number of the hash character '#' in URL
# Return: numeric
#
def count_hash(url: str):
    return url.count('#')


#
# Number of the numeric character
# Return: numeric
#
def count_digits(url: str):
    return sum(c.isdigit() for c in url)


#
# Check if there exists a HTTPS in website URL
# Return: boolean
#
def check_Https(url: str):
    try:
        req = requests.get(url, timeout=1).url
        return req.startswith('https')
    except Exception as e:
        return False


#
# Check if the IP address is used in the hostname of the website URL
# Return: boolean
#
def check_IP_address(url: str):
    return not bool(sum(not c.isdigit() and c != '.' for c in tldextract.extract(url).domain))


#
# Check if TLD is used as a part of the subdomain in website URL
# Return: boolean
#
def check_tld_in_subdomain(url: str):
    res = tldextract.extract(url)
    return res.domain in res.subdomain


#
# Check if TLD is used in the link of website URL
# Return: boolean
#
def check_tld_in_path(url: str):
    return tldextract.extract(url).domain in urlsplit(url).path


#
# Check if HTTPS is disordered in the hostname of website URL
# Return: boolean
#
def check_https_in_hostname(url: str):
    return 'https' in urlsplit(url).netloc


#
# Length of hostname
# Return: numeric
#
def get_hostname_length(url: str):
    return len(urlsplit(url).netloc)


#
# Length of the link path
# Return: numeric
#
def get_path_length(url: str):
    return len(urlparse(url).path)


#
# Length of the query string
# Return: numeric
#
def get_query_length(url):
    return len(urlparse(url).query)


#
# There exists a slash '//' in the link path
# Return: boolean
#
def check_double_slash_in_path(url: str):
    return '//' in urlparse(url).path


#
# Compute the lexical features by URL
# Return: Pandas.Series
#
def get_lexical_features(url, label):
    if not url.startswith(('http://', 'https://', 'ftp://')):
        url = 'http://' + url
    return [
        url,
        count_dots(url),
        count_subdomains(url),
        get_path_level(url),
        get_len(url),
        count_dash(url),
        check_at_symbol(url),
        check_tilde_symbol(url),
        count_underscore(url),
        count_percent(url),
        count_query_components(url),
        count_ampersand(url),
        count_hash(url),
        count_digits(url),
        check_Https(url),
        check_IP_address(url),
        check_tld_in_subdomain(url),
        check_tld_in_path(url),
        check_https_in_hostname(url),
        get_hostname_length(url),
        get_path_length(url),
        get_query_length(url),
        check_double_slash_in_path(url),
        label
    ]

if __name__ == '__main__':
    dataset_folder = "\\datasets"
    dataset_file = "\\urls_sampled.csv"
    features_df_dataset = "\\urls_with_features.csv"

    if os.name != 'nt':
        dataset_folder = "/datasets"
        dataset_file = "/urls_sampled.csv"
        features_df_dataset = "/urls_with_features.csv"

    dataset_dir = os.path.dirname(os.path.abspath( __file__)) + dataset_folder + dataset_file
    features_dataset_dir = os.path.dirname(os.path.abspath(__file__)) + dataset_folder + features_df_dataset

    df = pd.read_csv(dataset_dir)

    features_df = pd.DataFrame({
        'url':[],
        'numDots':[],
        'subdomainLevel':[],
        'pathLevel':[],
        'urlLength':[],
        'numDash':[], 
        'atSymbol':[],
        'tildeSymbol':[],
        'numUnderscore':[],
        'numPercent':[],
        'numQueryComponents':[],
        'numApersand':[],          
        'numHash':[],
        'numDigits':[],
        'https':[],
        'ipAddress':[], 
        'domainInSubdomains':[],
        'domainInPaths':[],
        'httpsInHostname':[],
        'hostnameLength':[],
        'pathLength':[],
        'queryLength':[],
        'doubleSlash':[],
        'type': []
    })
    
    for index, row in df.iterrows():
        warnings.filterwarnings('ignore')
        url_i = row['url']
        url_type_i = row['type']

        if (index % 500 == 0):
            print('Rows processed: ',index)
        try:
            features_df.loc[index] = get_lexical_features(url_i, url_type_i)
        except Exception as e:
            print('>>>>>>> EXCEPTION: ',e)
            print('>>>>>>> EXCEPTION URL: ',url_i)
            print('>>>>>>> EXCEPTION INDEX: ',index)
            continue
        
    features_df.to_csv(features_dataset_dir, index = False)
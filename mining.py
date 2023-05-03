import requests
import socket

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

def count_subdomains(hostname: str):
    # Split the hostname by dots
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

def count_query_components(url):
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
    req = requests.get(url).url
    return req.startswith('https')

def check_IP_address(url: str):
    ip = socket.gethostbyname(url)
    return ip in url


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


def is_https_disordered(url: str):
    # Extract the domain from the URL
    domain = url.split("//")[-1].split("/")[0]

    # Check if the letters "https" are disordered in the domain
    return "https" in domain and domain.index("https") != domain.index("h") + 1

def get_hostname_lenght(url: str):
    hostname = get_hostname(url)

    return len(hostname)


def get_path_length(url: str):
    # Find the index of the first slash after the domain
    domain_end_index = url.index("//") + 2
    uri_start_index = url.index("/", domain_end_index)

    # Find the index of the query string or fragment identifier, if present
    query_index = url.find("?")
    fragment_index = url.find("#")

    # Determine the end index of the path
    if query_index != -1 and (fragment_index == -1 or query_index < fragment_index):
        path_end_index = query_index
    elif fragment_index != -1:
        path_end_index = fragment_index
    else:
        path_end_index = len(url)

    # Extract the path from the URL and return its length
    path = url[uri_start_index:path_end_index]
    return len(path)


def get_query_length(url):
    # Find the index of the query string, if present
    query_start_index = url.find("?")
    if query_start_index == -1:
        # No query string found
        return 0

    # Find the index of the fragment identifier, if present
    fragment_index = url.find("#")

    # Determine the end index of the query string
    if fragment_index != -1:
        query_end_index = fragment_index
    else:
        query_end_index = len(url)

    # Extract the query string from the URL and return its length
    query = url[query_start_index+1:query_end_index]
    return len(query)


def check_double_slash(url: str):
    return '//' in url

if __name__ == '__main__':
    print("hello")
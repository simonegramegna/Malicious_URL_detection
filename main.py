import pandas as pd
from mining import *
import os

dataset_folder = "\datasets"
dataset_file = "\malicious_urls.csv"

if os.name != 'nt':
    dataset_folder = "/datasets"
    dataset_file = "/malicious_urls.csv"

dataset_dir = os.path.dirname(os.path.abspath(__file__)) + dataset_folder + dataset_file
df = pd.read_csv(dataset_dir)

i = 0

for i, row in df.iterrows():
    url_i = row['url']
    #url_i = url_i.encode('utf-8')

    len_i = get_len(url_i)
    dots = count_dots(url_i)
    h = get_hostname(url_i)
    cs = count_subdomains(url_i)
    csl = count_slash(url_i)
    cd = count_dash(url_i)
    cdh = count_dash_hostname(url_i)
    cat = check_at_symbol(url_i)
    ct = check_tilde_symbol(url_i)
    cu = count_underscore(url_i)
    cp = count_percent(url_i)
    cqp = count_query_components(url_i)
    ca = count_ampersand(url_i)
    ch = count_hash(url_i)
    cdi = count_digits(url_i)
    chhtps = check_no_Https(url_i)
    cip = check_IP_address(url_i)
    istld = is_tld_used_in_subdomain(url_i)
    islink = is_tld_used_in_link(url_i)
    idd = is_https_disordered(url_i, chhtps)
    glh = get_hostname_lenght(url_i)
    gpl = get_path_length(url_i)
    gql = get_query_length(url_i)
    cds = check_double_slash(url_i)



    print(len_i)
    print(dots)
    print(h)
    print(cs)
    print(csl)
    print(cd)
    print(cdh)
    print(cat)
    print(ct)
    print(ct)
    print(cu)
    print(cp)
    print(cqp)
    print(ca)
    print(ch)
    print(cdi)
    print(chhtps)
    print(cip)
    print(istld)
    print(islink)
    print(idd)
    print(glh)
    print(gpl)
    print(gql)
    print(cds)


    print("\n\n")



    i = i + 1

    if i == 100:
        break
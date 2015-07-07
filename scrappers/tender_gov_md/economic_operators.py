import re
import requests
import urllib
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

url = "http://tender.gov.md/ro/operatorii-economici-calificati?title=&field_indp_idno_value=&field_forma_organizatorico_"\
      "jurid_tid=All&field_genurile_de_activitate_des_value="
urls = [url]
visited = [url]
while len(urls) > 0:
    try:
        html_text = urllib.request.urlopen(urls[0]).read()
    except:
        print(urls[0])
    soup = BeautifulSoup(html_text)

    urls.pop(0)
    print(len(urls))

    for tag in soup.findAll('a', href=True):
        tag['href'] = urllib.parse.urljoin(url, tag['href'])
        if url in tag['href'] and tag['href'] not in visited:
            urls.append(tag['href'])
            visited.append(tag['href'])

print(visited)

regex = "(http://tender.gov.md/ro/content/[a-z,0-9]{2,})"
patten = re.compile(regex)
true_links = re.findall(patten, visited)
print(true_links)




'''
for url in visited:
        source_code = requests.get(url)
        source_text = source_code.text
        soup = BeautifulSoup(source_text)
        all_text = soup.get_text(separator=':', strip=True)
        print(all_text)
        regex = "((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).(?:[0-9]{1,5}))"
        pattern = re.compile(regex)
        all_ip = re.findall(pattern, all_text)

        #all_ip = [word.replace(" %s ", ':') for word in all_ip]
        print(all_ip)
        for item in all_ip:
            fw = open('Ip_list.txt', 'a')
            fw.write("%s\n" % item)
            fw.close()
            '''
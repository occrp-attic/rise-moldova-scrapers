import json
import requests
import urllib
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

#url = "http://tender.gov.md/ro/operatorii-economici-calificati?page=%s"

def spider_web(max_pages):
    page = 0
    links = []
    true_links = []
    dict = {'Name': '', 'Form_organiz': '', 'Address': '', 'Description': '', 'Idno': '', 'Nr_atrib': ''}
    list_of_dict = []
    while page <= max_pages:
        url = "http://tender.gov.md/ro/operatorii-economici-calificati?page=%s"
        url = url % page
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', href=True):
            href = "http://tender.gov.md" + link.get('href')
            links.append(href)

        page += 1
    #print(links)
    for items in links:
        if items.startswith("http://tender.gov.md/ro/content/"):
            true_links.append(items)
    #print(true_links)
    for urls in true_links:
        source_code = requests.get(urls)
        source_text = source_code.text
        soup = BeautifulSoup(source_text)
        for title in soup.findAll('h1', {'id': 'page-title'}):
            #print(str(title.string).encode())
            dict['Name'] = str(title.string).encode()
        for addres in soup.findAll('div', {'class': 'field field-name-field-adresa-juridic-rela-ii-de- field-type-text-'\
        'long field-label-above'}):
            soup1 = BeautifulSoup(str(addres))
            for sexting in soup1.findAll('div', {'class': 'field-items'}):
                soup2 = BeautifulSoup(str(sexting))
                html_text = soup2.get_text()
                #print(html_text.encode())
                dict['Address'] = html_text.encode()
        for description in soup.findAll('div', {'class': 'field field-name-field-genurile-de-activitate-des field-type-'\
                                                             'text-with-summary field-label-above'}):
            soup3 = BeautifulSoup(str(description))
            for final_string in soup3.findAll('div', {'class': 'field-items'}):
                soup4 = BeautifulSoup(str(final_string))
                last = soup4.get_text()
                #print(last.encode())
                dict['Description'] = str(last).encode()
        for idno in soup.findAll('div', {'class': 'field field-name-field-indp-idno field-type-text field-label-inline clearfix'}):
            soup6 = BeautifulSoup(str(idno))
            for idno2 in soup6.findAll('div', {'class': 'field-items'}):
                soup7 = BeautifulSoup(str(idno2))
                idno_text = soup7.get_text()
                #print(idno_text.encode())
                dict['Idno'] = str(idno_text).encode()
        for form_organ in soup.findAll('div', {'class': 'field field-name-field-forma-organizatorico-jurid field-type-'\
                                                        'taxonomy-term-reference field-label-inline clearfix'}):
            form_organ1 = BeautifulSoup(str(form_organ))
            for form_organ2 in form_organ1.findAll('div', {'class': 'field-items'}):
                form_organ3 = BeautifulSoup(str(form_organ2))
                form_organ4 = form_organ3.get_text()
                #print(form_organ4.encode())
                dict['Form_organiz'] = str(form_organ4).encode()
        for nr_atribution in soup.findAll('div', {'class': 'field field-name-field-nr-atribuit-nr-deciziei-ag field-'\
                                                           'type-text field-label-inline clearfix'}):
            nr_atribution1 = BeautifulSoup(str(nr_atribution))
            for nr_atribution2 in nr_atribution1.findAll('div', {'class': 'field-items'}):
                nr_atribution3 = BeautifulSoup(str(nr_atribution2))
                nr_atribution4 = nr_atribution3.get_text()
                #print(nr_atribution4.encode())
                dict['Nr_atrib'] = str(nr_atribution4).encode()
        list_of_dict.append(dict)
    return json.dumps(list_of_dict)




#spider_web(6)
with open('eo.json', 'w') as eo:
    eo.write(spider_web(6))



#def get_urls():



'''
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
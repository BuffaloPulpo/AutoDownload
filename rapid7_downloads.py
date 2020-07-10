import json
import os
import re

import requests

headers = {
    'X-Api-Key': '813ce51c-3906-4c46-9d71-9b4efe7fe932',
}

path1 = r"C:\Users\Niu\PycharmProjects\AutoDownload"
path2 = r"C:\Users\Niu\Desktop\all_rapid7datasets"


def get_the_quota_left():
    response = requests.get('https://us.api.insight.rapid7.com/opendata/quota/', headers=headers)
    content = response.content
    nr = content.decode("utf-8")
    res = json.loads(nr)
    quota_left = res['quota_left']
    return quota_left


def is_quota_available():
    quota_left = get_the_quota_left()
    if quota_left > 0:
        return True


def download_file(in_file):
    temp_file = r"2018-10-10-1539144250-redis_6379.csv.gz"
    full_filepath = 'https://us.api.insight.rapid7.com/opendata/studies/sonar.tcp/' + in_file + '/download/'

    response = requests.get(full_filepath, headers=headers)
    response_content = response.content
    response_content = response_content.decode('utf-8')
    response_content = json.loads(response_content)
    print(response_content)
    url = response_content['url']
    r = requests.get(url, allow_redirects=True)
    open(in_file, 'wb').write(r.content)


def get_set_files_from_rapid7_total():
    response_listing = requests.get('https://us.api.insight.rapid7.com/opendata/studies/sonar.tcp/', headers=headers)
    fileset_content = response_listing.content
    fileset_content = fileset_content.decode("utf-8")
    fileset_content = json.loads(fileset_content)
    file_list_rapid7 = fileset_content['sonarfile_set']
    file_set_rapid7 = set(file_list_rapid7)
    return file_set_rapid7


def get_set_files_from_rapid7_not_downloaded():
    file_set_rapid7 = get_set_files_from_rapid7_total()
    files1 = [f for f in os.listdir(path1) if re.match(r'.*\.csv.gz', f)]
    files1 = set(files1)
    files2 = [f for f in os.listdir(path2) if re.match(r'.*\.csv.gz', f)]
    files2 = set(files2)
    file_set_rapid7 = file_set_rapid7 - files1 - files2
    return file_set_rapid7


def get_set_files_from_rapid7_udp():
    response_listing = requests.get('https://us.api.insight.rapid7.com/opendata/studies/sonar.udp/', headers=headers)
    fileset_content = response_listing.content
    fileset_content = fileset_content.decode("utf-8")
    fileset_content = json.loads(fileset_content)
    file_list_rapid7 = fileset_content['sonarfile_set']
    file_set_rapid7 = set(file_list_rapid7)
    files1 = [f for f in os.listdir(path1) if re.match(r'.*\.csv.gz', f)]
    files1 = set(files1)
    files2 = [f for f in os.listdir(path2) if re.match(r'.*\.csv.gz', f)]
    files2 = set(files2)
    file_set_rapid7 = file_set_rapid7 - files1 - files2
    return file_set_rapid7


def get_set_rapid7_files_filter_not_downloaded(filter_word):
    set_files_from_rapid7 = get_set_files_from_rapid7_not_downloaded()
    filtered_set = set()
    for each in set_files_from_rapid7:
        if filter_word in each:
            filtered_set.add(each)
    return filtered_set


def get_set_rapid7_files_filter_total(filter_word):
    set_files_from_rapid7 = get_set_files_from_rapid7_total()
    filtered_set = set()
    for each in set_files_from_rapid7:
        if filter_word in each:
            filtered_set.add(each)
    return filtered_set


def data_collection_progress(filter_word):
    files_rapid7_not_downloaded = get_set_rapid7_files_filter_not_downloaded(filter_word)
    files_rapid7_total = get_set_rapid7_files_filter_total(filter_word)
    files_downloaded = files_rapid7_total - files_rapid7_not_downloaded

    if len(files_rapid7_total) > 0:
        percentage_downloaded = 100 * len(files_downloaded) / len(files_rapid7_total)
        print("For port {}, there are {} rapid7 files, {} downloaded, {:5.2f}% completed.".format(
            filter_word[1:-1],
            len(files_rapid7_total), len(files_downloaded), percentage_downloaded))
    # else:
    #     print("For {}, no file found on rapid7 server".format(filter_word[1:-1]))
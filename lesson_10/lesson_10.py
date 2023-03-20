import re
from datetime import datetime


def get_domain_names(file_name):
    domains = []
    with open(file_name) as my_file:
        for line in my_file:
            domains.append((line.strip())[1:])
    return domains


file_domains = 'domains.txt'
domain_names = get_domain_names(file_domains)
print(domain_names)


def get_surnames(file_name):
    surnames = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip().split('\t')
            surnames.append(line[1])
    return surnames


file_surnames = 'names.txt'
names = get_surnames(file_surnames)
print(names)


def get_dates(file_date):
    dates = []
    with open(file_date, 'r') as file:
        for line in file:
            line = line.strip()
            if (line != "\n") and (line != "") and (len(line) > 9):
                date = line.partition('-')[0]
                dates.append({"date": " ".join(date.rsplit())})

    return dates


authors = 'authors.txt'
datesFile = get_dates(authors)
print(datesFile)


def get_dates_modify(file_date):
    dates = []
    with open(file_date, 'r') as file:
        for line in file:
            line = line.strip()
            if (line != "\n") and (line != "") and (len(line) > 9):
                a_start = line.partition(' -')[0]
                a = line.partition('-')[0].rsplit()
                if not a[0].isalpha():
                    a[0] = "".join([re.sub('\D', "", i) for i in a[::3]])
                b = ",".join(a)
                if b[0].isdigit():
                    date = datetime.strptime(b, '%d,%B,%Y')
                else:
                    date = datetime.strptime(b, '%B,%Y')
                date_modified = date.strftime('%d/%m/%Y')
                result = {"date_original": a_start, "date_modified": date_modified}
                dates.append(result)

    return dates


datesFileModify = get_dates_modify(authors)
print(datesFileModify)
import re
from datetime import datetime


class File:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_domain_names(self):
        domains = []
        with open(self.file_name) as my_file:
            for line in my_file:
                domains.append((line.strip())[1:])
        return domains

    def get_surnames(self):
        surnames = []
        with open(self.file_name, 'r') as f:
            for line in f:
                line = line.strip().split('\t')
                surnames.append(line[1])
        return surnames

    def get_dates(self):
        dates = []
        with open(self.file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if (line != "\n") and (line != "") and (len(line) > 9):
                    date = line.partition('-')[0]
                    dates.append({"date": " ".join(date.rsplit())})

        return dates

    def get_dates_modify(self):
        dates = []
        with open(self.file_name, 'r') as file:
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


file_1 = File('domains.txt')
print(file_1.get_domain_names())

file_2 = File('names.txt')
print(file_2.get_surnames())

file_3 = File('authors.txt')
print(file_3.get_dates())
print(file_3.get_dates_modify())

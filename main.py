import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    c = 0
    list1 = []
    for row in reader:
        c += 1
        if c == 1:
            head = row
            continue
        fio = []
        str = []
        count = 0
        for el in row:
            count += 1
            if 0 < count < 4:
                fio.append(el)
        fio = [i for i in fio if i != ""]
        str = " ".join(fio)
        fio = str.split(" ")
        if len(fio) < 3:
            fio.append("")
        count = 0
        for el in row:
            count += 1
            if count > 3:
                fio.append(el)
        list1.append(fio)
    count1 = 0
    count2 = 0
    num = []
    for v1 in list1:
        count1 += 1
        countel = -1
        for el in v1:
            countel += 1
            if el == '':
                count2 = 0
                for v2 in list1:
                    count2 += 1
                    if count2 > count1:
                        if v2[0] in v1:
                            v1.pop(countel)
                            v1.insert(countel,v2[countel])
                            if countel == 6:
                                num.insert(0,count2 - 1)
for i in num:
    list1.pop(i)

pattern1 = r"\(?[а-я]+\.?\s?(\d+)\)?"
pattern2 = r"^(\+7|8)\s?\(?(\d{3})\)?[-|\s]?(\d{3})[-|\s]?(\d{2})[-|\s]?(\d{2})"
ch2 = r"+7(\2)\3-\4-\5"
ch1 = r"доб.\1"
for i in list1:
    res = re.sub(pattern2,ch2,i[5])
    res2 = re.sub(pattern1,ch1,res)
    i.pop(5)
    i.insert(5,res2)
list1.insert(0,head)
for i in list1:
    print(i)
with open("phonebook_raw_v2.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    for i in list1:
        writer.writerow(i)





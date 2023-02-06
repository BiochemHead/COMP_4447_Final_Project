import csv
import re


def split_difficulty(a):
    a_list=a.split('\\n')
    difficulty=a_list[0]
    r_list=a_list[1]
    if r_list[1].isalpha():
        rating = "None"
        no_rating = 0
    else:
        rating=float(r_list[1:4])
        no_rating=int(r_list[-2])
    area=(a_list[3:])
    return difficulty.strip(), rating, no_rating, area

def split_stars(strings):
    s2 = strings[4:-2]
    return s2

def split_dogs(b):
    b_list = b.split(',')
    if len(b_list) == 1:
        return b
    else:
        dogs = b_list[0]
        view = b_list[1].split(' · ')
        view 
        return dogs, view 

def split_rating(c):
    c1 = c.replace('\\n', '')
    c2 = c1.replace('\'', '')
    c3 = c2.replace(',' 'XX', '2')
    c3 = c3.strip()
    c3 = c3.split()
    s5 = split_stars(c3[5])
    s4 = split_stars(c3[6])
    s3 = split_stars(c3[7])
    s2 = split_stars(c3[8])
    s1 = split_stars(c3[9])
    res = re.sub("[A-Za-z]+", lambda ele: " " + ele[0] + " ", c3[-1])
    res = res.replace(' / ', 'XXXX')
    res = res.replace('%', ' ')
    res = res.replace('XXXX', '/')
    diffrating = res.split()
    return s5, s4, s3, s2, s1, diffrating

with open('test_df2.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    names=[]
    for row in reader:
        trail_name=row[0]
        one = split_difficulty(row[1])
        three = split_dogs(row[3])
        four = split_rating(row[4])
        names.append([trail_name, one, three, four, row[5][:-1], row[6][:-1], row[7], row[8], row[9][:-1], row[10][:-1], row[11][:-1], row[12][:-1]])
        
with open('cleaned_data.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(names)


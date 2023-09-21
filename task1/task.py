import csv
import json

def read_csv(filename: str):
    array=[]
    with open (filename, newline='') as t1:
        read = csv.reader(t1, delimiter=',')
        for row in read:
            array.append(row)
        return array

print(read_csv('example.csv')[2][2])

def read_json(filename: str):
    f = open(filename)
    j = json.load(f)
    return j

print(read_json('example.json')['str']['str1'][0])
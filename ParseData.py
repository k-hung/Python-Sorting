import os
import csv
import collections
from collections import Counter
def main():
    print('============================================================================')
    print('\n')
    print('     This  program allows you to see and explore a data set of Chicago.')
    print('\n')
    print('============================================================================')
    print('\n')
    options()


#GUI
def options():
    print('\n===== Options =====\n')
    print('1. Display stats for most common zipcodes.\n')
    print('2. Display stats for most common wards.\n')
    print('3. Display stats for most common Police Districts.\n')
    print('4. Display stats for most common application types.\n')
    print('5. Show a List of all Fire Stations.\n')
    print('6. Access function that counts requests within a certain day.\n')
    x = int(input('Please enter number of option or 0 to exit:'))
    if x == 1:
        ZipCount()
    elif x == 2:
        WardCount()
    elif x == 3:
        PoliceDistricts()
    elif x == 4:
        ApplicationTypes()
    elif x == 5:
        StationList()
    elif x == 6:
        dayData()
    elif x == 0:
        exit()
    else:
        os.system('clear')
        print('That is not a valid option. \nPlease enter a valid number.')
        options()

def ZipCount():
    os.system('clear')
    print('Starts for most common zipcodes')
    zipcodes=[]
    with open('Business Licenses.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[7] == 'CHICAGO':
                zipcodes.append(row[9])
        del zipcodes[0]
    zipCounts = Counter(zipcodes)
    x = input('Please enter from 1 to 10 your desired most common results, or press enter for all')
    print('Most common Zip Codes:')
    for zips, count in zipCounts.most_common(x):
        print ('%s: %d times.' % (zips, count))
    input('\nPress any key to return to Options.')
    options()


def WardCount():
    os.system('clear')
    print('Starts for most common ')
    wards=[]
    with open('Business Licenses.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[7] == 'CHICAGO':
                wards.append(row[10])
        del wards[0]
    wardCounts = Counter(wards)
    x = input('Please enter from 1 to 10 your desired most common results, or press enter for all')
    print('Most common Wards:')
    for ward, count in wardCounts.most_common(x):
        print ('%s: %d times.' % (ward, count))


def PoliceDistricts():
    os.system('clear')
    print('Starts for most common ')
    districts=[]
    with open('Business Licenses.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[7] == 'CHICAGO':
                districts.append(row[12])
        del districts[0]
    districtCount = Counter(districts)
    x = input('Please enter from 1 to 10 your desired most common results, or press enter for all')
    print('Most common Police Districts:')
    for district, count in districtsCount.most_common(x):
        print ('%s: %d times.' % (district, count))


def ApplicationTypes():
    os.system('clear')
    print('Starts for most common ')
    types=[]
    with open('Business Licenses.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[7] == 'CHICAGO':
                types.append(row[14])
        del types[0]
    typeCounts = Counter(types)
    x = input('Please enter from 1 to 10 your desired most common results, or press enter for all')
    print('Most common Application Types:')
    for type, count in typeCounts.most_common(x):
        print ('%s: %d times.' % (type, count))

def dayData():
    os.system('clear')
    print('Starts for date of most licenses issued.')
    dates=[]
    with open('Business Licenses.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[7] == 'CHICAGO':
                dates.append(row[24])
        del dates[0]
    dateCounts = Counter(dates)
    x = input('Please enter from 1 to 10 your desired top results, or press enter for all')
    print('Date of most licenses issued:')
    for date, count in dateCounts.most_common(x):
        print ('%s: %d times.' % (date, count))

main()

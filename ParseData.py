import os
import csv
import collections
from collections import Counter
def main():
    print('============================================================================')
    print('\n')
    print('  This program parses and sorts recorded data of issued business licenses.  ')
    print('\n')
    print('============================================================================')
    print('\n')
    options()


#GUI
def options():
    print('\n===== Options =====\n')
    print('1. Display data for most common zipcodes.\n')
    print('2. Display data for most common wards.\n')
    print('3. Display data for most common Police Districts.\n')
    print('4. Display data for most common application types.\n')
    print('5. Display data for most common license issue dates.\n')
    x = int(input('Please enter number of option or 0 to exit: '))
    if x == 1:
        ZipCount()
    elif x == 2:
        WardCount()
    elif x == 3:
        PoliceDistricts()
    elif x == 4:
        ApplicationTypes()
    elif x == 5:
        LicenseIssuedDate()
    elif x == 0:
        exit()
    else:
        print('That is not a valid option. \nPlease enter a valid number.')
        raw_input('\nPress any key to return to Options.')
        options()

def ZipCount():
    os.system('clear')
    print('Starts for most common zipcodes')
    zipcodes=[]
    with open('Business Licenses.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[7] == 'CHICAGO':
                if row[9] != '':
                    zipcodes.append(row[9])
        del zipcodes[0]
    zipCounts = Counter(zipcodes)
    x = input('Please enter your desired amount of top results or 0 for all data: ')
    print('Most common Zip Codes:')
    if x == 0:
        for zips, count in zipCounts.most_common():
            print ('%s: %d times.' % (zips, count))
    else:
        for zips, count in zipCounts.most_common(x):
            print ('%s: %d times.' % (zips, count))
    raw_input('\nPress any key to return to Options.')
    os.system('clear')
    options()


def WardCount():
    os.system('clear')
    print('Starts for most common ')
    wards=[]
    with open('Business Licenses.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[7] == 'CHICAGO':
                if row[10] != '':
                    wards.append(row[10])
        del wards[0]
    wardCounts = Counter(wards)
    x = input('Please enter your desired amount of top results or 0 for all data: ')
    print('Most common Wards:')
    if x == 0:
        for ward, count in zipCounts.most_common():
            print ('%s: %d times.' % (ward, count))
    else:
        for ward, count in wardCounts.most_common(x):
            print ('Ward#%s: %d times.' % (ward, count))
    raw_input('\nPress any key to return to Options.')
    os.system('clear')
    options()


def PoliceDistricts():
    os.system('clear')
    print('Starts for most common ')
    districts=[]
    with open('Business Licenses.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[7] == 'CHICAGO':
                if row[12] != '':
                    districts.append(row[12])
        del districts[0]
    districtCount = Counter(districts)
    x = input('Please enter your desired amount of top results or 0 for all data: ')
    print('Most common Police Districts:')
    if x == 0:
        for district, count in zipCounts.most_common():
            print ('%s: %d times.' % (district, count))
    else:
        for district, count in districtCount.most_common(x):
            print ('%s: %d times.' % (district, count))
    raw_input('\nPress any key to return to Options.')
    os.system('clear')
    options()


def ApplicationTypes():
    os.system('clear')
    print('Starts for most common ')
    types=[]
    with open('Business Licenses.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[7] == 'CHICAGO':
                if row[14] != '':
                    types.append(row[14])
        del types[0]
    typeCounts = Counter(types)
    x = input('Please enter your desired amount of top results or 0 for all data: ')
    print('Most common Application Types:')
    if x == 0:
        for type, count in zipCounts.most_common():
            print ('%s: %d times.' % (type, count))
    else:
        for type, count in typeCounts.most_common(x):
            print ('%s: %d times.' % (type, count))
    raw_input('\nPress any key to return to Options.')
    os.system('clear')
    options()

def LicenseIssuedDate():
    os.system('clear')
    print('Starts for date of most licenses issued.')
    dates=[]
    with open('Business Licenses.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[7] == 'CHICAGO':
                if row[24] != '':
                    dates.append(row[24])
        del dates[0]
    dateCounts = Counter(dates)
    x = input('enter your desired amount of top results or 0 for all data: ')
    print('Date of most licenses issued:')
    if x == 0:
        for date, count in zipCounts.most_common():
            print ('%s: %d times.' % (date, count))
    else:
        for date, count in dateCounts.most_common(x):
            print ('%s: %d times.' % (date, count))
    raw_input('\nPress any key to return to Options.')
    os.system('clear')
    options()

main()

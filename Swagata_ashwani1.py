# Swagata Ashwani
# Original Creation Date - 20171116
# Last Modified Date - 20171211
# Activity 1 of Course Project.  This program creates dictionaries and lists from input files.
# Then we update the lists with values from dictionaries.

import sys,collections, csv
from collections import Counter


# main function creates dictionaries and lists from input files.
# Then we update the lists with values from dictionaries.

def main():
    # read compound_file, convert to dict
    compound_d={}
    compound_file=csv.reader(open('compound_words.csv','r'))
    for row in compound_file:
        k,v = row
        compound_d[k]=v

    # users chooses if they want to see the compound file
    print("Welcome to Project Activity 1 - please make screen full for best results")
    inputFlag='x'
    while inputFlag!='y' and inputFlag!='Y' and inputFlag!='n' and inputFlag!='N':
        inputFlag=input("Press 'y' to see the file with Compound Components. Press 'n' to skip to the next step or 'q' to quit.")
        if inputFlag=='q' or inputFlag=='Q':
            sys.exit()
    print()
    # loop through compound dict and print
    if inputFlag=='Y' or inputFlag=='y':
        for k,v in compound_d.items():
            print("{:40s}-->\t{:40s}".format(k,v))
        print("------------------------------------------------------------------------------------")
    print()

    # read normalization file, conver to dict
    normalization_d={}
    normalization_file=csv.reader(open('normalization.csv','r'))
    for row in normalization_file:
        k,v = row
        normalization_d[k]=v

    inputFlag='x'
    while inputFlag!='y' and inputFlag!='Y' and inputFlag!='n' and inputFlag!='N':
        inputFlag=input("Press 'y' to see the file with Normalization components. Press 'n' to skip to the next step or 'q' to quit.")
        if inputFlag=='q' or inputFlag=='Q':
            sys.exit()
    print()
    # loop through normalization dict and print
    # print dict in columns of 2
    row_counter=0
    if inputFlag=='Y' or inputFlag=='y':
        for k,v in normalization_d.items():
            if row_counter % 2== 0 and row_counter > 0:
                print()
            print("{:20s}-->\t{:20s}\t\t".format(k,v),sep='|',end='')
            row_counter +=1
        print()
        print("------------------------------------------------------------------------------------")
    print()

    # read stemming file, convert to dict
    stemming_d={}
    stemming_file=csv.reader(open('stemming.csv','r'))
    for row in stemming_file:
        k,v = row
        stemming_d[k]=v

    inputFlag='x'
    while inputFlag!='y' and inputFlag!='Y' and inputFlag!='n' and inputFlag!='N':
        inputFlag=input("Press 'y' to see the file with STEMMING components. Press 'n' to skip to the next step or 'q' to quit.")
        if inputFlag=='q' or inputFlag=='Q':
            sys.exit()
    print()
    # loop through steming dict and print
    # print dict in columns of 2
    row_counter=0
    if inputFlag=='Y' or inputFlag=='y':
        for k,v in stemming_d.items():
            if row_counter % 2== 0 and row_counter > 0:
                print()
            print("{:25s}-->\t{:25s}\t\t".format(k,v),sep='|',end='')
            row_counter +=1
        print()
        print("------------------------------------------------------------------------------------")
    print()

    # read noise file convert to list
    noise_list=open('noise_words.csv','r').read().split('\n')

    # Reads file raw ticket into a string
    raw_file=open('Raw_Old_Tickets.txt','r')
    raw_tickets_str=raw_file.read().lower()
    raw_tickets_str=raw_tickets_str.strip('\n')
    raw_file.close()

    # loops through each key in compound dict, replaces in file string each instance of key with key-value
    for k in compound_d:
        raw_tickets_str=raw_tickets_str.replace(k,compound_d[k])

    # converts file string to list
    raw_tickets_list=raw_tickets_str.split()

    # removes non-alphanumeric characters at the end of each word like periods or semicolons or commas
    # will not remove the period in .net or 8.1 for example
    for a in range(len(raw_tickets_list)):
        word=raw_tickets_list[a]
        if word[len(word)-1].isalnum() == False:
            raw_tickets_list[a] = word[:len(word)-1]

    # Reads new ticket file into a string
    new_ticket_file=open('raw_compare_ticket.txt','r')
    new_ticket_str=new_ticket_file.read().lower()
    new_ticket_str = new_ticket_str.strip('\n')
    new_ticket_file.close()

    # loops through each key in compound dict, replaces in file string each instance of key with key-value
    for k in compound_d:
        new_ticket_str=new_ticket_str.replace(k,compound_d[k])

    # converts file string to list
    new_ticket_list=new_ticket_str.split()

    # removes non-alphanumeric characters at the end of each word like periods or semicolons or commas
    # will not remove the period in .net or 8.1 for example
    for a in range(len(new_ticket_list)):
        word=new_ticket_list[a]
        if word[len(word)-1].isalnum() == False:
            new_ticket_list[a] = word[:len(word)-1]

    # loops through ticket list, checks to see if item is a key in normalization dict
    # replaces list value with key-value
    for i in range(len(raw_tickets_list)):
        word = raw_tickets_list[i]
        if word in normalization_d.keys():
            raw_tickets_list[i]=normalization_d[word]

    # loops through new ticket list, checks to see if item is a key in normalization dict
    # replaces list value with key-value
    for i in range(len(new_ticket_list)):
        word = new_ticket_list[i]
        if word in normalization_d.keys():
            new_ticket_list[i]=normalization_d[word]

    # loops through ticket list, checks to see if item is a key in stemming dict
    # replaces list value with key-value
    for i in range(len(raw_tickets_list)):
        word = raw_tickets_list[i]
        if word in stemming_d.keys():
            raw_tickets_list[i]=stemming_d[word]

    # loops through new ticket list, checks to see if item is a key in stemming dict
    # replaces list value with key-value
    for i in range(len(new_ticket_list)):
        word = new_ticket_list[i]
        if word in stemming_d.keys():
            new_ticket_list[i]=stemming_d[word]

    # created new empty list and added items from ticket list that were not in noise list
    raw_tickets_clean_list=[]
    for a in raw_tickets_list:
        if a not in noise_list:
            raw_tickets_clean_list.append(a)
    raw_tickets_clean_list.sort()

    # created new empty list and added items from new ticket list that were not in noise list
    new_ticket_clean_list=[]
    for a in new_ticket_list:
        if a not in noise_list:
            new_ticket_clean_list.append(a)
    new_ticket_clean_list.sort()

    # Printing Scrubbed Lists
    inputFlag='n'
    while inputFlag!='y' and inputFlag!='Y':
        inputFlag=input("Press 'y' to see the scrubbed list of old tickets or 'q' to quit.")
        if inputFlag=='q' or inputFlag=='Q':
            sys.exit()
    print()
    print("The following is a list of previous tickets scrubbed performing:\nCompound Concepts, Normalization, Stemming, and Noise Words Removed")
    print("--------------------------------------------------------------------------")
    for a in range(len(raw_tickets_clean_list)):
        if (a) % 3 == 0 and a > 0:
            print()
        print('{:30s}'.format(raw_tickets_clean_list[a]),sep='|',end='')
    print()
    print("------------------------------------------------------------------------------------")
    print()
    # allow the user to decide when ready to go to the next step
    inputFlag='n'
    while inputFlag!='y' and inputFlag!='Y':
        inputFlag=input("Press 'y' to see the new ticket or 'q' to quit.")
        if inputFlag=='q' or inputFlag=='Q':
            sys.exit()
    print("The following is a list of new ticket scrubbed performing:\nCompound Concepts, Normalization, Stemming, and Noise Words Removed")
    print("--------------------------------------------------------------------------")
    for a in range(len(new_ticket_clean_list)):
        if (a) % 3 == 0 and a > 0:
            print()
        print('{:30s}'.format(new_ticket_clean_list[a]),sep='|',end='')
    print()
    print("------------------------------------------------------------------------------------")
    print()

# Call the main function
main()

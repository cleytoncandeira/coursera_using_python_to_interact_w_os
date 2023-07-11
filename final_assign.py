#!/usr/bin/env python3

import os
import re
import csv
from collections import defaultdict
from operator import itemgetter


error_counter = defaultdict(int)
error_user = defaultdict(int)
info_user = defaultdict(int)


def search_file():
    """Reads each line of the syslog.log file and checks if it is an error or an info message."""
    with open('syslog.log', "r") as myfile:
        for line in myfile:
            if " ERROR " in line:
                find_error(line)
                add_user_list(line, 1)
            elif " INFO " in line:
                add_user_list(line, 2)


def find_error(line):
    """If it is an error, it reads the error from the line and increments the error counter dictionary."""
    match = re.search(r"(ERROR [\w \[]*) ", line)
    if match is not None:
        error = match.group(0).replace("ERROR ", "").strip()
        if error == "Ticket":
            error = "Ticket doesn't exist"
        error_counter[error] += 1


def add_user_list(line, op):
    """Reads the user from the string and adds to the error or info user counter."""
    match = re.search(r'\(.*?\)', line)
    user = match.group(0).strip("()")
    if op == 1:
        error_user[user] += 1
    elif op == 2:
        info_user[user] += 1


def sort_dict_by_value(dictionary, reverse=True):
    """Sorts a dictionary by its values and returns a list of tuples."""
    return sorted(dictionary.items(), key=itemgetter(1), reverse=reverse)


def get_error_value(key):
    """Returns the value of a user in the error user dictionary, or 0 if the key doesn't exist."""
    return error_user.get(key, 0)


def write_csv(op):
    """Writes the CSV files."""
    if op == 1:
        with open('user_statistics.csv', 'w', newline='') as output:
            fieldnames = ['Username', 'INFO', 'ERROR']
            csv_writer = csv.DictWriter(output, fieldnames=fieldnames)
            csv_writer.writeheader()
            for key, value in info_user.items():
                val_error = get_error_value(key)
                csv_writer.writerow({'Username': key, 'INFO': value, 'ERROR': val_error})
    elif op == 2:
        with open('error_message.csv', 'w', newline='') as output:
            fieldnames = ['Error', 'Count']
            csv_writer = csv.DictWriter(output, fieldnames=fieldnames)
            csv_writer.writeheader()
            for key, value in error_counter.items():
                csv_writer.writerow({'Error': key, 'Count': value})


def add_zeros():
    """Adds zero to the other dictionary if a user is not a key."""
    for user in error_user.keys():
        info_user.setdefault(user, 0)
    for user in info_user.keys():
        error_user.setdefault(user, 0)


def main():
    """Executes the functions."""
    search_file()
    add_zeros()
    error_counter_sorted = sort_dict_by_value(error_counter)
    error_user_sorted = sort_dict_by_value(error_user, reverse=False)
    info_user_sorted = sort_dict_by_value(info_user, reverse=False)
    write_csv(1)
    write_csv(2)


if __name__ == "__main__":
    main()


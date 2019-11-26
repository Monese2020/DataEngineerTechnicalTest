#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Get Top Commiters to the Airflow Github Project."""
import argparse
import json

import requests


def get_airflow_commits(date):

    "your code here"

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Get the airflow commits at a given date")
    parser.add_argument('-d',
                        '--date',
                        type=str,
                        help='The date to be executed in the YYYYMMDD format. (Eg. 20180120)',
                        required=True)

    args = parser.parse_args()
    get_airflow_commits(args.date)

#!/usr/bin/env python3

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, SUPPRESS
import json
import os
from time import time
import sys

import datadog


def main(args):
    try:
        datadog_api_key = os.environ['DATADOG_API_KEY']
        datadog_app_key = os.environ['DATADOG_APP_KEY']
    except KeyError as e:
        print('Missing environment variable:', e, file=sys.stderr)
        print('Please see help for more info: fetch --help', file=sys.stderr)
        return 3

    datadog.initialize(api_key=datadog_api_key, app_key=datadog_app_key)

    end = int(time())
    start = end - args.period

    results = datadog.api.Metric.query(start=start, end=end, query=args.query)

    if args.out:
        with open(args.out, 'w') as fl:
            json.dump(results, fl)
    else:
        print(json.dumps(results))


def create_argparser():
    parser = ArgumentParser(
        description=
            'Fetches metric data from Datadog. '
            'To run this script, two environment variables are required: DATADOG_API_KEY and DATADOG_APP_KEY. '
            'See https://app.datadoghq.com/account/settings#api on how to obtain them.',
        formatter_class=
            ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('query', help='Metric query to fetch data from.')
    parser.add_argument('--period', type=int, default=3600, help='Time period over which you want to fetch data (in seconds).')
    parser.add_argument('--out', default=SUPPRESS, help='File name to store data to. Displays to terminal by default.')

    return parser


if __name__ == '__main__':
    sys.exit(main(create_argparser().parse_args()))

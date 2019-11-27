import sys
import os
import json
import requests
import psycopg2
import time

api_url = 'https://rem.eon.llc'
headers = {'content-type': 'application/json'}
table_name = ''

conn = psycopg2.connect(database='', user='', password='', host='', port='')
sql = "INSERT INTO {}(producer, cpu_usage_us, transaction_id, block_num, created_on) VALUES(%(producer)s, %(cpu_usage_us)s, %(transaction_id)s, %(block_num)s, %(created_on)s)".format(table_name)

def main():

    filepath = '/root/rem-benchmark/scripts/actions.log'
    records = []

    if not os.path.isfile(filepath):
            print('File path {} does not exist. Exiting...'.format(filepath))
            sys.exit()

    with  open(filepath, 'r') as fp:
        actions = fp.read()
        for action in actions.split('--action--'):
            record = {}
            lines = action.splitlines()

            if len(lines) > 4 and lines[4].startswith('executed'):
                record['transaction_id'] = lines[4].split()[2]
                record['created_on'] = lines[1]

                transaction = get_transaction(record['transaction_id'])

                # code is returned only in case of an error
                if 'code' in transaction:
                    continue

                for action in transaction['actions']:
                    if action['act']['account'] == 'rembenchmark' and action['act']['name'] == 'cpu':
                        record['cpu_usage_us'] = action['cpu_usage_us']
                        record['block_num'] = action['block_num']
                        record['producer'] = action['producer']

                records.append(record)
                time.sleep(.100)

        cur = conn.cursor()
        cur.executemany(sql, records)
        conn.commit()
        cur.close()
        conn.close()

        # empty the log file
        with open(filepath, 'w'):
            pass

def get_transaction(id):
    url = api_url + '/v2/history/get_transaction'
    params = {'id': id}
    request = requests.get(url, params=params)
    response = request.json()
    return response

if __name__ == '__main__':
        main()
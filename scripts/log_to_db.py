import sys
import os
import json
import requests
import psycopg2

api_url = 'https://testchain.remme.io'
headers = {'content-type': 'application/json'}

conn = psycopg2.connect(database='vmlucgke', user='oalabncu', password='8gHvnpKDdBPXa44XjzmAMAwmCtLCfgei3qwiDUkq', host='52.0.126.177', port='5432')
sql = "INSERT INTO benchmarks(producer, cpu_usage_us, transaction_id, block_num, created_on) VALUES(%(producer)s, %(cpu_usage_us)s, %(transaction_id)s, %(block_num)s, %(created_on)s)"

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

                record['cpu_usage_us'] = transaction['trx']['receipt']['cpu_usage_us']
                record['block_num'] = transaction['block_num']

                block = get_block(record['block_num'])

                record['producer'] = block['producer']

                records.append(record)

        cur = conn.cursor()
        cur.executemany(sql, records)
        conn.commit()
        cur.close()
        conn.close()

        # empty the log file
        with open(filepath, 'w'):
            pass

def get_transaction(id):
    url = api_url + '/v1/history/get_transaction'
    payload = '{"id": "' + id + '"}'
    request = requests.request("POST", url, data=payload, headers=headers)
    response = request.json()
    return response

def get_block(id):
    url = api_url + '/v1/chain/get_block'
    payload = '{"block_num_or_id": "' + str(id) + '"}'
    request = requests.request("POST", url, data=payload, headers=headers)
    response = request.json()
    return response

if __name__ == '__main__':
        main()
#!/usr/bin/env python3
import requests
import json
import dbus, argparse, subprocess

headers = {
    'Content-type': 'application/json',
}

horaireBus = requests.get('https://api-ratp.pierre-grimaud.fr/v4/schedules/buses/106/Les%2BMarronniers/R', headers=headers).json()
EtatRER = requests.get('https://api-ratp.pierre-grimaud.fr/v4/traffic/rers/A', headers=headers).json()

dumpJsonBus = json.dumps(horaireBus)
dumpJsonRER = json.dumps(EtatRER)

data_dictBus = json.loads(dumpJsonBus)
data_dictRER = json.loads(dumpJsonRER)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description='''\
Permet de récupérer les temps d'attente d'une ligne RATP''',
epilog='''\
Exemples d'utilisation:

-t1 pour avoir le premier arrêt.
-t2 pour avoir le second arrêt.
-d pour avoir la destination.
''')

parser.add_argument('-t1', '--time1', action='store_true', help='Get Time 1')
parser.add_argument('-t2', '--time2', action='store_true', help='Get Time 2')
parser.add_argument('-d', '--destination', action='store_true', help='Get Destination')
parser.add_argument('-rt', '--rertitre', action='store_true', help='Get RER message')
parser.add_argument('-rm', '--rermessage', action='store_true', help='Get RER Description')
args = parser.parse_args()

if args.time1:
    print(data_dictBus["result"]["schedules"][0]["message"])
if args.time2:
    print(data_dictBus["result"]["schedules"][1]["message"])
if args.destination:
    print(data_dictBus["result"]["schedules"][1]["destination"])
if args.rertitre:
    print(data_dictRER["result"]["title"])
if args.rermessage:
    print(data_dictRER["result"]["message"])

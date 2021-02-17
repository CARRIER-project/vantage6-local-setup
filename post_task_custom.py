from carrier import VantageClient
import time

HOST = 'http://vserver'
PORT = 5000
IMAGE = 'localhost:5000/v6-carrier-py:latest'

WAIT_TIME = 10

USERNAME = 'admin'
PASSWORD = 'admin'

COLLABORATION_ID = 1
MASTER_ORGANIZATION = [1]
RPC_ORGANIZATIONS = [2, 3, 6]

KEYS = ['GBAGeboorteJaar', 'GBAGeboorteMaand', 'GBAGeboorteDag', 'GBAGeslacht',
        'GBAPostcode', 'GBAHuisnummer', 'GBAToev']

FEATURES = ['height', 'weight', 'bmi', 'Age', 'n_smokingcat4', 'WOZ', 'N_ALCOHOL_CAT',
            'ZVWKOPHOOGFACTOR_2010', 'ZVWKHUISARTS_2010', 'ZVWKFARMACIE_2010', 'ZVWKZIEKENHUIS_2010',
            'ZVWKPARAMEDISCH_2010', 'ZVWKZIEKENVERVOER_2010',
            'ZVWKBUITENLAND_2010', 'ZVWKOVERIG_2010', 'ZVWKEERSTELIJNSPSYCHO_2010', 'ZVWKGGZ_2010',
            'ZVWKHULPMIDDEL_2010', 'ZVWKOPHOOGFACTOR_2011', 'ZVWKHUISARTS_2011']
TARGET = 'N_CVD'

client = VantageClient(USERNAME, PASSWORD)

input_ = {'method': 'column_names', 'master': False}
organizations = [{'id': o, 'input': input_} for o in RPC_ORGANIZATIONS]

# Retrieve columns names to check if a simple algorithm succeeds
task = client.post_task('column_names', image=IMAGE, collaboration_id=COLLABORATION_ID,
                        organizations=organizations)

print('Waiting for results...')
time.sleep(WAIT_TIME)
print(client.get_results(task['id']))

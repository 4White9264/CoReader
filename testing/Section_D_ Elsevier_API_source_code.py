"""An example program that uses the elsapy module"""

from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch
from elsapy.elsprofile import ElsAuthor
from elsapy.elsdoc import AbsDoc

import json
    
apikey = "101a5c0bb191f2c4f5931930171aeeb6" # insert a valid apikey


## Initialize client
client = ElsClient(apikey)
client.inst_token = ''

print(client)

first_name = 'Yurii'
last_name = 'Morozov'

def affiliation_id_serch(schoolname, client):
    """Search affiliation ID by name
    client - object of the ElsClient class  """
    
    school_srch = ElsSearch(' AFFIL(%s)'%schoolname,'affiliation')
    school_srch.execute(client)
    return school_srch.results

school_srch_results = affiliation_id_serch('Notre Dame', client)

print('Found ', len(school_srch_results), ' schools \n')

print('{:<15} {:>}'.format('Affiliation ID', '| Afiiliation Name'))
print('-'*40)

for school in school_srch_results:
    school_id =  school['dc:identifier'].split(':')[1]
    school_name = school['affiliation-name']
    print( '{:<15}  {:>}'.format(school_id, school_name))

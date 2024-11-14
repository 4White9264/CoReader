from Section_D_IEEE_API_source_code import XPLORE

# IEEE API key
query = XPLORE('26q3cwt335bbq2khcwf9gmhb')

query.abstractText('123')
query.dataType('json')
query.dataFormat('raw')
data = query.callAPI()

print(data)

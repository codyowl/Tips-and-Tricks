from collections import OrderedDict
import json

dictionary = OrderedDict()

dictionary['one'] = 'first'
dictionary['two'] = 'second'
dictionary['three'] = 'third'
dictionary['four'] = 'fourth'

json.dumps(dictionary)

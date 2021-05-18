import sys
import rmi_server
import rmi_client

sys.path.insert(1, 'symptoms_analysis')

import symptoms_analyzer as sym_anal

sa = sym_anal.SymptomsAnalyzer()

s = rmi_server.Server(sa)
uri = s.uri
print(uri)
s.start()

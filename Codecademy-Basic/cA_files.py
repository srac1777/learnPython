# with open("test.txt", "w") as file_doc:
#   file_doc.write("this is a test!")

import json

data_payload = { "k": 4 }

with open("data.json", "w") as data_json:
  json.dump(data_payload, data_json)
 
import json
import glob
import os

from random import randrange
from faker import Faker
from collections import OrderedDict
from datetime import date

locales = OrderedDict([
    ('pt-BR', 1),
])
faker_factory = Faker(locales)

id_counter = 0
medical_report_list = []
for file_name in glob.glob("/home/rgil/Git/neuralmed/data-engineer-test/data/exam_old/*"):
   with open(file_name, "r") as f:
      json_list = json.load(f)
      for json_item in json_list:
         
         json_item["content"]["id"] = id_counter
         if "exam_id" in json_item["content"]:
            json_item["content"].pop("exam_id")
         json_item["content"]["source"] = faker_factory.random_elements(elements=('first institute', "hospital ABC"), unique=True, length=1)[0],
         id_counter += 1

         keys_to_delete = []
         for k, v in json_item["content"].items():
            if not v:
               keys_to_delete.append(k)
         
         for key in keys_to_delete:
            json_item["content"].pop(key)
            
         labels = []
         for x in range(randrange(10)):
            labels.append({
            "classification": faker_factory.random_elements(elements=('covid19', "edema", "tumor", "hernia", "mass"), unique=True, length=1)[0],
            "labelled_by": faker_factory.name(),
            "labelled_date": str(faker_factory.date_between(date(2020, 1, 1))),
            "labelling_method": faker_factory.random_elements(elements=('ml_model', "physician"), unique=True)[0],
            "classification_type": "binary",
            "value": faker_factory.boolean(50)
         })

         medical_report = {
            "content": {
               "exam_id": id_counter,
               "report_date": str(faker_factory.date_between(date(2020, 1, 1))),
               "reported_by": faker_factory.name(),
               "text": faker_factory.text(),
            }
         }
         medical_report_list.append(medical_report)

         json_item["content"]["labels"] = labels
   
      with open(f"/home/rgil/Git/neuralmed/data-engineer-test/data/exam/{os.path.basename(file_name)}", 'w') as f:
         json.dump(json_list, f)

      with open(f"/home/rgil/Git/neuralmed/data-engineer-test/data/medical_report/{os.path.basename(file_name)}", 'w') as f:
         json.dump(medical_report_list, f)
      medical_report_list = []

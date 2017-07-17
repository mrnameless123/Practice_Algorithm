from collections import OrderedDict

selectedColumns = [
OrderedDict([('Country', '93535'), ('City', '72046'), ('Crime', '28'), ('Males', '34879'), ('Females', '37167'), ('Total PPL', '20672'), ('Size', '3')]),
OrderedDict([('Country', '93536'), ('City', '70918'), ('Crime', '34'), ('Males', '37804'), ('Females', '33114'), ('Total PPL', '20964'), ('Size', '3')]),
OrderedDict([('Country', '93543'), ('City', '13033'), ('Crime', '32'), ('Males', '6695'), ('Females', '6338'), ('Total PPL', '3560'), ('Size', '3')]),
OrderedDict([('Country', '93544'), ('City', '1259'), ('Crime', '52'), ('Males', '689'), ('Females', '570'), ('Total PPL', '569'), ('Size', '2')]),
OrderedDict([('Country', '93550'), ('City', '74929'), ('Crime', '27'), ('Males', '36414'), ('Females', '38515'), ('Total PPL', '20864'), ('Size', '3')]),
OrderedDict([('Country', '93551'), ('City', '50798'), ('Crime', '37'), ('Males', '25056'), ('Females', '25742'), ('Total PPL', '15963'), ('Size', '3')]),
OrderedDict([('Country', '93552'), ('City', '38158'), ('Crime', '28'), ('Males', '18711'), ('Females', '19447'), ('Total PPL', '9690'), ('Size', '3')]),
OrderedDict([('Country', '93553'), ('City', '2138'), ('Crime', '43'), ('Males', '1121'), ('Females', '1017'), ('Total PPL', '816'), ('Size', '2')])
]
ordered = sorted(selectedColumns, key= lambda element: element['City'])

for obj in ordered:
    print(obj)

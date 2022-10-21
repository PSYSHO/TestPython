from os.path import exists

from CSVcreator import creating
from fileWorker import writing_scv
from fileWorker import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()
writing_scv()
writing_txt()

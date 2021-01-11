import os
import glob
from pandas import *

os.chdir('data_afc_job_job')

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pandas.concat([pandas.read_csv(f) for f in all_filenames])
combined_csv.to_csv("data_afc_job_job_extern_final.csv", index=False)
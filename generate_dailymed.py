import pandas as pd

from analysis import *

path_dm = ".\\data\\dailymed\\prescription"

df_dm = make_df_drugs(get_all_file_paths(path_dm))

df_dm.to_csv(r".\\data\\dailymed\\dailymed.csv", index = False)
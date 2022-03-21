from google_play_scraper import app

import pandas as pd

import numpy as np

from google_play_scraper import Sort, reviews

result, continuation_token = reviews(
    'ajaib.co.id',
    lang='id', 
    country='id', 
    sort=Sort.NEWEST, 
    count=10, 
    filter_score_with=None 
)

df_busu = pd.DataFrame(np.array(result),columns=['review'])

df_busu = df_busu.join(pd.DataFrame(df_busu.pop('review').tolist()))

df_busu.head()
len(df_busu.index)
df_busu[['userName','at', 'content']].head()
my_df = df_busu[['userName','at', 'content']]
my_df.to_csv("scrapped.csv", index = False)


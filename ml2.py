import pandas as pd


work_experience = [12, 3,3, 25, 7, 18, 1, 30, 14, 9, 22,
                   5, 27, 16, 2, 20, 11, 6, 28, 15, 24,
                   8, 19, 4, 26, 13, 10, 21, 29, 17, 23]

salary = [109442, 44444, 15267, 203328, 73332, 152774, 30000, 239438, 123886, 87776, 181662,
          58888, 210550, 145552, 37222, 167218, 102220, 66110, 217772, 131108, 174440,
          80554, 159996, 51666, 196106, 116664, 94998, 188884, 232216, 138330, 166662]

rich_status = ['rich', 'not rich', 'not rich', 'rich', 'not rich', 'rich', 'not rich', 'rich', 'rich', 'not rich', 'rich',
               'not rich', 'rich', 'rich', 'not rich', 'rich', 'rich', 'not rich', 'rich', 'rich', 'rich',
               'not rich', 'rich', 'not rich', 'rich', 'rich', 'not rich', 'rich', 'rich', 'rich', 'rich']

df=pd.DataFrame()
df["work_exp"]=work_experience
df["salary"]=salary
df["rich_status"]=rich_status


exp = 32

k = 5

df['filter'] = df['work_exp'] - exp
df['filter'] = df['filter'].abs()

print(df.sort_values(by = 'filter', ascending = True).head(k)['salary'].mean())


exp = 9
k = 5

df['filter'] = df['work_exp'] - exp
df['filter'] = df['filter'].abs()

print(df.sort_values(by = 'filter', ascending = True).head(k)['rich_status'].value_counts().index[0])


exp = 5
salary = 60000
k = 5


df['filter'] = df['work_exp'] - exp
df['filter'] = df['filter'].abs()

df_ = df.sort_values(by = 'filter', ascending = True).head(10)

df_['filter'] = df_['salary'] - salary
df_['filter'] = df_['filter'].abs()

print(df_['rich_status'].value_counts().index[0])


exp = 1000
salary = 60000
k = 5

df['filter'] = df['salary'] + df['work_exp']
df['filter'] = df['filter'] - (salary + exp)
df['filter'] = df['filter'].abs()

df = df.sort_values(by = 'filter', ascending = True).head(10).head(k)

print(df)
















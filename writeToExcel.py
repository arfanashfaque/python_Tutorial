import pandas as pd
import openpyxl

df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                  index=['one', 'two', 'three'], columns=['a', 'b', 'c'])

print(df)
#print(df.info())
df.to_excel('pandas_to_excel_no_index_header.xlsx', index=False, header=False)
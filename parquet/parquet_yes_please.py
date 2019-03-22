import pandas as pd
import pyarrow as pa
from pyarrow import parquet as pq


# Converting Pandas DataFrame to Apache Arrow Table
df = pd.read_csv('100_crimes.csv')
# df = pd.read_csv('crimes_2001_to_present.csv')
print(type(df))
table = pa.Table.from_pandas(df)
print(table)

# Writing a parquet from Apache Arrow (codecs)
pq.write_table(table, '100_crimes.parquet', compression='snappy')
# pq.write_table(table, 'mini_crimes_gzip.parquet', compression='gzip')
# pq.write_table(table, 'mini_crimes_brotli.parquet', compression='brotli')
# pq.write_table(table, 'mini_crimes_none.parquet', compression='none')

# Reading a parquet file
table_all = pq.read_table('100_crimes.parquet')
print(table_all)
# Reading some columns from a parquet file
table_sub = pq.read_table('100_crimes.parquet', columns=['Description', 'Arrest'])
print(table_sub)

# Write a partitioned Parquet table
df_small =  pd.DataFrame({'one': [1, 2.5, 3],
                   'two': ['Peru', 'Brasil', 'Canada'],
                   'three': [True, False, True]},
                   index=list('abc'))
table_small = pa.Table.from_pandas(df_small)

# write the dataset
pq.write_to_dataset(table_all, root_path='dataset_output', partition_cols=['Description', 'Arrest'])

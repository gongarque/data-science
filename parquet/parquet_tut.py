import pyarrow.parquet as pq
import numpy as np
import pandas as pd
import pyarrow as pa

# Reading and Writing Single Files
# Dataframe definition
df = pd.DataFrame(
    {'one': [-1, np.nan, 2.5],
     'two': ['foo', 'bar', 'baz'],
     'three': [True, False, True]},
    index=list('abc'),
    columns=['one', 'two', 'three'])

print('Dataframe created...', '\n', df, '\n')

# Pyarrow table
pyarrow_table = pa.Table.from_pandas(df)
print('Printing pyarrow table...\n', pyarrow_table, '\n')

# Writing into parquet file
pq.write_table(pyarrow_table, 'example.parquet')

table2 = pq.read_table('example.parquet')
print('Printing read table from parquet...\n', table2.to_pandas(), '\n')

print(pq.read_table('example.parquet', columns=['one', 'three']))
print(pq.read_pandas('example.parquet', columns=['two']).to_pandas())

# Finer-grained Reading and Writing
pf = pq.ParquetFile('example.parquet')
print(pf.metadata)
print(pf.schema)
print(pf.num_row_groups)
print('Read row group\n', pf.read_row_group(0), '\n')

with pq.ParquetWriter('example2.parquet', pyarrow_table.schema) as writer:
    for i in range(3):
        writer.write_table(pyarrow_table)
# writer.close()
pf2 = pq.ParquetFile('example2.parquet')
print(pf2.num_row_groups)
print(pq.read_pandas('example2.parquet').to_pandas())

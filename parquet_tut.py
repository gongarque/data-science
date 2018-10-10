import pyarrow.parquet as pq
import numpy as np
import pandas as pd
import pyarrow as pa

# Reading and Writing Single Files
df = pd.DataFrame(
    {'one': [-1, np.nan, 2.5],
     'two': ['foo', 'bar', 'baz'],
     'three': [True, False, True]},
    index=list('abc'))

print(df)

table = pa.Table.from_pandas(df)

print(table)

pq.write_table(table, 'example.parquet')

table2 = pq.read_table('example.parquet')
print(table2.to_pandas())

print(pq.read_table('example.parquet', columns=['one', 'three']))
print(pq.read_pandas('example.parquet', columns=['two']).to_pandas())

# Finer-grained Reading and Writing
pf = pq.ParquetFile('example.parquet')
print(pf.metadata)
print(pf.schema)
print(pf.num_row_groups)
print(pf.read_row_group(0))

with pq.ParquetWriter('example2.parquet', table.schema) as writer:
    for i in range(3):
        writer.write_table(table)
# writer.close()
pf2 = pq.ParquetFile('example2.parquet')
print(pf2.num_row_groups)
print(pq.read_pandas('example2.parquet').to_pandas())





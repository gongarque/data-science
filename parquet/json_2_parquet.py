import pandas as pd
import pyarrow as pa
from pyarrow import parquet as pq

# Converting Pandas DataFrame to Apache Arrow Table
df_tel = pd.read_csv('samples/telemetry_parsed.csv', sep=';')

df_small = pd.DataFrame({
    'int': [1, 2],
    'str': ['a', 'b']
    })

# pyarrow table from DF
table_tel = pa.Table.from_pandas(df_tel)
print(table_tel.columns)

# write a partitioned dataset in parquet
pq.write_to_dataset(table_tel, root_path='dataset_output', partition_cols=['KEY-SOURCE'], compression='brotli')

# read from partitioned datasets
# Option 1
dataset = pq.ParquetDataset('dataset_output/', filters=[('KEY-SOURCE', '=', 'PazHRSensor'),])
print(type(dataset))
table_read = dataset.read()

# Option 2
# table_read = pq.read_table('dataset_output/KEY-SOURCE=PazHRSensor')

print('TABLE READ FROM PARQUET\n', table_read)
# print(table_read.columns)
print(table_read.to_pandas())


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np_list = np.random.rand(10, 5)
print(np_list)
df = pd.DataFrame(np_list, columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box(grid=True)

# plt.boxplot(df.values)
plt.show()
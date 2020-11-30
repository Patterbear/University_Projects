import numpy as np

x = list(range(1, 21))

x_array = np.array(x)

x_array_cube = x_array**3

x_array_cube_avg = np.mean(x_array_cube)

x_array_cube_avg_2d = x_array_cube_avg.reshape(5, 4)

x_array_cube_2d_l20 = x_array_cube_avg_2d[20 < e]

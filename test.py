from scipy import io as spio
import numpy as np

a = np.ones((3, 3))
spio.savemat('f.mat', {'a': a})
data = spio.loadmat('f.mat', struct_as_record=True)
data['a']

#测试terminal
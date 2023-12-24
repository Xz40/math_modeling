import numpy as np

w = np.random.random((1,3)).T
print(f'previous weights = {w}')
def sigmoid(x):
	return 1/(1+np.exp(-x))
in_train=np.array([[1,1,0],
				   [1,0,0],
				   [0,0,1],
				   [1,1,1]])
out_train = np.array([[1,1,0,1]]).T
for i in range(20000):
	output = sigmoid(np.dot(in_train, w))
	err = out_train - output
	w += np.dot(in_train.T, err*(output*(1-output)))
print(output)
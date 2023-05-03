import torch

is_cuda = torch.cuda.is_available()
print (f'cuda availability: {is_cuda}')

x = torch.rand(3, 4)
print(x)

from gym import envs
print(envs.registry.keys())

env = gym.make('FrozenLake-v0')
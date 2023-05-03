import gym

env = gym.make('FrozenLake-v1', render_mode='rgb_array')


n_state = env.observation_space.n
print(n_state)

n_action = env.action_space.n
print(n_action)

env.reset()

env.render()
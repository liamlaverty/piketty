import gym
env = gym.make('FrozenLake-v1', render_mode='human')


n_state = env.observation_space.n
print(f'n_state: {n_state}')

n_action = env.action_space.n
print(f'n_action: {n_action}')

env.reset()

env.render()

discard, new_state, reward, is_done, info = env.step(2)
print(f'new_state: {new_state}')
print(f'reward: {reward}')
print(f'info: {info}')

discard, new_state, reward, is_done, info = env.step(3)
print(f'new_state: {new_state}')
print(f'reward: {reward}')
print(f'info: {info}')
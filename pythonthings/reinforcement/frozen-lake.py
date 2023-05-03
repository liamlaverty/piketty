import gym
import torch

env = gym.make('FrozenLake-v1', render_mode='human')


n_state = env.observation_space.n
print(f'n_state: {n_state}')

n_action = env.action_space.n
print(f'n_action: {n_action}')

env.reset()

env.render()

# _discard, new_state, reward, is_done, info = env.step(2)
# print(f'new_state: {new_state}')
# print(f'reward: {reward}')
# print(f'info: {info}')

# discard, new_state, reward, is_done, info = env.step(3)
# print(f'new_state: {new_state}')
# print(f'reward: {reward}')
# print(f'info: {info}')

def run_episode(env, policy):
    state = env.reset()
    total_reward = 0
    is_done = False
    itterator = 0
    print(f'policy: {policy}')
    print(f'state: {state}')
    while not is_done:
        print(f'itteration: {itterator}')
        itterator+=1
        action = policy[state].item()
        _discard, state, reward, is_done, info = env.step(action)
        total_reward += reward
        if is_done:
            break
    return total_reward

n_episode = 1000
total_rewards = []
for episode in range(n_episode):
    this_random_policy = torch.randint(low=0, high=n_action, size=(n_state,))
    this_total_reward = run_episode(env, this_random_policy)
    total_rewards.append(this_total_reward)
print(f'avg total reward under random policy: {sum(total_rewards)/n_episode}')
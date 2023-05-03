import gymnasium as gym
import torch

env = gym.make('FrozenLake-v1', render_mode='human')


n_state = env.observation_space.n
print(f'n_state: {n_state}')

n_action = env.action_space.n
print(f'n_action: {n_action}')

env.reset()

env.render()

_discard, new_state, reward, is_done, info = env.step(2)
env.render()
print(new_state)
print(reward)
print(is_done)
print(info)


def run_episode(env, policy):
    state = env.reset()
    total_reward = 0
    is_done = False
    itterator = 0
    print(f'state: {state}')

    while not is_done:
        action = policy[state].item()
        state, reward, is_done, info = env.step(policy)
        total_reward += reward
        if is_done:
            break
        print(f'itteration: {itterator}')
        itterator+=1
    return total_reward


n_episode = 1000
total_rewards = []
for episode in range(n_episode):
    random_policy = torch.randint(high=n_action, size=(n_state,))
    print(f'randpolicy: {random_policy}')
    total_reward = run_episode(env, random_policy)
    total_rewards.append(total_reward)
print(f'avg total reward under random policy: {sum(total_rewards)/n_episode}')
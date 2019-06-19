from gym.envs.registration import register

register(
    id='bb8gym-v0',
    entry_point='bb8_gym.envs.bb8_env:BB8Enviroment'
)
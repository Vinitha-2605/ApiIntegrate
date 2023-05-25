import toml

def get_config():
  token = toml.load('config/config.toml')
  return token
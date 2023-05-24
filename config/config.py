import toml

def get_config():
  return toml.load('config/config.toml')
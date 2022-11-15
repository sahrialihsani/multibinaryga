from importlib.abc import Loader
import yaml

def load_config():

    config_path = "./config/params.yaml"

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    return config
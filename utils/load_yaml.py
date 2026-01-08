
import yaml

def load_yaml_file(path:str):
    with open(path,"r") as file:
        config = yaml.safe_load(file)
    return config


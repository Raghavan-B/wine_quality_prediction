import os
import yaml
from src.wine_quality_prediction import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns 

    Args: 
    path_to_yaml (str): path like input

    Raises:
    ValueError: if yaml file is empty
    e: empty file   

    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        return e 


@ensure_annotations
def create_directories(path_to_directories: list,verbose = True):
    """create list of directories

    Args:
    path_to_directories (list): list of path of directories
    ignore_log (bool,optional): ignore if multiple dirs to be created.  
    
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")


@ensure_annotations
def save_json(path : Path,data: dict):
    """
    saves json data

    Args:
    path (Path): path to the json file
    data(dict): data to be saved in json file
    """
    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"Json file saved at {path}")

@ensure_annotations
def load_json(path : Path) -> ConfigBox:
    """
    loads json data

    Args:
    path (Path): path to the json file
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"Json file loaded successfully from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data : Any,path: Path):
    """
    saves binary file

    Args:
    path (Path): path to the binary file
    data(dict): data to be saved in binary file
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"Binary file saved at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    loads binary file

    Args:
    path (Path): path to the binary file

    Returns: 
    Any object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data
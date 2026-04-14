import os 
import yaml
from src.DSPROJECT import logger
import json
import joblib
from ensure import ensure_annotations
from box import Config_Box
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> Config_Box:
    """Reads yaml file and returns.
    
    Args:
        path_to_yaml (str): Path to the yaml file.

    Raises:
        ValueError: If the yaml file is empty.
        e: Any exception that occurs while reading the yaml file.

    Returns:
        Config_Box: A Config_Box object containing the yaml data.
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return Config_Box(content)
    except ValueError as ve:
        logger.exception(f"yaml file: {path_to_yaml} is empty.")
        raise ve
    except Exception as e:
        logger.exception(f"Error occurred while reading yaml file: {path_to_yaml}.")
        raise e
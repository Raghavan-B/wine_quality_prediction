from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir : Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict ## have all schema details in schema.yaml

## Data transformation entity
@dataclass
class DataTransformationConfig:
    root_dir : Path
    data_path: Path

## Model trainer Config
@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha : float ##Should be in params.yaml file
    l1_ratio: float ##Should be in params.yaml file
    target_column: str

    
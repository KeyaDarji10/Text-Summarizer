# creating entity
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    # return types of the function
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
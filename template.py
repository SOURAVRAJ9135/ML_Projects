import os 
from pathlib import Path
from setuptools import setup, find_packages
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
project_name = "ml_project_template"
list_of_files = [
    
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    "requirements.txt",
    "setup.py",
    "README.md",
    "LICENSE",
    "Dockerfile",


]

for file_path in list_of_files:
    file_path = Path(file_path)
    if not file_path.exists():
        logging.info(f"Creating file: {file_path}")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch()
    else:
        logging.info(f"File already exists: {file_path}")

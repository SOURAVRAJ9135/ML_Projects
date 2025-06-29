import os 
import sys 
from src.house_price_prediction.logger import logging ## for logging messages
from src.house_price_prediction.exception import CustomException ## custom exception class
import pandas as pd ## for data manipulation
from sklearn.model_selection import train_test_split ## for splitting data into training and testing sets
from src.house_price_prediction.utils import read_sql_data ## utility function to read data from SQL


from dataclasses import dataclass ## for creating data classes
@dataclass
class DataIngestionConfig:
    """
    Data Ingestion Configuration Class
    This class holds the configuration for data ingestion.
    """
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    """
    Data Ingestion Class
    This class is responsible for ingesting data from a source and splitting it into training and testing sets.
    """
    
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() ## initialize the ingestion config

    def initiate_data_ingestion(self):
        """
        Initiates the data ingestion process.
        """
        logging.info("Data Ingestion started")
        try:
            # Read the dataset from SQL database
            df = pd.read_csv(os.path.join('notebook/data','raw.csv'))
            logging.info("Dataset read successfully")

            # Save the raw data
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data saved successfully")

            # Split the data into training and testing sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info("Data split into training and testing sets")

            # Save the training and testing sets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Training and testing sets saved successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )
        except Exception as e:
            raise CustomException(e, sys) ## raise custom exception if any error occurs
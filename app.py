from src.house_price_prediction.logger import logging
from src.house_price_prediction.exception import CustomException
import sys
from src.house_price_prediction.components.data_ingestion import DataIngestion






if __name__ == "__main__":
    logging.info("Starting the house price prediction(churn_modelling) application...")
    # Here you would typically call your main function or start your application logic
    # For example:
    # from src.house_price_prediction import main
    # main.run()
    
    logging.info("House price prediction application has started successfully.")
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        # Simulate some processing
        logging.info("Data ingestion completed successfully.")
        # You can add more processing steps here
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise CustomException(e, sys) from e
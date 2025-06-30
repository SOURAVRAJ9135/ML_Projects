from src.house_price_prediction.logger import logging
from src.house_price_prediction.exception import CustomException
import sys
from src.house_price_prediction.components.data_ingestion import DataIngestion
from src.house_price_prediction.components.data_transformation import DataTransformation




if __name__ == "__main__":
    logging.info("Starting the house price prediction(churn_modelling) application...")
    # Here you would typically call your main function or start your application logic
    # For example:
    # from src.house_price_prediction import main
    # main.run()
    
    logging.info("House price prediction application has started successfully.")
    try:
        data_ingestion = DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        # Simulate some processing
        logging.info("Data ingestion completed successfully.")
        # You can add more processing steps here

        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
        logging.info("Data transformation completed successfully.")

        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise CustomException(e, sys) 
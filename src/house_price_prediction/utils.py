import os
import sys
from src.house_price_prediction.logger import logging  # for logging messages
from src.house_price_prediction.exception import CustomException  # custom exception class
import pandas as pd  # for data manipulation
from sklearn.model_selection import train_test_split  # for splitting data into training and testing sets
from dotenv import load_dotenv  # for loading environment variables
import pymysql  # for connecting to MySQL database

load_dotenv()  # Load environment variables from .env file

host=os.getenv('host')  # Get host from environment variable, default to 'localhost'
user=os.getenv('user')  # Get user from environment variable, default to 'root'
password=os.getenv('password')  # Get password from environment variable, default to 'root'
database=os.getenv('db')  # Get database from environment variable, default to 'house_price_prediction'
port=os.getenv('port')  # Get port from environment variable, created port '3307'
def read_sql_data():
    """
    Reads data from a SQL database and returns it as a pandas DataFrame.
    
    Returns:
        pd.DataFrame: DataFrame containing the data from the SQL database.
    """
    try:
        
        mydb=pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=database,
                             port=int(port))  # Connect to the SQL database using environment variables
                            
        logging.info("Connected to the SQL database successfully")
        df=pd.read_sql_query("SELECT * FROM churn_modelling", mydb)  # Read data from the SQL table
        logging.info("Data read from SQL database successfully")
        return df
    except Exception as e:
        raise CustomException(e, sys)  # Raise custom exception if any error occurs
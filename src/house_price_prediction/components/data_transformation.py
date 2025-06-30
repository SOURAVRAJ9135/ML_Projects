import sys 
from dataclasses import dataclass
import os
import pandas as pd     
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from src.house_price_prediction.logger import logging       
from src.house_price_prediction.exception import CustomException

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer   
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.house_price_prediction.utils import save_object



@dataclass
class DataTransformationConfig:
    """
    Data Transformation Configuration Class
    This class holds the configuration for data transformation.
    """
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')
    

class DataTransformation:
    """
    Data Transformation Class
    This class is responsible for transforming the data by applying preprocessing steps.
    """

    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        """
        Get the data transformer object for preprocessing.
        
        Returns:
            Pipeline: A scikit-learn Pipeline object for data transformation.
        """
        try:
            numerical_features = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']

            categorical_features = ['Geography','Gender',  'HasCrCard', 'IsActiveMember']
                                    

            numerical_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='mean')),
                ('scaler', StandardScaler())
            ])

            categorical_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('onehotencoder', OneHotEncoder(handle_unknown='ignore'))
            ])
            logging.info("Numerical and categorical transformers created successfully")
            logging.info(f"Numerical features: {numerical_features}")
            logging.info(f"Categorical features: {categorical_features}")

            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', numerical_transformer, numerical_features),
                    ('cat', categorical_transformer, categorical_features)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
    def initiate_data_transformation(self, train_data_path, test_data_path):
        """
        Initiates the data transformation process.
        
        Args:
            train_data_path (str): Path to the training data CSV file.
            test_data_path (str): Path to the testing data CSV file.
        
        Returns:
            tuple: Transformed training and testing data arrays, and the preprocessor object.
        """
        try:
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)

            logging.info("Data loaded successfully for transformation")

            preprocessing_obj = self.get_data_transformer_object()

            target_column = 'Exited'
            ## dividing input and target features for training and testing data
            input_feature_train_df = train_df.drop(columns=[target_column], axis=1)
            target_feature_train_df= train_df[target_column]

            input_feature_test_df = test_df.drop(columns=[target_column], axis=1)
            target_feature_test_df = test_df[target_column]

            logging.info("Data split into features and target variable")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr=np.c_[input_feature_train_arr, target_feature_train_df]
            test_arr=np.c_[input_feature_test_arr, target_feature_test_df]

            logging.info("Data transformation completed successfully")

            # Save the preprocessor object
            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,obj=preprocessing_obj)

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)
    
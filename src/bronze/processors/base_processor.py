from src.core.base_processor import BaseProcessor
# from src.utils.spark_session_manager import SparkSessionManager


class BronzeLevelBaseProcessor(BaseProcessor):
    def __init__(self, config):
        # super().__init__(config)
        self.config = config
        self.load_type = config.get('load_type', 'full')
        # self.spark = SparkSessionManager.get_spark_session()
        print('Test spark session.')

    def validate_schema(self, df):
        """Common validation for bronze layer"""
        pass

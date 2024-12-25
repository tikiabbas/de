# In bronze/config.py
import importlib
from apollo.core.processor_factory import ProcessorFactory
from .processors.customer_processor import CustomerBronzeProcessor
from .processors.sales_processor import SalesBronzeProcessor
from apollo.utils.config_manager import ConfigManager



def register_bronze_processors():
    # Load bronze-specific configuration
    bronze_config = ConfigManager.load_config('apollo/config/bronze_config.yaml')

    for table, table_config in bronze_config['tables'].items():

        module = importlib.import_module(f'apollo.bronze.processors.{table}_processor')
        processor_class_name = getattr(module, f'{table.capitalize()}BronzeProcessor', None)

        ProcessorFactory.register_processor(
            layer='bronze',
            table=table,
            processor_class= processor_class_name,  # Example processor
            config=table_config
        )


# # from .processors.sales_processor import SalesBronzeProcessor
#
#
# def register_bronze_processors():
#     ProcessorFactory.register_processor(
#         layer='bronze',
#         table='customers',
#         processor_class=CustomerBronzeProcessor,
#         config={
#             'source_path': '/data/raw/customers',
#             'target_path': '/data/bronze/customers',
#             'format': 'csv'
#         }
#     )

    # ProcessorFactory.register_processor(
    #     layer='bronze',
    #     table='sales',
    #     processor_class=SalesBronzeProcessor,
    #     config={
    #         'source_path': '/data/raw/sales',
    #         'target_path': '/data/bronze/sales',
    #         'format': 'parquet'
    #     }
    # )

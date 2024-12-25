import argparse
from src.core.processor_factory import ProcessorFactory
from src.bronze.config import register_bronze_processors
# from src.silver.config import register_silver_processors
# from src.gold.config import register_gold_processors

def main():
    """
    Entry point for Medallion Architecture pipeline
    Reflects Abbas's experience in developing dynamic ETL solutions
    """
    parser = argparse.ArgumentParser(description='Medallion Pipeline Processor')
    parser.add_argument('--layer', required=True, choices=['bronze', 'silver', 'gold'])
    parser.add_argument('--table', required=True)
    parser.add_argument('--load_type', choices=['full', 'inc'], default='full')

    args = parser.parse_args()

    register_bronze_processors()
    # register_silver_processors()
    # register_gold_processors()

    try:
        # Dynamically retrieve and execute processor
        # processor = ProcessorFactory.get_processor(args.layer, args.table, args.load_type)
        # processor.process()

        p = ProcessorFactory()
        p.get_processor(args.layer, args.table, args.load_type).process()
        # print(f'Processor: {processor}')
    except Exception as e:
        print(f"Error processing {args.table} in {args.layer} layer: {e}")


if __name__ == '__main__':
    main()

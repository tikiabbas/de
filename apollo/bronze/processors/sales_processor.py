from .base_processor import BronzeLevelBaseProcessor


class SalesBronzeProcessor(BronzeLevelBaseProcessor):
    def process(self):
        print("In: SalesBronzeProcessor")
        # Raw data ingestion specific to customers
        # df = self.spark.read.format(self.config['format']) \
        #     .load(self.config['source_path'])

        # Bronze layer specific processing
        # validated_df = self.validate_schema(df)

        # validated_df.write \
        #     .format('delta') \
        #     .mode('overwrite') \
        #     .save(self.config['target_path'])

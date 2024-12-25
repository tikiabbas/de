from .base_processor import BronzeLevelBaseProcessor


class CustomerBronzeProcessor(BronzeLevelBaseProcessor):
    def process(self):
        print("In: CustomerBronzeProcessor")
        if self.load_type == "full":
            self._full_load()
        elif self.load_type == "inc":
            self._inc_load()

    def _full_load(self):
        # Full load implementation
        print("Starting Full load.")

    def _inc_load(self):
        # Incremental load implementation
        print("Starting Incremental load.")

        # Raw data ingestion specific to customers
        # df = self.spark.read.format(self.config['format']) \
        #     .load(self.config['source_path'])

        # Bronze layer specific processing
        # validated_df = self.validate_schema(df)

        # validated_df.write \
        #     .format('delta') \
        #     .mode('overwrite') \
        #     .save(self.config['target_path'])

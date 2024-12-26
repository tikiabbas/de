import uuid
from .base_processor import BronzeLevelBaseProcessor
from apollo.utils.logger import StructuredTableLogger, timing_decorator
from typing import Dict, Any


class CustomerBronzeProcessor(BronzeLevelBaseProcessor):
    def __init__(self, config: Dict[str, Any]):
        print("Init Customer Bronze Proc")
        super().__init__(config)
        self.logger = StructuredTableLogger(
            None,  # self.spark,
            "logs/medallion_pipeline",  # Changed from dbfs path to local path
        )
        self.correlation_id = str(uuid.uuid4())

    @timing_decorator
    def process(self):
        print("Start CustomerBronzeProcessor")
        try:
            self.logger.log(
                "INFO",
                "process.start",
                correlation_id=self.correlation_id,
                layer="bronze",
                processor="CustomerBronzeProcessor",
                load_type=self.load_type,
            )

            if self.load_type == "full":
                self._full_load()
                return "Full load is triggered."
            elif self.load_type == "inc":
                self._inc_load()
                return "Inc load is triggered."

        except Exception as e:
            self.logger.log(
                "ERROR",
                "process.failed",
                correlation_id=self.correlation_id,
                layer="bronze",
                processor="CustomerBronzeProcessor",
                error=str(e),
                error_type=type(e).__name__,
            )
            raise

    def _full_load(self):
        try:
            self.logger.log(
                "INFO",
                "full_load.start",
                correlation_id=self.correlation_id,
                layer="bronze",
                processor="CustomerBronzeProcessor",
            )

            print("Full load is triggered.")

            self.logger.log(
                "INFO",
                "data.loaded",
                correlation_id=self.correlation_id,
                layer="bronze",
                processor="CustomerBronzeProcessor",
                record_count="0",  # Removed df.count() as no DataFrame exists
            )

        except Exception as e:
            self.logger.log(
                "ERROR",
                "full_load.failed",
                correlation_id=self.correlation_id,
                layer="bronze",
                processor="CustomerBronzeProcessor",
                error=str(e),
                error_type=type(e).__name__,
            )
            raise

    def _inc_load(self):
        try:
            self.logger.log(
                "INFO",
                "incremental_load.start",
                correlation_id=self.correlation_id,
                layer="bronze",
                processor="CustomerBronzeProcessor",
            )

            print("Inc load is triggered.")

            self.logger.log(
                "INFO",
                "data.loaded",
                correlation_id=self.correlation_id,
                layer="bronze",
                processor="CustomerBronzeProcessor",
                record_count="0",  # Removed df.count() as no DataFrame exists
            )

        except Exception as e:
            self.logger.log(
                "ERROR",
                "incremental_load.failed",
                correlation_id=self.correlation_id,
                layer="bronze",
                processor="CustomerBronzeProcessor",
                error=str(e),
                error_type=type(e).__name__,
            )
            raise

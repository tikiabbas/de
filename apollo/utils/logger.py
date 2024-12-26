# src/apollo/utils/logger.py
import structlog
import logging
import time
from functools import wraps
from datetime import datetime
from pyspark.sql.types import StructType, StructField, StringType, TimestampType
# from typing import Any, Dict


class StructuredTableLogger:
    def __init__(self, spark, log_table_path: str):

        self.spark = None
        self.log_table_path = log_table_path
        self.logger = self._configure_logger()
        self.log_schema = StructType([
            StructField("timestamp", TimestampType(), False),
            StructField("level", StringType(), False),
            StructField("correlation_id", StringType(), True),
            StructField("layer", StringType(), True),
            StructField("processor", StringType(), True),
            StructField("event", StringType(), False),
            StructField("execution_time_ms", StringType(), True),
            StructField("context", StringType(), True)
        ])

    def _configure_logger(self):
        structlog.configure(
            processors=[
                structlog.contextvars.merge_contextvars,
                structlog.processors.add_log_level,
                structlog.processors.TimeStamper(fmt="iso"),
                structlog.processors.JSONRenderer()
            ],
            wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
            context_class=dict,
            cache_logger_on_first_use=True
        )
        return structlog.get_logger()

    def log(self, level: str, event: str, **kwargs):
        # Create structured log
        log_entry = self.logger.bind(**kwargs).msg(event)

        # Write to Delta table
        # log_df = self.spark.createDataFrame(
        #     [[
        #         datetime.now(),
        #         level,
        #         kwargs.get('correlation_id'),
        #         kwargs.get('layer'),
        #         kwargs.get('processor'),
        #         event,
        #         kwargs.get('execution_time_ms'),
        #         str(log_entry)
        #     ]],
        #     schema=self.log_schema
        # )

        # log_df.write.mode('append').format('delta').save(self.log_table_path)
        print(str(log_entry))


def timing_decorator(func=None, logger=None):
    if func is None:
        return lambda f: timing_decorator(f, logger)

    print(f"Rcvd function {func}")

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Inside wrapper")
        start_time = time.perf_counter()
        try:
            # Use instance logger if no logger provided
            instance_logger = logger or (args[0].logger if args else None)

            result = func(*args, **kwargs)
            execution_time = (time.perf_counter() - start_time) * 1000

            if instance_logger:
                instance_logger.log(
                    "INFO",
                    "function.execution.completed",
                    execution_time_ms=str(execution_time),
                    status="success",
                    function=func.__name__
                )
            return result

        except Exception as e:
            execution_time = (time.perf_counter() - start_time) * 1000
            if instance_logger:
                instance_logger.log(
                    "ERROR",
                    "function.execution.failed",
                    execution_time_ms=str(execution_time),
                    error=str(e),
                    error_type=type(e).__name__,
                    status="failed",
                    function=func.__name__
                )
            raise

    return wrapper
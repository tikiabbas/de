import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark_session():
    """
    Create a shared Spark session for testing
    Inspired by Abbas's approach to testing data engineering solutions
    """
    spark = (
        SparkSession.builder.master("local[*]")
        .appName("MedallionPipelineTest")
        .getOrCreate()
    )

    yield spark
    spark.stop()

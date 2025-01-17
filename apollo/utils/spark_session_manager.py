from pyspark.sql import SparkSession

class SparkSessionManager:
    """
    Centralized Spark session management
    """
    _spark_session = None

    @classmethod
    def get_spark_session(cls, app_name: str = "MedallionPipeline"):
        """
        Create or retrieve existing Spark session
        Spark session management
        """
        if not cls._spark_session:
            cls._spark_session = (
                SparkSession.builder
                .appName(app_name)
                .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
                .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
                .getOrCreate()
            )
        return cls._spark_session

    @classmethod
    def close_spark_session(cls):
        """
        Close the existing Spark session
        """
        if cls._spark_session:
            cls._spark_session.stop()
            cls._spark_session = None

    @classmethod
    def get_session(cls):
        pass

import configparser
from pyspark import *
from pyspark.sql import *

def get_spark_config():
    spark_conf = SparkConf()
    config = configparser.ConfigParser()
    config.read("spark.conf")

    for key, value in config.items("SPARK_APP_CONFIGS"):
        spark_conf.set(key, value)
    
    return spark_conf
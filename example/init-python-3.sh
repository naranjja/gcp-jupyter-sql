#!/bin/bash
apt-get -y install python3
echo "export PYSPARK_PYTHON=python3" | tee -a  /etc/profile.d/spark_config.sh  /etc/*bashrc /usr/lib/spark/conf/spark-env.sh
echo "Adding PYTHONHASHSEED=0 to profiles and spark-defaults.conf..."
echo "export PYTHONHASHSEED=0" | tee -a /etc/profile.d/spark_config.sh /etc/*bashrc /usr/lib/spark/conf/spark-env.sh
echo "spark.executorEnv.PYTHONHASHSEED=0" >> /etc/spark/conf/spark-defaults.conf

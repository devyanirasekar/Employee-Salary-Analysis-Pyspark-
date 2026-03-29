# read data
df = spark.table("workspace.default.employee_data")
df.show()

# → Check Structure
# check column name
df.select("id","name","dept","salary").show()
# check schema
df.printSchema()
# count table rows
df.count()

# Filter High Salary Employees (>5000)
df_high = df.filter(df.salary > 5000)
df_high.show()

# Department-wise Average Salary
from pyspark.sql.functions import avg
df_avg = df.groupBy("dept").agg(avg("salary").alias("avg_salary"))
df_avg.show()

# Total Salary per Department
from pyspark.sql.functions import sum
df_total = df.groupBy("dept").agg(sum("salary").alias("total_salary"))
df_total.show()

# Count Employees per Department
from pyspark.sql.functions import count
df_count = df.groupBy("dept").agg(count("name").alias("employee_count"))
df_count.show()

# Highest Salary Employee
df_top = df.orderBy(df.salary.desc()).limit(1)
df_top.show()

# Write Data
df_avg.write.mode("overwrite").saveAsTable("workspace.default.avg_salary")
# Read → Filter → GroupBy → Aggregation → Sort → Write

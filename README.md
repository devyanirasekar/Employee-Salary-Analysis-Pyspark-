📊 Employee Salary Analysis using PySpark & Databricks

📌 Project Overview
This project focuses on analyzing employee salary data using PySpark in Databricks.  
The goal is to perform data transformation and generate insights such as department-wise salary distribution, employee count, and top earners.

🚀 Objectives
- Analyze employee salary data
- Identify high salary employees
- Calculate department-wise salary insights
- Store processed results for future use

🛠️ Tools & Technologies
- PySpark  
- Databricks (Unity Catalog)  
- Python  

📂 Dataset
The dataset contains employee details:
- `id` → Employee ID  
- `name` → Employee Name  
- `dept` → Department  
- `salary` → Salary  

🔄 Workflow
1. Read data from Databricks table  
2. Check schema and structure  
3. Filter high salary employees  
4. Perform aggregation using groupBy  
5. Identify top salary employee  
6. Write results into Databricks table  

⚙️ Key Operations

🔹 Data Transformation
  - select()
  - filter()
    
🔹 Aggregation
  - avg()
  - sum()
  - count()
    
🔹 Sorting
  - orderBy()

📊 Key Insights
- Department-wise average salary  
- Total salary per department  
- Employee count per department  
- Highest-paid employee  

💾 Data Storage
Processed results are stored using Databricks tables:
workspace.default.avg_salary

📈 Project Flow
Read → Filter → GroupBy → Aggregation → Sort → Write

🎯 Learning Outcomes
- Hands-on experience with PySpark DataFrames  
- Understanding of data transformation and aggregation  
- Practical use of Databricks for data processing  
- Building an end-to-end ETL pipeline  

📌 Conclusion
This project demonstrates how PySpark can be used for efficient data analysis and how Databricks helps in managing and storing processed data.

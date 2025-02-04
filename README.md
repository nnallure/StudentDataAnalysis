# Student Data Analysis with Pandas  

This project demonstrates how to use **Pandas** to manipulate and analyze student data, including merging datasets, modifying columns, and performing conditional filtering.  

## 📌 Features  

- **Create DataFrames**: Store student details, including scores, sports, and majors.  
- **Modify Data**:  
  - Add a **new column** for student majors.  
  - Remove the **gender** column.  
  - Change the **index** for readability.  
- **Conditional Operations**:  
  - Add a `"pass"` column based on math scores (≥85).  
- **Descriptive Statistics**:  
  - Generate summary statistics using `.describe()`.  
- **Merge Datasets**:  
  - Use `pd.merge()` to combine two datasets on the `"name"` column.  
- **Calculated Columns**:  
  - Compute the `"total score"` (sum of math, chemistry, and physics scores).  
- **Filter & Sort Data**:  
  - Extract students who scored ≥75 in both math and chemistry.  
  - Sort data alphabetically by name.  

## 🛠️ Installation  

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/student-data-analysis.git
   cd student-data-analysis
2. Install dependencies:
    ```bash
    pip install pandas

3. Run the script:
   ```bash
   python student_analysis.py

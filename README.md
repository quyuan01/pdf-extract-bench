# Introduction
   PDF-benchmark is a PDF document understanding ability evaluation set for large model data scenarios. The total data volume is 1069 PDF files and 46916 pages of PDF, including 11 types of data sets such as textbooks, academic documents, PPT to PDF, and test papers. It can provide a reference for PDF document understanding capabilities for large model data developers and tool developers.

# Statistics of PDF-benchmark
![image](https://github.com/quyuan01/pdf-extract-bench/assets/102640628/a32d4a6f-fc36-41b9-b633-ce2dc85f3c01)


# Results


# Evaluation tools
 Before using the tool, you need to match the md file name you converted with the pdf file name. --standard is the md file list in annotations, and --actual is the md file list extracted for your solution.

```
cd evaluate_tool
python markdown_calculate.py --standard dir/annations --actual dir/actual_dir --results dir/xx.txt
```


# Get Data
Datasets can be downloaded from opendatalab: https://openxlab.org.cn/datasets/quyuan/PDF-bench/tree/main

# Introduction
   PDF-benchmark is a PDF document understanding ability evaluation set for large model data scenarios. The total data volume is 1069 PDF files and 46916 pages of PDF, including 11 types of data sets such as textbooks, academic documents, PPT to PDF, and test papers. It can provide a reference for PDF document understanding capabilities for large model data developers and tool developers.

# Statistics of PDF-benchmark
Referring to the corpus distribution of the LLM, the distribution(by page) of different categories of our benchmark is as follows：

![image](https://github.com/quyuan01/pdf-extract-bench/assets/102640628/b6281579-585c-43da-9d88-b25f226b39d1)

Referring to the corpus distribution of the LLM, the distribution(by PDF file) of different categories of our benchmark is as follows：

![image](https://github.com/quyuan01/pdf-extract-bench/assets/102640628/c186b7cc-2956-4a9d-a54c-1f7aca3aaafe)
The layout is distributed as follows:

![image](https://github.com/quyuan01/pdf-extract-bench/assets/102640628/2aa4c6bd-bd31-48e2-8c02-6e03b50d63a9)

The difficulty of OCR recognition is distributed as follows：
![image](https://github.com/quyuan01/pdf-extract-bench/assets/102640628/6b2f42df-fe1a-45f8-a0ae-8d89ae19d740)

The layout analysis is distributed as follows：
![image](https://github.com/quyuan01/pdf-extract-bench/assets/102640628/faa35a3a-0f68-4ed8-bd5c-fe8105a20125)

# Results


# Evaluation tools
 Before using the tool, you need to match the md file name you converted with the pdf file name. --standard is the md file list in annotations, and --actual is the md file list extracted for your solution.

```
cd evaluate_tool
python markdown_calculate.py --standard dir/annations --actual dir/actual_dir --results dir/xx.txt
```


# Get Data
Datasets can be downloaded from opendatalab: https://openxlab.org.cn/datasets/quyuan/PDF-bench/tree/main

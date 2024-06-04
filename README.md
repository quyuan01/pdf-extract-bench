# Introduction
   PDF-benchmark is a PDF document understanding ability evaluation set for large model data scenarios. The total data volume is 1069 PDF files and 46916 pages of PDF, including 11 types of data sets such as textbooks, academic documents, PPT to PDF, and test papers. It can provide a reference for PDF document understanding capabilities for large model data developers and tool developers.

# Statistics of PDF-benchmark

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/afe90ec7-9277-4303-b177-e619be749913" width="350" height="200" alt="The distribution of pages">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/069c12e8-97fb-4961-8a5d-9d5e93b62c8f" width="350" height="200" alt="The distribution of PDF file">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/2aa4c6bd-bd31-48e2-8c02-6e03b50d63a9" width="350" height="200" alt="The distribution of Text Extraction Difficulty">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/cbf7c4d8-1bfb-4541-9deb-52f485f86f35" width="350" height="200" alt="The distribution of OCR Extraction Difficulty">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/faa35a3a-0f68-4ed8-bd5c-fe8105a20125" width="350" height="200" alt="The distribution of layout">  



# Results


# Evaluation tools
 Before using the tool, you need to match the md file name you converted with the pdf file name. --standard is the md file list in annotations, and --actual is the md file list extracted for your solution.

```
cd evaluate_tool
python markdown_calculate.py --standard dir/annations --actual dir/actual_dir --results dir/xx.txt
```


# Get Data
Datasets can be downloaded from opendatalab: https://openxlab.org.cn/datasets/quyuan/PDF-bench/tree/main

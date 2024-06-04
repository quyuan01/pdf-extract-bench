# Introduction
   PDF-benchmark is an end-to-end evaluation set of PDF document comprehension capabilities for large model data scenarios. It is human-readable and provides technical difficulty labels for PDF document comprehension at the file granularity. The total data volume is 1,069 PDF files and 46,916 pages of PDF, including 11 types of data sets such as textbooks, academic documents, PPT to PDF, and test papers. It can provide a reference for PDF document comprehension capability evaluation for large model data developers and tool developers.
   Note: The PDF-benchmark dataset can only be used for non-commercial research purposes. 

# Statistics of PDF-benchmark

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/afe90ec7-9277-4303-b177-e619be749913" width="350" height="200" alt="The distribution of pages">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/069c12e8-97fb-4961-8a5d-9d5e93b62c8f" width="350" height="200" alt="The distribution of PDF file">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/2aa4c6bd-bd31-48e2-8c02-6e03b50d63a9" width="350" height="200" alt="The distribution of Text Extraction Difficulty">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/cbf7c4d8-1bfb-4541-9deb-52f485f86f35" width="350" height="200" alt="The distribution of OCR Extraction Difficulty">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/faa35a3a-0f68-4ed8-bd5c-fe8105a20125" width="350" height="200" alt="The distribution of layout">  

# Dataset Source
The PDF-benchmark datasets were collected from various sources, including arXiv, SCIHUB, textbooks, test papers, historical documents, etc. The proportion of different corpora is shown in lamma and internlm 20b. The source and composition of different subsets are shown below.

- The scientific article subset includes articles from arXiv and SCIHUB, including single-column, double-column, charts, formulas and other complex layouts;
- The ordinary textbook subset contains 458 PDF files which is from http://www.nsmath.cn/jszl and its colors are black and white, and it contains a rich formula;
- The colorful textbook subset contains 57 PDF files, it includes English, mathematics, Chinese (including pinyin) subjects. It includes colorful graphics information; 
- The research report subset contains 71 PDF files, it contains rich table information;
- The ordinary books subset contains 37 PDF files, it contains en and zh language; 
- The ordinary exam paper subset consists of 
- The magazine subset includes 1,000 Chinese and English magazines in PDF format, respectively. The Chinese magazines were sourced from five publishers: Global Science, The Mystery, Youth Digest, China National Geographic, and The Reader. The English magazines were sourced from five American publishers: The New Yorker, New Scientist, Scientific American, The Economist, and Time USA.
- The newspaper subset contains 500 PDF document images from the Chinese People's Daily and the Wall Street Journal.
- The note subset consists of students' handwritten notes in nine subjects, including 500 scanned pages.
- The book subset contains 500 photographed images, which were acquired from 50 books with 10 pages each. Each book has a distinct layout, resulting in considerable diversity in this subset.


# Results


# Evaluation tools
 Before using the tool, you need to match the md file name you converted with the pdf file name. --standard is the md file list in annotations, and --actual is the md file list extracted for your solution.

```
cd evaluate_tool
python markdown_calculate.py --standard dir/annations --actual dir/actual_dir --results dir/xx.txt
```


# Get Data
Datasets can be downloaded from opendatalab: https://openxlab.org.cn/datasets/quyuan/PDF-bench/tree/main

# License
The PDF-benchmark dataset should be used and distributed under the Creative Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) License(https://creativecommons.org/licenses/by-nc-nd/4.0/)for non-commercial research purposes

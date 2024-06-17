# Introduction
   MPB (Magic-PDF-Benchmark) is an end-to-end PDF document comprehension evaluation suite designed for large-scale model data scenarios. It ensures human readability at the file granularity and provides PDF categorization tags. The total dataset comprises 350 PDF files and 8410 pages of PDFs, including 11 types of datasets such as books, textbooks, academic literature, PPT to PDF conversions, and examination papers. It serves as a reference for the evaluation of PDF document comprehension capabilities for developers of large-scale model data and tool developers.
   
   Note: The PDF-benchmark dataset can only be used for non-commercial research purposes. 
# Dataset Source
The MPB dataset is sourced from a variety of origins, including arXiv, Sci-Hub, textbooks, examination papers, historical documents, etc., with reference to the corpus proportion of lamma and internlm 20b. The sources and composition of different subsets are as follows:

| Category                  | Tag                 | File Count | Total Pages | Description                                                                                    |
|---------------------------|---------------------|-------------|--------------|------------------------------------------------------------------------------------------------|
| Research Reports           | research_report     | 70          | 875          | Contains rich tabular information with single-column, double-column, and complex layouts.       |
| Ordinary Textbooks        | ordinary_textbook   | 40          | 388          | Single-column layout, black and white, includes a wealth of formulas.                         |
| Academic Literature        | academic_literature | 183         | 3323         | Data sourced from arXiv and Sci-Hub, includes single-column, double-column, charts, formulas, and other complex formats. |
| Atlas                     | atlas               | 3           | 269          | Characterized by a single page containing large area images.                                 |
| Courseware (PPT to PDF)   | courseware         | 7           | 383          | Includes subjects such as Biology, Chinese, English, and Physics.                              |
| Special Exam Papers       | special_exam_paper  | 3           | 80           | Includes watermarks, text within graphics, primary school Pinyin, and math problems.         |
| Historical Documents       | historical_documents | 1           | 3            | Layout is vertical, reading order is from right to left.                                     |
| Notes                      | notes               | 3           | 293          | Includes handwritten notes from three junior high school students.                            |
| Ordinary Exam Papers       | ordinary_exam_paper | 27          | 372          | Includes subjects such as Computer Science, Mathematics, Chinese, covering primary school, junior high school, high school, and industry question banks, mainly in black and white. |
| Colorful Textbooks        | colorful_textbook   | 3           | 144          | Includes subjects such as English, Mathematics, Chinese (including Pinyin), containing colorful graphic information. |
| Ordinary Books             | ordinary_books      | 10          | 2280         | Single-column layout, black and white background books.                                       |

# Statistics of MPB

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/43176747-4f03-42ad-b48b-a4448fc0dc0e" width="350" height="200" alt="The distribution of pages">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/fb06f784-f22f-4897-9b7e-00cf7f622e38" width="350" height="200" alt="The distribution of PDF file"> 

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/d233a4ca-c54a-41f3-be96-8b80b1b0b740" width="350" height="200" alt="The distribution of md language">  
<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/5ff056a7-6094-420b-8a93-a31585da9451" width="350" height="200" alt="The distribution of PDF  Type">  




# Results
### Overall Average Score
| Solution               | Extraction Rate (↑) | Similarity Score (↑) | Edit Distance (↓) | BLEU Score (↑) |
|------------------------|----------------------|----------------------|------------------|------------------|
| nogout(Open-Source Tool)                 | 100%                 | 0.35                 | 0.57             | 0.33             |
| marker(Open-Source Tool)                 | 99.4%                | 0.47                 | 0.42             | 0.386            |
| doc2x (Commercial Tool)| 99%                  | 0.67                 | 0.189            | 0.611            |
| ocrmath (Commercial Tool) | 92%                 | 0.56                 | 0.38             | 0.39             |
| mathpix (Commercial Tool) | 100%                | 0.83                 | 0.08             | 0.91             |

### Extraction scores of 11 Types
<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/473223d0-fee9-4158-8b79-52c09066d8e1" width="350" height="200" alt="The distribution of sim_socre">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/eb537cf8-f8d0-4815-b1c4-0494d72aa9ae" width="350" height="200" alt="The distribution of edit distance">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/f358d113-72fd-4cea-9f68-d46f01249219" width="350" height="200" alt="The distribution of bleu">  

# Get Data
Datasets can be downloaded from opendatalab: https://openxlab.org.cn/datasets/quyuan/PDF-bench/tree/main

# Evaluation tools
 Before using the tool, you need to match the md file name you converted with the pdf file name. --standard is the md file list in annotations, and --actual is the md file list extracted for your solution.

```
cd evaluate_tool
python markdown_calculate.py --standard dir/annations --actual dir/actual_dir --results dir/xx.txt
```


# License
The PDF-benchmark dataset should be used and distributed under the Creative Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) License(https://creativecommons.org/licenses/by-nc-nd/4.0/)for non-commercial research purposes

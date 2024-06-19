# Introduction
   MPB (Miner-PDF-Benchmark) is an end-to-end PDF document comprehension evaluation suite designed for large-scale model data scenarios. It ensures human readability at the file granularity and provides PDF categorization tags. The total dataset comprises 350 PDF files and 8410 pages of PDFs, including 11 types of datasets such as books, textbooks, academic literature, PPT to PDF conversions, and examination papers. It serves as a reference for the evaluation of PDF document comprehension capabilities for developers of large-scale model data and tool developers.
   
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

# Metrics
## sim score

- **Overlap Score**

For a set of hypothesis text chunks `H` and a set of reference text chunks `R`, the maximum similarity score between each hypothesis text chunk and the reference text chunks is calculated using the function `F(H_chunk, R_chunk)`, which returns a value between 0 and 1.

$${maxscore}(H_{\text{chunk}}, R) = \max_{R_{\text{chunk}} \in R} \left[ F(H, R_{\text{chunk}}) \right]$$


- **Mean Score**

The mean score `Mean_score` is calculated for the set of maximum scores `maxscore` of all hypothesis text chunks:

$$\text{Mean\\_score} = \text{mean}(maxscore)$$

If `maxscore` is empty, the mean score is 0.

- **Final Score**

The final score is the average alignment score between the set of hypothesis text chunks and the set of reference text chunks, denoted as `Score(T_H, T_R)`:

$${Score}(T_H, T_R) = \text{Mean}\left(\max_{R_{\text{chunk}} \in R} \left[ F(C(T_H, chunk\_len), R_{\text{chunk}}) \right]\right)$$
Where:
- `T_H` is the hypothesis text.
- `T_R` is the reference text.
- `C(T, chunk_len)` is the function that segments text `T` into chunks of length `chunk_len`.
- `F(H_chunk, R_chunk)` is the function that calculates the similarity score between two text chunks, which calculated by edit distance, score_cutoff is 30.
- `max` indicates finding the most similar chunk in the set of reference text chunks `R` for each hypothesis text chunk.
- `Mean` is the function that calculates the average value.
## Edit Distance

The Levenshtein distance ${lev}_{a,b}(i, j)$
between two strings  `a` and `b` is calculated as follows:

<center><img style="margin: 0 auto;" src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/6336202a-27d5-438a-b712-e01da6b14755" width="500" height="100" alt="The distribution of PDF  Type"> </center>


Where:
- `i` and `j` are the indices being compared in strings `a` and `b`, respectively.
- $\text{lev}_{a,b}(i', j')$ denotes the Levenshtein distance between the prefixes of `a` and `b` up to indices`i'` and` j' `.


The normalized edit distance between two strings `a` and `b` is calculated using the following formula:

$$\text{editdistance} = \frac{\text{lev}(a, b)}{\max(\text{len}(a), \text{len}(b))}$$

Where:
- ${lev}(a, b)$ represents the Levenshtein distance between strings `a` and `b`.
- $\text{len}(a)$ and $\text{len}(b)$represent the lengths of strings `a` and `b`, respectively.
- $\max(\text{len}(a), \text{len}(b))$ finds the greater of the two lengths.

## Blue

The BLEU score is calculated using the `sentence_bleu` method with smoothing function method1. Bleu is calculated as follows:

<center><img style="margin: 0 auto;" src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/87e0c8df-3f05-4e92-96b3-c25db681eb1e" width="450" height="150" alt="The distribution of PDF  Type"> </center>

where:
- $P_n$ represents the probability or proportion of a specific n-gram occurring in the candidates.
- $C_{\text{(n-gram)}}$ is the count of the specific n-gram within the set of candidates. This is the number of times the n-gram appears in the candidate translations.
- $C'_{\text{(n-gram')}}$ is the total count of all n-grams in the candidates. This could represent the sum of occurrences of all unique n-grams within the candidate translations.

<center><img style="margin: 0 auto;" src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/5b85781e-31fa-4969-9f3b-921884c96856" width="300" height="100" alt="The distribution of PDF  Type"> </center>

Where:
- $c$ is the length of the candidate translation.
- $r$ is the length of the reference translation.

The final BLEU score is calculated using a logarithmic evaluation:
<center><img style="margin: 0 auto;" src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/f6d4900f-9616-48ff-afdc-1c04cc9bf318" width="500" height="100" alt="The distribution of PDF  Type"> </center>



# Results
### Overall Average Score
| Solution               | Extraction Rate (↑) | Similarity Score (↑) | Edit Distance (↓) | BLEU Score (↑) |
|------------------------|----------------------|----------------------|------------------|------------------|
| nogout (Open-Source Tool)                 | 100%                 | 0.35                 | 0.57             | 0.33             |
| marker (Open-Source Tool)                 | 99.4%                | 0.47                 | 0.42             | 0.386            |
| doc2x (Commercial Tool)| 99%                  | 0.67                 | 0.189            | 0.611            |
| ocrmath (Commercial Tool) | 92%                 | 0.56                 | 0.38             | 0.39             |
| **mathpix (Commercial Tool)** | **100%**                | **0.83**                 | **0.08**             | **0.91**         |

### Scores of 11 Types
<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/473223d0-fee9-4158-8b79-52c09066d8e1" width="350" height="200" alt="The distribution of sim_socre">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/eb537cf8-f8d0-4815-b1c4-0494d72aa9ae" width="350" height="200" alt="The distribution of edit distance">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/f358d113-72fd-4cea-9f68-d46f01249219" width="350" height="200" alt="The distribution of bleu">  

notes:
- marker's test version is v0.2.8;
- nogout's test version is v0.1.0 small;
  
# Get Data
Datasets can be downloaded from opendatalab: https://openxlab.org.cn/datasets/quyuan/PDF-bench/tree/main

# Usage
- **step1**

After completing the download of the evaluation set, please execute the following command to complete the preliminary cleaning. The term "tool_type" refers to the name of the tool that is to be evaluated, such as "nogout." or "annotations" . The term "download_dir" refers to the data folder that has been downloaded from OpenDataLab.

notes: Annotations also should  be cleaned.
  ```
  cd evaluate_tool
  python clean_photo.py --tool_type annotations --download_dir datasets/annotations
  ```
- **step2**
  
Then, please place the Markdown files which produced by evaluated tool into the datasets/tools directory, please ensuring that the filenames match the names of the downloaded PDF files.
```
cd evaluate_tool
python markdown_calculate.py --tool_type tools --download_dir datasets/tools 
```
- **step3**
  
If you wish to select one of the types for evaluation, please proceed with the --types, eg "academic_literature", all is defalut

```
cd evaluate_tool
python markdown_calculate.py --tool_type tools --download_dir datasets/tools --types dataset_type
```
# Contact
For any questions about the dataset, please contact the authors by wechat opendatalab_yunying.

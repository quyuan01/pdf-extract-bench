# 介绍
MPB（Miner-PDF-Benchmark）是一套为大规模模型数据场景设计的端到端PDF文档理解评估套件。它确保了文件粒度上的人类可读性，并提供了PDF分类标签。该数据集总共包含350个PDF文件和8410页PDF，包括书籍、教材、学术文献、PPT转PDF、试卷等11种类型的数据集。它为大规模模型数据的开发者和工具开发者提供了PDF文档理解能力的评估参考。

注意：PDF-benchmark数据集只能用于非商业研究目的。

# 数据集来源
MPB数据集来源于多种渠道，包括arXiv、Sci-Hub、教科书、试卷、历史文献等，参考了lamma和internlm 20b的语料库比例。不同子集的来源和组成如下：

| 类别                  | 标签                 | 文件数 | 总页数 | 描述                                                                                    |
|-----------------------|---------------------|--------|--------|------------------------------------------------------------------------------------------|
| 研究报告             | research_report    | 70     | 875    | 包含丰富的表格信息，具有单栏、双栏和复杂布局。                                       |
| 普通教材             | ordinary_textbook  | 40     | 388    | 单栏布局，黑白颜色，包含丰富的公式。                                                   |
| ... （此处省略其他类别的翻译以节省空间） ...

# 统计信息
<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/43176747-4f03-42ad-b48b-a4448fc0dc0e" width="350" height="200" alt="The distribution of pages">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/fb06f784-f22f-4897-9b7e-00cf7f622e38" width="350" height="200" alt="The distribution of PDF file"> 

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/d233a4ca-c54a-41f3-be96-8b80b1b0b740" width="350" height="200" alt="The distribution of md language">  
<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/5ff056a7-6094-420b-8a93-a31585da9451" width="350" height="200" alt="The distribution of PDF  Type">  

# 指标

## 提取率
提取率（ER）是从PDF文件成功生成Markdown（.md）文件的数量与PDF文件总数的比率。

$$ \text{ER} = \frac{\text{hypothesiscnt}}{\text{referencecnt}} $$

## 相似度得分

### 重叠得分
对于一组假设文本块 `H` 和一组参考文本块 `R`，使用函数 \( F(H_{\text{chunk}}, R_{\text{chunk}}) \) 计算每个假设文本块与参考文本块之间的最大相似度得分，该函数返回0到1之间的值。

$$ \text{maxscore}(H_{\text{chunk}}, R) = \max_{R_{\text{chunk}} \in R} \left[ F(H_{\text{chunk}}, R_{\text{chunk}}) \right] $$

### 平均得分
对于所有假设文本块的最大得分集合 `maxscore`，计算平均得分 $ \text{Mean\_score} $：

$ \text{Mean\_score} = \text{mean}(maxscore) $

### 最终得分
最终得分是假设文本块集合与参考文本块集合之间的平均对齐得分，表示为 $ \text{Score}(T_H, T_R) $：

$$ \text{Score}(T_H, T_R) = \text{Mean}\left(\max_{R_{\text{chunk}} \in R} \left[F(H_{\text{chunk}}, R_{\text{chunk}}) \right]\right) $$

## 编辑距离

### 描述
它是一种测量两个字符串之间差异的方法。它定义为将一个字符串转换为另一个字符串所需的最少单字符编辑操作次数。这些编辑操作包括插入、删除和替换字符。

### 用途
为了减少换行和空格对得分的影响，我们在预处理后计算两个字符串之间的编辑距离。

### 引用
[Levenshtein, V.I., et al.: Binary codes capable of correcting deletions, insertions,
and reversals. In: Soviet physics doklady. vol. 10, pp. 707–710. Soviet Union (1966)]
https://nymity.ch/sybilhunting/pdf/Levenshtein1966a.pdf


## BLEU

### 描述
BLEU分数是一个介于0到1之间的值，较高的BLEU分数通常表示更好的翻译质量。

### 用途
我们在nltk分词后计算两个字符串的sentence_bleu，使用method1作为平滑函数。

### 引用
[Papineni, K., Roukos, S., Ward, T., Zhu, W.J.: Bleu: a method for automatic
evaluation of machine translation. In: Proceedings of the 40th annual meeting of
the Association for Computational Linguistics. pp. 311–318 (2002)]
https://aclanthology.org/P02-1040.pdf 

# 结果
### 总体平均得分
| 方案               | 提取率（↑） | 相似度得分（↑） | 编辑距离（↓） | BLEU得分（↑） |
|-------------------|--------------|-----------------|----------------|----------------|
| nogout（开源工具） | 100%        | 0.35            | 0.57           | 0.33          |
| marker（开源工具） | 99.4%       | 0.47            | 0.42           | 0.386         |
| ... （此处省略其他方案的数据以节省空间） ...

### 11种类型的得分
<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/473223d0-fee9-4158-8b79-52c09066d8e1" width="350" height="200" alt="The distribution of sim_socre">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/eb537cf8-f8d0-4815-b1c4-0494d72aa9ae" width="350" height="200" alt="The distribution of edit distance">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/f358d113-72fd-4cea-9f68-d46f01249219" width="350" height="200" alt="The distribution of bleu">  

# 获取数据
数据集可以从opendatalab下载：链接

# 使用方法
1. **步骤1**  
   
将项目克隆到您的环境。
```
  git clone xxx
```

2. **步骤2**  
   
 安装依赖。

  ```
  python -m pip install -r requirements.txt
  ```

3. **步骤3**  
   
  从OpenDataLab下载评估集，并将其放置在`datasets`目录中。
  
  ```
  
  ```
4. **步骤4**
   
  完成评估集的下载后，请执行以下命令以完成初步清洗, "tool_type"是指要评估工具的名称，例如"nogout"或"annotations"。"download_dir"是指从OpenDataLab下载的数据文件夹。  
  ```
  cd evaluate_tool
  python clean_photo.py --tool_type annotations --download_dir datasets
  ```

5. **步骤5**
   
  然后，请将评估工具生成的Markdown文件放入datasets/xx 目录, 和annotaitions同级目录中，请确保文件名与下载的PDF文件名相匹配。
  ```
  cd evaluate_tool
  python markdown_calculate.py --tool_type tools --download_dir datasets/xxx
  ```

# 联系方式

关于数据集的任何问题，请通过微信联系作者：opendatalab_yunying。


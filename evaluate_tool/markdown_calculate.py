import os  
from Levenshtein import distance  
from nltk.translate.bleu_score import sentence_bleu  
from nltk.tokenize import word_tokenize  
import json
# 假设我们有一个简单的BLEU评分函数，这里仅用于示例  
# 注意：这不是标准的BLEU评分，因为它没有多个参考译文  
def simple_bleu_score(candidate, reference):  
    # 假设我们按空格分词，并且没有考虑标点符号等  
    candidate_tokens = word_tokenize(candidate)  
    reference_tokens = word_tokenize(reference)  
    return sentence_bleu([reference_tokens], candidate_tokens, weights=(0.25, 0.25, 0.25, 0.25))  
  
# 定义目录路径  
dir_a = 'D:\code\\testcode\QA\commit_qa\dataset_validator\script\grou truth\教材\普通教材\普通教材-magicpdf'  # 替换为你的A目录路径 ,竞品
dir_b = 'D:\code\\testcode\QA\commit_qa\dataset_validator\script\grou truth\教材\普通教材\普通教材-标准'  # 替换为你的B目录路径, groud_truth
  
# 初始化列表来存储编辑距离和BLEU分数  
edit_distances = []  
bleu_scores = []  
filenames = []
# 遍历A目录和B目录  
for filename in os.listdir(dir_a):  
    if filename.endswith('.md') and not filename.startswith('.'):  # 忽略隐藏文件  
        # 读取A目录中的文件  
        with open(os.path.join(dir_a, filename), 'r', encoding='utf-8') as file_a:  
            content_a = file_a.read()  
  
        # 读取B目录中的对应文件  
        filepath_b = os.path.join(dir_b, filename)  
        if os.path.exists(filepath_b):  
            with open(filepath_b, 'r', encoding='utf-8') as file_b:  
                content_b = file_b.read()  
                filenames.append(filename)
                # 计算编辑距离  
                edit_dist = distance(content_a, content_b)  
                edit_distances.append(edit_dist)  
  
                # 计算BLEU分数（简化版）  
                bleu_score = simple_bleu_score(content_a, content_b)  
                bleu_scores.append(bleu_score)  
        else:  
            print(f"File {filename} not found in directory B.")  

# 计算平均值  
average_edit_distance = sum(edit_distances) / len(edit_distances) if edit_distances else 0  
average_bleu_score = sum(bleu_scores) / len(bleu_scores) if bleu_scores else 0  

fw = open('score.txt', 'w+', encoding='utf-8')
fw.write(json.dumps(filenames, ensure_ascii=False) + "\n")
fw.write(json.dumps(edit_distances, ensure_ascii=False) + "\n")
fw.write(json.dumps(bleu_scores, ensure_ascii=False) + "\n")
fw.write(f"Average Levenshtein Distance: {average_edit_distance}" + "\n")
fw.write(f"Average BLEU Score: {average_bleu_score}" + "\n")
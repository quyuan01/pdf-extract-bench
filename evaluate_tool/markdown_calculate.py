import os  
from Levenshtein import distance  
from nltk.translate.bleu_score import corpus_bleu  
from nltk.tokenize import word_tokenize  
import json 
parser = argparse.ArgumentParser(description="get directory")
parser.add_argument(
    "--standard ",
    type=str,
    required=True,
    help="input standard path",
)

parser.add_argument(
    "--actual",
    type=str,
    required=True,
    help="input actual path",
)
parser.add_argument(
    "--results ",
    type=str,
    required=True,
    help="results path",
)
args = parser.parse_args()

class EvaluationTool:
    def __init__(self, standard_dir, actual_dir, results_dir):
        self.standard_dir = standard_dir
        self.actual_dir = actual_dir
        self.results = results_dir
        self.edit_distances = []
        self.bleu_scores = []
        self.filenames = []
        self.output = dict()
    def get_scores(self):
        for filename in os.listdir(self.actual_dir):  
            if filename.endswith('.md') and not filename.startswith('.'): 
                with open(os.path.join(self.dir_a, filename), 'r', encoding='utf-8') as file_a:  
                    content_a = file_a.read() 
  
                filepath_b = os.path.join(self.standard_dir, filename)  
                if os.path.exists(filepath_b):  
                    with open(filepath_b, 'r', encoding='utf-8') as file_b:  
                        content_b = file_b.read()  
                        self.filenames.append(filename)
                        # 计算编辑距离  
                        edit_dist = distance(content_a, content_b) / max(len(content_a), len(content_b))
                        self.edit_distances.append(edit_dist)  
                        #计算BLUE分数
                        bleu_score = bleu_score(content_a, content_b)  
                        self.bleu_scores.append(bleu_score)  
                        self.output[filename] = {
                            'edit_distance': edit_dist,
                            'bleu_score': bleu_score
                        }
                else:  
                    print(f"File {filename} not found in directory standard_dir.")  
        average_edit_distance = sum(self.edit_distances) / len(self.edit_distances) 
        average_bleu_score = sum(self.bleu_scores) / len(self.bleu_scores) 
        
        # 输出结果到文件
        with open(os.path.join(self.results, 'results.txt'), 'w', encoding='utf-8') as fw:  
            fw.write(f"Average Levenshtein Distance: {average_edit_distance}\n")
            fw.write(f"Average BLEU Score: {average_bleu_score}" + "\n")
            fw.write(json.dumps(self.output, ensure_ascii=False) + "\n")
            fw.close()
def bleu_score(candidate, reference):  
    candidate_tokens = word_tokenize(candidate)  
    reference_tokens = word_tokenize(reference) 
    return corpus_bleu([[reference_tokens]], [candidate_tokens])  

if __name__ == "__main__":
    standard_dir = args.standard
    actual_dir = args.actual
    results_dir = args.results
    evaluation_tool = EvaluationTool(standard_dir, actual_dir, results_dir)
    evaluation_tool.get_scores()




import openxlab
openxlab.login(ak=<Access Key>, sk=<Secret Key>) #进行登录，输入对应的AK/SK

from openxlab.dataset import info
info(dataset_repo='OpenDataLab/Miner-PDF-Benchmark') #数据集信息查看

from openxlab.dataset import query
query(dataset_repo='OpenDataLab/Miner-PDF-Benchmark') #数据集文件列表查看

from openxlab.dataset import get
get(dataset_repo='OpenDataLab/Miner-PDF-Benchmark', target_path='.')  # 数据集下载

from openxlab.dataset import download
download(dataset_repo='OpenDataLab/Miner-PDF-Benchmark',source_path='/README.md', target_path='.') #数据集文件下载
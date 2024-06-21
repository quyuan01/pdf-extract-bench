
  pip install openxlab #安装

  pip install -U openxlab #版本升级
  
  import openxlab
  openxlab.login(ak=<Access Key>, sk=<Secret Key>) #进行登录，输入对应的AK/SK

  from openxlab.dataset import info
  info(dataset_repo='quyuan/Miner-PDF-Benchmark') #数据集信息查看

  from openxlab.dataset import query
  query(dataset_repo='quyuan/Miner-PDF-Benchmark') #数据集文件列表查看

  from openxlab.dataset import get
  get(dataset_repo='quyuan/Miner-PDF-Benchmark', target_path='/path/to/local/folder/')  # 数据集下载

  from openxlab.dataset import download
  download(dataset_repo='quyuan/Miner-PDF-Benchmark',source_path='/README.md', target_path='/path/to/local/folder') #数据集文件下载
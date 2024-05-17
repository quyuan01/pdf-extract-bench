import openxlab
openxlab.login(ak="lvj9vxjbg2llw21xz0d2", sk="qlyrpnbdmoonvjjdondxmmgxlb2g4879lyzk5agq") #进行登录，输入对应的AK/SK

from openxlab.dataset import info
info(dataset_repo='quyuan/PDF-bench') #数据集信息查看

from openxlab.dataset import query
query(dataset_repo='quyuan/PDF-bench') #数据集文件列表查看

from openxlab.dataset import get
get(dataset_repo='quyuan/PDF-bench', target_path='/path/to/local/folder/') # 数据集下载

from openxlab.dataset import download
download(dataset_repo='quyuan/PDF-bench',source_path='/README.md', target_path='/path/to/local/folder') #数据集文件下载
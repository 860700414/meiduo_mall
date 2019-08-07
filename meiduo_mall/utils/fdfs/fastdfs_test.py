from fdfs_client.client import Fdfs_client
client=Fdfs_client('/home/python/Desktop/meiduo_mall/meiduo_mall/utils/fdfs/client.conf')
ret = client.upload_by_filename('/home/python/Desktop/下载.png')
print(ret)
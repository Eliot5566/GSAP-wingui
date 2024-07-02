import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # 使用__file__ 獲取當前文件絕對路徑
print (ROOT_DIR) # 打印當前文件絕對路徑

def get_path(relative_path):
    return os.path.join(ROOT_DIR, relative_path)


file_path = get_path('data/example.txt')
with open(file_path, 'r') as file: # 使用with open() as file: 打開文件 'r' 表示讀取
    content = file.read()
    print(content)

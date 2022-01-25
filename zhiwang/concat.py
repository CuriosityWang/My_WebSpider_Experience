
# 可用于多个excel文件的合并

import pandas as pd
import os


def Read_Folder(path):
    """
    读取文件夹下所有文件
    """
    FolderPath = path
    files = os.listdir(FolderPath)
    files.sort(key=lambda fn: os.path.getmtime(FolderPath+'/'+fn))
    return files


if __name__ == '__main__':

    lst = Read_Folder("./second_page")
    excels = [pd.read_excel("./second_page/" + i) for i in lst]
    df = pd.concat(excels)
    df.to_excel("concat.xlsx", index=False)
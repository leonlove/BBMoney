# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 09:54:46 2023

@author: leon
"""

import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

def DataCompare():
    print("国电通GIM数据之亿力与国遥生产状况对比！")
    base_dir = r'D:\WorkSpace\SGGlobe\项目管理\国电通-基建全过程和电网数字工程化\数据对比'
    excel_yl = base_dir + '\\' + '李盼-亿力-电网工程0607.xls'
    excel_gy = base_dir + '\\' + '李盼-国遥-工程数字化0607.xls'
    excel_project = base_dir + '\\' + 'PROJECT.xlsx'
    excel_xl_project = base_dir + '\\' + 'XL_PROJECT.xlsx'
    
    # new_xl_pro = base_dir + '\\' + 'XL_PROJECT1.csv'
    
    
    df_yl = pd.read_excel(excel_yl)
    df_gy = pd.read_excel(excel_gy)
    df_project = pd.read_excel(excel_project)
    df_xl_project = pd.read_excel(excel_xl_project)
    
    # 第一步，先整理project表
    print(df_project.loc[df_project['ATTACHID'].str.endswith('.gim'),'ATTACHNAME'])
    df_project.loc[df_project['ATTACHID'].str.endswith('.gim'),'ATTACHNAME'] = 
    print(df_project.loc[df_project['ATTACHID'].str.endswith('.gim'),'ATTACHNAME'])
    # 第二步，更新xl_project表
    # 第三步，对比亿力和国遥的表，分析原因
    
    # df_xl_project_new = df_xl_project.update(df_project)
    # df_xl_project.update(df_project)
    # print(df_xl_project.to_csv(new_xl_pro,index=False))
    # print(pd.merge(df_xl_project,df_project,on=['ID'],how='left').to_csv(new_xl_pro))
    # df_new = df_yl.loc[~df_yl['ID'].isin(df_gy['ID'].to_list())]
    # df_new['提交时间'] = pd.to_datetime(df_new['提交时间']) # date转为时间格式
    
    # print(df_xl_project)
    pass
if __name__ =="__main__":
    DataCompare()
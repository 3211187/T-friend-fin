import pandas as pd
import json



class FileSeg():
    def file_seg(self, commend, save_path, path_2, orient='records'):

        filename = 'test_file.json'
        

        #with open(path_2 + filename) as f:
        #    json_data = json.load(f)
        #df = pd.DataFrame.from_dict(json_data, orient='columns')
        df = pd.read_json(path_2 + filename, orient='records', dtype=False)
        #print('result :', df.head())

        # pre_data = df.loc[:, [name,name2]].astype('str')

        ## 매입/매춰 나누기
        C_in = []
        C_out = []

        for i in range(len(df)):
            # #print(df.loc[i,['CD_SCRP']].values)
            if df.loc[i, ['CD_TRAN']].item() == 'home1in' or df.loc[i, ['CD_TRAN']].item() == 'home2in':
                if df.loc[i, ['NM_ITEM']].isnull().values.any(): df.loc[i, ['NM_ITEM']] = 0
            #else :
            
            if df.loc[i, ['TP_BIZ_C']].isnull().values.any(): 
                df.loc[i, ['TP_BIZ_C']] = 0
           #     #print("TP_BIZ_C Check!!")
            '''
            if df.loc[i, ['TP_BIZ_C']].item()=='':
                df.loc[i, ['TP_BIZ_C']] = 0
                #print("TP_BIZ_C Check!!")     
            '''
            name = df.loc[i, ['CD_TRAN']].item()
            name_list = list(name)
            last_num = len(name_list) - 1
            if name_list[last_num] == 'n':
                C_in.append(i)
            else:
                C_out.append(i)

        df_in = df.iloc[C_in, :]
        df_in = df_in.reset_index()
        df_in = df_in.drop(['index'], axis=1)

        df_out = df.iloc[C_out, :]
        df_out = df_out.reset_index()
        df_out = df_out.drop(['index'], axis=1)
        if commend == 'test':
            df_out['CD_ACCOUNT'] = 401
        #df_out['CD_DEDU'] = 0

        #save_path = 'C:\\Users\\ialab\\Desktop\\T-Friend\\process\\'
        df_in.to_json(save_path + 'in_file.json', orient='records', double_precision=15, default_handler=callable,force_ascii=False)
        df_out.to_json(save_path + 'out_file.json', orient='records', double_precision=15, default_handler=callable,force_ascii=False)
        #df_in.to_excel(save_path + 'in_file.xlsx', 'w', encoding='utf-8')
        #df_out.to_excel(save_path + 'out_file.xlsx', 'w', encoding='utf-8')


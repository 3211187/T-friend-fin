import pandas as pd
import json


class FileSeg2():
    def file_seg2(self, PATH):
        #PATH = 'C:\\Users\\ialab\\Desktop\\T-Friend\\process\\'
        filename = 'in_file.json'
        
        #with open(PATH + filename) as f:
        #    json_data = json.load(f)
        #df = pd.DataFrame.from_dict(json_data, orient='columns')
        df = pd.read_json(PATH + filename, orient = 'records', dtype=False)
        #print(df.head())

        # pre_data = df.loc[:, [name,name2]].astype('str')

        ## 계산서/영수증/기타 나누기
        C_12 = []
        C_34 = []
        C_etc = []
        save_etc = 0

        for i in range(len(df)):
            # #print(df.loc[i,['CD_SCRP']].values)
            name = df.loc[i, ['CD_TRAN']].item()
            if name == 'home1in' or name == 'home2in':
                C_12.append(i)
            elif name == 'home3in' or name == 'home4in':
                C_34.append(i)
            else:
                C_etc.append(i)

        #save_path = 'C:\\Users\\ialab\\Desktop\\T-Friend\\process\\'

        if len(C_12) > 0:
            df_12 = df.iloc[C_12, :]
            df_12 = df_12.reset_index()
            df_12 = df_12.drop(['index'], axis=1)
            df_12.to_json(PATH + '12_file.json', orient='records', double_precision=15, default_handler=callable,force_ascii=False)
            #df_12.to_excel(PATH + '12_file.xlsx', 'w', encoding='utf-8')

        if len(C_34) > 0:
            df_34 = df.iloc[C_34, :]
            df_34 = df_34.reset_index()
            df_34 = df_34.drop(['index'], axis=1)
            df_34.to_json(PATH + '34_file.json', orient='records', double_precision=15, default_handler=callable,force_ascii=False)
            #df_34.to_excel(PATH + '34_file.xlsx', 'w', encoding='utf-8')

        #print(len(C_etc))
        if len(C_etc) > 0:
            df_etc = df.iloc[C_etc, :]
            df_etc = df_etc.reset_index()
            df_etc = df_etc.drop(['index'], axis=1)
            df_etc.to_json(PATH + 'etc_file.json', orient='records', double_precision=15, default_handler=callable,force_ascii=False)
            #df_etc.to_excel(PATH + 'etc_file.xlsx', 'w', encoding='utf-8')
            return 1


        return 0


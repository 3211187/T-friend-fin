import pandas as pd


class Convert():
    def __init__(self, path_json, path1, path3):
        self.path_json = path_json
        self.path1 = path1
        self.path3 = path3

    def convert(self, etc):
        #path_json = 'C:\\Users\\ialab\\Desktop\\T-Friend\\json\\'
        #path1 = 'C:\\Users\\ialab\\Desktop\\T-Friend\\pre\\'

        file_12 = 'e_bill_2019_uniq.json'
        #data = pd.read_excel(self.path1 + file_12, index_col=0)
        data = pd.read_json(self.path1 + file_12, orient='records',dtype=False)
       
        file_34 = 'cash_train.json'
        #data1 = pd.read_excel(self.path1 + file_34, index_col=0)
        data1 = pd.read_json(self.path1 + file_34,orient='records',dtype=False)

        #path3 = 'C:\\Users\\ialab\\Desktop\\T-Friend\\process\\'
        file_extra = 'out_file.json'
        #data3 = pd.read_excel(self.path3 + file_extra, index_col=0)
        data3 = pd.read_json(self.path3 + file_extra, orient='records',dtype=False)

        if etc == 1:
            file_ex = 'etc.json'
            #data2 = pd.read_excel(self.path1 + file_ex, index_col=0)
            data2 = pd.read_json(self.path1 + file_ex, orient='records',dtype=False)

            data_merge = pd.concat([data, data1, data2, data3], axis=0)
            data_merge = data_merge.reset_index()
            data_merge = data_merge.drop(['index'], axis=1)
            #print(data_merge)
            data_merge.to_json(self.path_json + 'RES.json', orient='records', double_precision=15, default_handler=callable,
                               force_ascii=False)
            return

        data_merge = pd.concat([data, data1,data3], axis=0, sort = False)
        data_merge = data_merge.reset_index()
        data_merge = data_merge.drop(['index'], axis=1)
        #print("data_merge : ", data_merge)
        data_merge.to_json(self.path_json + 'RES.json', orient='records', double_precision=15, default_handler=callable,
                           force_ascii=False)




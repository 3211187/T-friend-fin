import pandas as pd
import json

class FILTER_CNN(object):
    def __init__(self,T, excel_PATH, filter_name):
        self.T = T
        self.excel_PATH = excel_PATH
        self.filter_name = filter_name + '.json'

    def main_f_cnn(self):

        e_name = self.filter_name
        if self.T == '계산서':
            raw_DATA = 'e_bill_2019_uniq.json'
            #e_name = '계산서_filter_cnn.xlsx'
        elif self.T == '영수증':
            raw_DATA = 'cash_train.json'
            #e_name = '영수증_filter_cnn.xlsx'
        elif self.T == '기타':
            raw_DATA = 'etc.json'

        #df = pd.read_excel(self.excel_PATH + raw_DATA, encoding='utf-8', sheet_name='Sheet1', index_col=0)
        df = pd.read_json(self.excel_PATH + raw_DATA,orient='records',dtype=False)
        #with open(self.excel_PATH + raw_DATA) as f:
        #    json_data = json.load(f)
        #df = pd.DataFrame.from_dict(json_data, orient='columns')

        list = []
        count = 0
        #print('Selecting less than 80% accuracy...(CNN)')
        for i in range(len(df)):
            if float(df.loc[i,['predict']].item())<0.8:
                list.append(i)
                count +=1
        #print('count : ',count)

        df_1 = df.iloc[list,:]

#        df_1.to_excel('/home/cent/Documents/github/T-friend/filter_cnn/' + e_name)
        df_1.to_json('./filter_cnn/' + e_name, orient='records', double_precision=15, default_handler=callable,force_ascii=False)




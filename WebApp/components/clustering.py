import pandas as pd
import numpy as np

"""
ここでは、体質診断を行なった結果のDataFrameに対して点数化を行い、複数の体質に分けていく：
"""
# https://mainichigahakken.net/health/article/post-1961.php これを参考にした
 
class Taishitsu():

    def __init__(self,data):
        self.data = data


    

    def calculate_result(self):

        weights_data = {
        1:  [0, 0, 0, 1, 3, 0, 1, 1], # 胸やおなかが...
        2:  [2, 0, 1, 0, 3, 0, 0, 1], # イライラしやすく...
        3:  [2, 3, 1, 0, 3, 1, 0, 1], # 不眠になりやすい
        4:  [0, 0, 0, 0, 0, 0, 0, 2],
        5:  [1, 0, 0, 0, 0, 0, 0, 2],
        6:  [0, 0, 0, 0, 0, 3, 3, 1],
        7:  [0, 0, 0, 0, 0, 3, 0, 0],
        8:  [0, 0, 0, 1, 0, 0, 3, 1],
        9:  [0, 0, 0, 0, 0, 0, 3, 1],
        10: [1, 3, 0, 0, 0, 2, 0, 0],
        11: [0, 0, 3, 1, 0, 0, 2, 1],
        12: [0, 0, 0, 0, 0, 0, 3, 2],
        13: [0, 0, 0, 0, 0, 3, 0, 0],
        14: [1, 0, 3, 2, 2, 0, 2, 1],
        15: [0, 0, 3, 1, 1, 0, 1, 1],
        16: [0, 0, 0, 0, 0, 3, 1, 1],
        17: [0, 0, 0, 1, 3, 1, 2, 1],
        18: [1, 3, 1, 2, 0, 0, 0, 0],
        19: [2, 3, 0, 0, 0, 0, 0, 0],
        20: [1, 3, 0, 1, 1, 0, 1, 1],
        21: [3, 0, 0, 0, 0, 2, 2, 1],
        22: [3, 0, 0, 0, 0, 0, 0, 1]
        }

        weights_df = pd.DataFrame.from_dict(
            weights_data,
            orient='index',
            columns=['Lack_Moisture','Lack_Blood','Lack_Energy','Lack_Heat',
                    'Stagnation_energy','Stagnation_blood','Moisture_excess','Heat_Moisture_excess']
        ).T

    
        user_answer_series= self.data['answer'].apply(lambda x: 1 if x=="Yes" else 0)
        
        result = weights_df.dot(user_answer_series.values)
        
        

        return result 
    
    def type_classify(self,result):
        
        result_sorted = result.sort_values(ascending=False)
        typelist = result_sorted.index
        
        return typelist[0]
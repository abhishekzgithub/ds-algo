# string_list=['apple','ball','elephant','zebra']
# #find longest element in list

# maxi=0
# max_ele=None
# for ele in string_list:
#     if maxi<len(ele)-1:
#         maxi=max(len(ele)-1,maxi)
#         max_ele=ele

# print(maxi,max_ele)

# data = {
#     'id':['1','2','3','4','5'],
#     'student':['A','B','C','D','E'],
#     'subject1':[90,85,87,60,80],
#     'subject2':[98,90,75,55,88],
#     'subject3':[80,70,90,70,80],
# }

 

# ## (i) add total score as new column ,
# # (ii) add percentage column by lambda function,
# # (iii) find highest scoring student
# import pandas as pd
# dataframe=pd.DataFrame(data)
# dataframe["total_score"]=
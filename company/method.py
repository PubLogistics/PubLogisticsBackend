from django.db.models.query import RawQuerySet
def model2jsonArr(data:RawQuerySet):
    rData = []
    for p in data:
        p.__dict__.pop("_state") # 除去'model、pk'
        rData.append(p.__dict__) 
    return rData
# ————————————————
# 版权声明：本文为CSDN博主「xiaotuwai8」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/xiaotuwai8/article/details/104729458
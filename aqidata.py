import urllib.request as urllib
import json
import pymongo
 
url = 'https://raw.githubusercontent.com/kirkchu/mongodb/main/aqi.json'
 
# 下載 JSON 資料並解析
response = urllib.urlopen(url)
text = response.read().decode('utf-8')
print(text)
text = text.replace('PM2.5', 'PM2_5')  #因為.有其他含意，故用_替換
text = text.replace('"AQI": ""', '"AQI": "-1"')  #指標為空的用-1替換
jsonObj = json.loads(text)
 
# 將資料存進opendata資料庫中的AQI資料表
client = pymongo.MongoClient()
db = client.opendata  #client代表連線，opendata代表資料庫
db.AQI.insert_many(jsonObj['records'])  #所有資料會放到records這個key裡面，後面的資料型態為陣列，只存records下面的資料




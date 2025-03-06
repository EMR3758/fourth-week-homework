import json 

with open("/Users/emirhanozcan/Desktop/veri bilimi ödev/Phyton ile Veri Bilimi 4.Hafta Ödev/theoretical-questions/answer.json","r",encoding="utf-8") as data:
    file = json.load(data)
    for key,value in file.items():
        if isinstance(value,dict):
            print(f"{key}:")
            for sub_key,sub_value in value.items():
                print(f"{sub_key}: {sub_value}")
        elif isinstance(value,list):
            print(f"{key}:")
            for item in value:
                print(f"  {item}")
                
        else: 
            print(f"{key}: {value}")
        print()
        
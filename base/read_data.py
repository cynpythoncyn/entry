import yaml,os


class ReadData():

    def __init__(self,file_name):
        # cwd = current work dirctionary 当前工作目录 即项目根目录
        self.file_path = os.getcwd() + os.sep + "data" + os.sep + file_name
        # self.file_path = os.getcwd() + os.sep + file_name

    def return_data(self):

        with open(self.file_path,"r",encoding='utf-8') as f:
            # 这里会有yaml warning ，解决：添加 Loader
            data = yaml.load(f, Loader=yaml.FullLoader)

        # list_data = list()
        # for i in data.keys():
        #     list_data.append((i,data.get(i).get(key)))

        return data

    def return_search_data(self,key,key1):
        data = self.return_data()
        # print(type(data))
        list_data = list()
        for i in data.keys():
            if i == key:
                list_data.append((i,data.get(i).get(key1)))

            # print(list_data ,i)



        return list_data

# if __name__ == '__main__':
#     print(ReadData("search_data.yaml").return_search_data("input_text"))


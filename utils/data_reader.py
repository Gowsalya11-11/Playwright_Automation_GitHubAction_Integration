import json


class DataReader:
    _data = None

    @staticmethod
    def read_json(file_path="testdata/logindata.json"):
        if DataReader._data is None:
            with open(file_path, "r") as file:
                DataReader._data = json.load(file)
        return DataReader._data

    @staticmethod
    def get(key, file_path="testdata/logindata.json"):
        data = DataReader.read_json(file_path)
        return data.get(key)
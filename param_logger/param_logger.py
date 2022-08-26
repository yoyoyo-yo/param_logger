import os
import functools
import csv

    
class ParamLogger():
    def __init__(self, name, root_path='./', file_suffix='_log', meta_info={}):
        self.name = name
        self.root_path = root_path
        self.file_suffix = file_suffix
        self.all_data = []
        self.keys = []
        self.data = []
        self.meta_info = meta_info

        print('ParamLogger output >>', self.get_filepath())

    def get_filepath(self):
        return os.path.join(self.root_path, self.name + self.file_suffix + '.csv')

    def add_meta_info(self, meta_info=None):
        self.meta_info.update(meta_info)

    def delete_meta_info(self):
        self.meta_info = {}
        
    def get_data_length(self):
        return len(self.all_data)
    
    def get_column_length(self):
        return len(self.keys)
        
    def add_param(self, key, value, data_index=None, update=False):
        assert type(key) is str
        
        if data_index and data_index >= self.get_data_length():
            print(f'[WARNING]invalid data_index = {data_index}. Current data size = {self.get_data_length()}, so process was skipped')
            return
        
        # add new key
        if key not in self.keys:
            self.keys.append(key)
            
        # select target data
        if data_index is None:
            target_data = self.data
        else:
            target_data = self.all_data[data_index] 
            
        # get write position in list for adjusting format
        key_idx = self.keys.index(key)
        
        # fit columns size and add data
        if len(target_data) <= key_idx:
            idx_diff = key_idx - len(target_data) + 1
            
            target_data += [None] * idx_diff
            
        target_data[key_idx] = value
                
        # store written data
        if data_index is None:
            self.data = target_data
        else:
            self.all_data[data_index] = target_data
            
        if update:
            self.update()
        

    def add_params(self, params, data_index=None, update=True): 
        assert type(params) is dict
        
        for k, v in params.items():
            self.add_param(k, v, data_index)
            
        if update:
            self.update()

    def delete_params(self):
        self.data = []

    
    def update(self):
        self.all_data.append(self.data)
        self.adjust_size_all_data()
        self.write_csv()
        self.data = []
    
    def write_csv(self):
        
        if len(self.meta_info) == 0:
            _columns = self.keys
            _content = self.all_data
            
        else:
            _columns = self.keys + ['meta_info']
            _content = [self.all_data[0] + [self.meta_info]]
            
            for i in range(1, self.get_data_length()):
                _content.append(self.all_data[i] + [None])
            
        with open(self.get_filepath(), 'w') as log_file:
            writer = csv.writer(log_file)
            writer.writerow(_columns)
            writer.writerows(_content)
                
    
    def adjust_size_all_data(self):
        _max_len = self.get_column_length()
        
        for data_idx in range(self.get_data_length()):
            target_data = self.all_data[data_idx]
            target_data += [None] * (_max_len - len(target_data))
            self.all_data[data_idx] = target_data

    
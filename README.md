# Param Logger

Easy csv logging suporter.

No warranthy.

## Install

```bash
pip install git+https://github.com/yoyoyo-yo/param_logger.git
```

## Usage

You only add ParamLogger instance.
add_param() and add_params() can receive any argument (both existed and new parameter)

```python
import param_logger

plog = param_logger.ParamLogger('exp_v1', root_path='./')

plog.add_meta_info({'fold':0, 'x':4, 'description':'this is test', 'time':'2021-7-31'})
plog.add_param('epoch', 0)
plog.update()
plog.add_param('epoch', 1)
plog.update()
plog.add_param('epoch', 2, update=True)

plog.add_params({'epoch':3, 'loss':0.2, 'accuracy':0.6, 'update':True})
plog.add_params({'epoch':4, 'loss':0.1, 'accuracy':0.8,})
plog.add_params({'epoch':5, 'loss':0.01, 'accuracy':0.6, 'lr':0.001, 'update':True})
```

```bash
ParamLogger output >> ./exp_v1_log.csvz
```

exp_v1_log.csv is below

```bash
	epoch	loss	accuracy	update	lr	 meta_info
0	0	    NaN	    NaN			NaN	    NaN	    {'fold': 0, 'x': 4, ...
1	1	    NaN	    NaN	        NaN	    NaN	    NaN
2	2	    NaN	    NaN	        NaN	    NaN	    NaN
3	3	    0.20	0.6	        True	NaN	    NaN
4	4	    0.10	0.8	        NaN	    NaN	    NaN
5	5	    0.01	0.6	        True	0.001	NaN
```

See >> sample_run.ipynb

## Functions

## ParamLoggerConfig(exp_name, base_path='./', file_suffix='_log')
- exp_name : [str] current id.
- base_path : [str] directory path to save csv.
- file_suffix : [str] csv name suffix.

## class ParamLogger(name, root_path='./', file_suffix='_log', meta_info=None):
- name : [str] current id.
- root_path : [str] directory path to save csv.
- file_suffix : [str] csv name suffix.
- meta_info : [dict] meta information dictionary.

### add_param(key, value, data_index=None, update=False)
Add new value to current data.
- key : [str] paramter name.
- value : [any type] parameter value.
- data_index : [None, int] target data index for adding or replacing value.
- update : [bool] flag whther save file as soon as adding value.

### add_params(kv_dict, data_index=None, update=True)
Add new values to current data.
- kv_dict : [dict] paramter name and value pairs.
- data_index : [None, int] same as add_param.
- update : [bool] same as add_param.

### add_meta_info(meta_info=None):
- meta_info : [dict] meta information dictionary.


### update()
Save historical parameters to csv file.


## License

MIT License
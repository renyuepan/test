import pandas as pd
import yaml

df = pd.DataFrame(pd.read_csv('list.txt',sep="\t"))
sample_df = df.set_index("Proj_ID")
sample_dict = sample_df.to_dict(orient='index')
for key in sample_dict.keys():
    f = open('/mnt/user/errand/projects/HR_ONE/development/TMB_OncoBuster/unassigned/{}.yaml'.format(key),'w')
    #data = sample_dict[key]
    #print(yaml.dump(data,)) 
    yaml.dump(sample_dict[key],f)

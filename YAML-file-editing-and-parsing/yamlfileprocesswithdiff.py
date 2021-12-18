#THIS CODE IS TESTED ON PYTHON 3.8.10
import sys
import yaml
import os
import platform
#Inputs: name of file, and colon separated key-value pair
#Outputs: Modified file
def read_yaml_and_replace(fname, kv_pair):
	#Open file with read access
    input_file = open(fname)
    
	#Check if file is a valid yaml file; if yes, load to dictionary
    try:
        file_data = yaml.load(input_file, Loader=yaml.FullLoader)
        input_file.close()
    except:
        print("File is not in valid YAML format. There are either missing or extra characters.")
        return
	
	#Iterate over dictionary to replace value with kv_pair
    if 'applications' in file_data.keys():	
        for item in file_data['applications']:
            item['env'] = {'APP_Dynamics':{kv_pair.split(":")[0]: kv_pair.split(":")[1]}}
            item['metadata'] = {'labels':{'app.id': kv_pair.split(":")[1]}}
    else:
        print("A required key (applications) was missing.")
        return
	#Convert dictionary to yaml format and write to file - close after use.
    new_fname = "output_"+fname
    out_file = open(new_fname, "w")
    yaml.dump(file_data, out_file, default_flow_style=False, sort_keys = False)
    out_file.close()
    
	#Find difference between original input and generated output file based on operating system
    if(platform.system() == 'Windows'):
        os.system(f'FC /W {fname} {new_fname}')
    else:
        os.system(f'diff -w -b {fname} {new_fname}')
    
    #Verifying format of output YAML file
    new_f = open(new_fname)
    try:
        test_data = yaml.load(new_f, Loader=yaml.FullLoader)
        print("Output file is a valid YAML file")
        new_f.close()
    except:
        print("Output file is not a valid YAML file")
        new_f.close()
    
if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print('Insufficient number of arguments passed.')
        print("Call this program as shown below: ")
        print("python <name-of-script> input_yaml_filename key_value_pair")
    else:
        read_yaml_and_replace(sys.argv[1], sys.argv[2])

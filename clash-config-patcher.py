from urllib import request
from argparse import ArgumentParser

import yaml

parser = ArgumentParser()
parser.add_argument("patch_file")
parser.add_argument("-u","--url",type=str,required=False)
parser.add_argument("-f","--file",type=str,required=False)
parser.add_argument("-o","--output",type=str,required=False)
args = parser.parse_args()

with open(args.patch_file,"r",encoding="utf-8") as sr:
    patch_data = yaml.safe_load(sr)

if args.url != None:
    req = request.Request(
        url=args.url,
        method="GET",
        headers={
            "User-Agent": "ClashforWindows/0.19.26"
        }
    )
    with request.urlopen(req) as res:
        config_data = yaml.safe_load(res.read().decode("utf-8"))
elif args.file != None:
    with open(args.file,"r",encoding="utf-8") as sr:
        config_data = yaml.safe_load(sr)
else:
    raise ValueError("Please provide either --url or --file to load the configuration data.")

    
for key in patch_data:
    cur = config_data
    val = patch_data[key]
    items = key.split("/")
    for i in range(len(items)):
        item = items[i]
        if i == len(items) - 1:
            if isinstance(val,list):
                arr = cur[item] if item in cur else []
                cur[item] = patch_data[key] + arr
            elif isinstance(val,dict):
                dic = cur[item] if item in cur else {}
                dic.update(patch_data[key])
                cur[item] = dic
            else:
                cur[item] = val
        elif not item in cur:
            cur = cur[item] = {}
        else:
            cur = cur[item]


save_path = args.output if args.output != None else f"./config_new.yaml"
with open(save_path,"w",encoding="utf-8") as sw:
    yaml.dump(config_data,sw)
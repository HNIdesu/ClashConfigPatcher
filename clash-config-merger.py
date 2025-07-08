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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
        }
    )
    with request.urlopen(req) as res:
        config_data = yaml.safe_load(res.read().decode("utf-8"))
elif args.file != None:
    with open(args.file,"r",encoding="utf-8") as sr:
        config_data = yaml.safe_load(sr)
else:
    raise ValueError("Please provide either --url or --file to load the configuration data.")

if "rules" in patch_data:
    config_data["rules"] = patch_data["rules"] + config_data["rules"]
if "external-controller" in patch_data:
    config_data["external-controller"] = patch_data["external-controller"]
if "mixed-port" in patch_data:
    config_data["mixed-port"] = patch_data["mixed-port"]
if "bind-address" in patch_data:
    config_data["bind-address"] = patch_data["bind-address"]
if "allow-lan" in patch_data:
    config_data["allow-lan"] = patch_data["allow-lan"]

save_path = args.output if args.output != None else f"./config_new.yaml"
with open(save_path,"w",encoding="utf-8") as sw:
    yaml.dump(config_data,sw)
import re
import sys
import json

kx_config = sys.stdin.read()

#reading Kusaba-X configuration
with open(kx_config, 'r') as file:
        contents = file.read()

ku_dict = {
    "type": re.search(r"\$cf\['KU_DBTYPE'\]\s*=\s*'([^']+)", contents).group(1),
    "host": re.search(r"\$cf\['KU_DBHOST'\]\s*=\s*'([^']+)", contents).group(1),
    "username": re.search(r"\$cf\['KU_DBUSERNAME'\]\s*=\s*'([^']+)", contents).group(1),
    "password": re.search(r"\$cf\['KU_DBPASSWORD'\]\s*=\s*'([^']+)", contents).group(1),
    "database": re.search(r"\$cf\['KU_DBDATABASE'\]\s*=\s*'([^']+)", contents).group(1),
    "randomseed": re.search(r"\$cf\['KU_RANDOMSEED'\]\s*=\s*'([^']+)", contents).group(1),
}

dbprefix = re.search(r"\$cf\['KU_DBPREFIX'\]\s*=\s*'([^']+)", contents)
ku_dict["prefix"] = dbprefix.group(1) if dbprefix else ""

sys.stdout.write(json.dumps(ku_dict))
sys.stdout.flush()

#!/usr/bin/python
from ansible.module_utils.basic import *
import requests

def main():
    fields = {"url": {"required": True, "type": "str"}}

    module = AnsibleModule(argument_spec=fields)
    url=module.params['url']

    try:
        resp = requests.get(url)
        scode = resp.status_code
    except:
        response = {"url": url},{"return_code": "N/A"}
        module.fail_json(msg="Invalid URL!", meta = response)
        
    response = {"url": url},{"return_code": scode}
    module.exit_json(changed=True, meta=response)

if  __name__ == '__main__':
    main()
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/5/24
from common.YamlUtil import load_yaml

if __name__ == '__main__':
    # import os
    # config = os.path.join(os.path.dirname('../source/'), 'detail.yaml')
    # cfg = load_yaml(config)
    # # print(cfg['appium_url'])
    # print(cfg)
    dt = {
        'k1': {
            'k2': 'v2',
            'k3': 'v3',
            'k4':
                {
                    'k5': 'v5'
                }
        }
    }
    # for k, v in dt.items():
    #     print(k + ':')
    #     print(v)
    #     print('\n')
    for k in dt.keys():
        print(k)




'''
Description: 
Version: 1.0
Author: xieyucheng
Date: 2021-06-01 09:50:00
LastEditors: xieyucheng
LastEditTime: 2021-06-02 16:19:02
'''
from flask import Flask

app = Flask(__name__)


if __name__ == '__main__':
    print('hello')
    app.run(host='0.0.0.0', port=5001)

# ps -ef | grep python3 -u nbc_node_test.py
# python3 -u nbc_node_test.py 
# ps -ef |grep nbc_node_test.py
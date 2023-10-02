#!/bin/bash

echo "**** Run test case ****"

pytest -s  test_web.py 

allure serve report --port 4443
# 快速构建REST API

## 快速开始

通过Serverless Framework CLI快速构建一个REST API应用，实现GET/PUT操作。

1. [安装](#1-安装)
2. [配置](#2-配置)
3. [部署](#3-部署)
4. [测试](#4-测试)

### 1. 安装

**安装 Serverless Framework**
```console
$ npm install -g serverless
```

### 2. 配置

通过如下命令直接下载该例子，目录结构如下：

```console
serverless create --template-url 
```

```
.
├── product_action.py
├── user_action.py
├── package.json
└── serverless.yml
```

执行下列命令，安装 Serverless Framework Tencent SCF插件：
```console
$ npm install
```

查看`product_action.py`代码，可以看到接口的传参和返回逻辑：

```python
# -*- coding: utf8 -*-

def product_get():
    # todo: product_get action
    return {
        "result": "it is product_get action"
    }

def product_put():
    # todo: product_put action
    return {
        "result": "it is product_put action"
    }

def main_handler(event, context):
    print(str(event))
    if event["httpMethod"] == "GET":
        return product_get()
    if event["httpMethod"] == "PUT":
        return product_put()
```

查看`serverless.yml`代码，可以看到函数及API网关触发器的配置逻辑
```yml
service: plugin

provider:
  name: tencent
  runtime: Python3.6
  credentials: ~/credentials
  region: ap-singapore

plugins:
  - serverless-tencent-scf

functions:
  user_action_search:
    handler: user_action.student_get
    description: Tencent Serverless Cloud Function
    events:
      - apigw:
          name: user_action_apigw
          parameters:
            stageName: release
            serviceId:
            httpMethod: GET
            path: /user/student/
            enableCORS: true
            serviceTimeout: 10
  user_action_add:
    handler: user_action.teacher_put
    description: Tencent Serverless Cloud Function
    events:
      - apigw:
          name: user_action.teacher
          parameters:
            stageName: release
            serviceId:
            httpMethod: PUT
            path: /user/teacher/
            enableCORS: true
            serviceTimeout: 10
  product_action:
    handler: product_action.main_handler
    description: Tencent Serverless Cloud Function
    events:
      - apigw:
          name: product_action_apigw
          parameters:
            stageName: release
            serviceId:
            httpMethod: ANY
            path: /product/
            enableCORS: true
            serviceTimeout: 10
```

### 3. 部署

通过`sls deploy`命令进行部署，并可以添加`--debug`参数查看部署过程中的信息

如您的账号未[登陆](https://cloud.tencent.com/login)或[注册](https://cloud.tencent.com/register)腾讯云，您可以直接通过`微信`扫描命令行中的二维码进行授权登陆和注册。

```text
$ serverless deploy

Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Uploading service package to cos[sls-cloudfunction-ap-singapore]. plugin-dev-kadtaG-2019-11-27-19-51-55.zip
Serverless: Uploaded package successful /Users/dfounderliu/Desktop/restAPI/plugin/.serverless/plugin.zip
Serverless: Creating function plugin-dev-user_action_search
Serverless: Created function plugin-dev-user_action_search
Serverless: Setting tags for function plugin-dev-user_action_search
Serverless: Creating trigger for function plugin-dev-user_action_search
Serverless: Created apigw trigger plugin-dev-user_action_search_apigw for function plugin-dev-user_action_search success. service id service-5mds4800 url https://service-5mds4800-1250000000.sg.apigw.tencentcs.com/release/user/student/
Serverless: Deployed function plugin-dev-user_action_search successful
Serverless: Creating function plugin-dev-user_action_add
Serverless: Created function plugin-dev-user_action_add
Serverless: Setting tags for function plugin-dev-user_action_add
Serverless: Creating trigger for function plugin-dev-user_action_add
Serverless: Created apigw trigger plugin-dev-user_action_add_apigw for function plugin-dev-user_action_add success. service id service-pnj5msa4 url https://service-pnj5msa4-1250000000.sg.apigw.tencentcs.com/release/user/teacher/
Serverless: Deployed function plugin-dev-user_action_add successful
Serverless: Creating function plugin-dev-product_action
Serverless: Created function plugin-dev-product_action
Serverless: Setting tags for function plugin-dev-product_action
Serverless: Creating trigger for function plugin-dev-product_action
Serverless: Created apigw trigger plugin-dev-product_action_apigw for function plugin-dev-product_action success. service id service-pci7m1ac url https://service-pci7m1ac-1250000000.sg.apigw.tencentcs.com/release/product/
Serverless: Deployed function plugin-dev-product_action successful
Serverless: Service Information
service: plugin 
stage: dev 
region: ap-singapore 
stack: plugin-dev
resources: 0
functions:   user_action_search: plugin-dev-user_action_search
    GET - https://service-5mds4800-1250000000.sg.apigw.tencentcs.com/release/user/student/
  user_action_add: plugin-dev-user_action_add
    PUT - https://service-pnj5msa4-1250000000.sg.apigw.tencentcs.com/release/user/teacher/
  product_action: plugin-dev-product_action
    ANY - https://service-pci7m1ac-1250000000.sg.apigw.tencentcs.com/release/product/
```

### 4. 测试

通过如下命令测试REST API的返回情况：
> 注：如windows系统中未安装`curl`，也可以直接通过浏览器打开对应链接查看返回情况

```console
$ curl -XGET https://service-1z7fl6vc-1250000000.sg.apigw.tencentcs.com/release/user/student/

{"result": "it is student_get action"}
```

```console
$ curl -X PUT https://service-89ocqgsg-1250000000.sg.apigw.tencentcs.com/release/user/teacher/

{"result": "it is teacher_put action"}
```

```console
$ curl -XGET http://service-9t28e0tg-1250000000.sg.apigw.tencentcs.com/release/product/

{"result": "it is product_get action"}
```

#### 配置账户信息（可选）

当前默认支持CLI扫描二维码登录，如您希望配置持久的环境变量/秘钥信息，也可以参考 [配置账号](https://github.com/serverless-tencent/serverless-tencent-scf/blob/master/docs/zh/%E9%85%8D%E7%BD%AE%E8%B4%A6%E5%8F%B7.md) 文档。

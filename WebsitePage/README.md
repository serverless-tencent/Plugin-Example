# 腾讯云Serverless网页Demo

## Demo目的

腾讯云Serverless产品，在为您提供简单快捷的函数计算平台，更可以灵活应用API网关与云函数的，将其组合应用，使用其集成响应功能（参数`integratedResponse`）,可以在函数中返回一个网页。

## 提前准备

* 需要电脑安装Node.js，NPM等必要基础软件

* 需要电脑安装Serverless Framework，[可以点击此处获取安装方法](https://github.com/serverless-tencent/serverless-tencent-scf/blob/master/docs/zh/%E5%BF%AB%E9%80%9F%E5%AE%89%E8%A3%85.md)

* 配置账号信息，[可以点击此处获取配置方法](https://github.com/serverless-tencent/serverless-tencent-scf/blob/master/docs/zh/%E9%85%8D%E7%BD%AE%E8%B4%A6%E5%8F%B7.md)

## 使用方法

* 下载本demo到本地

* 进入到Demo目录

* 执行指令`npm install`安装必要的依赖

* 执行`serverless deeploy`进行部署，部署成功可以看到以下信息：

```text
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Uploading service package to cos[sls-cloudfunction-ap-guangzhou]. websitepage-dev-bCAwfz-2019-11-05-22-32-31.zip
Serverless: Uploaded package successful /Users/dfounderliu/Desktop/SeerverlessPluginDemo/WebsitePage/.serverless/websitepage.zip
Serverless: Creating function websitepage-dev-my_web_page
Serverless: Created function websitepage-dev-my_web_page
Serverless: Setting tags for function websitepage-dev-my_web_page
Serverless: Deployed function websitepage-dev-my_web_page successful
Serverless: Service Information
service: websitepage 
stage: dev 
region: ap-guangzhou 
stack: websitepage-dev
resources: 1
functions:   my_web_page: websitepage-dev-my_web_page
    ANY - https://service-pcrn2ty8-1256773370.gz.apigw.tencentcs.com/release/websitepage-dev-my_web_page

```

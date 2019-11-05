# 自动文本摘要Demo

## Demo目的

通过该例子，希望用户可以创建项目的同时，将所需依赖打包上传。

## 提前准备

* 需要电脑安装Node.js，NPM等必要基础软件

* 需要电脑安装Serverless Framework，[可以点击此处获取安装方法](https://github.com/serverless-tencent/serverless-tencent-scf/blob/master/docs/zh/%E5%BF%AB%E9%80%9F%E5%AE%89%E8%A3%85.md)

* 配置账号信息，[可以点击此处获取配置方法](https://github.com/serverless-tencent/serverless-tencent-scf/blob/master/docs/zh/%E9%85%8D%E7%BD%AE%E8%B4%A6%E5%8F%B7.md)

## 使用方法

* 下载本demo到本地

* 进入到Demo目录

* 执行指令`npm install`安装必要的依赖

* 执行命令`pip install -t . jieba snownlp`安装函数运行时所需的依赖

* 执行`serverless deploy`进行部署，部署成功可以看到以下信息：

```text
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Uploading service package to cos[sls-cloudfunction-ap-guangzhou]. textsummarization-dev-YbdGk3-2019-11-05-23-50-43.zip
Serverless: Uploaded package successful /Users/dfounderliu/Desktop/SeerverlessPluginDemo/TextSummarization/.serverless/textsummarization.zip
Serverless: Creating function textsummarization-dev-text_summarization
Serverless: Created function textsummarization-dev-text_summarization
Serverless: Setting tags for function textsummarization-dev-text_summarization
Serverless: Creating trigger for function textsummarization-dev-text_summarization
Serverless: Deployed function textsummarization-dev-text_summarization successful
Serverless: Service Information
service: textsummarization 
stage: dev 
region: ap-guangzhou 
stack: textsummarization-dev
resources: 1
functions:   text_summarization: textsummarization-dev-text_summarization

```

* 完成之后，可以通过invoke实现远程调试`serverless invoke -f text_summarization --path test.json`:
```text
Serverless: 

{"keywords": ["\u51fd\u6570", "\u817e\u8baf", "\u8fd0\u884c", "\u81ea\u5b9a\u4e49", "COS"], "summary": ["\u60a8\u53ea\u9700\u7f16\u5199\u7b80\u5355\u7684\u3001\u76ee\u7684\u5355\u4e00\u7684\u4e91\u51fd\u6570\u5373\u53ef\u5c06\u5b83\u4e0e\u60a8\u7684\u817e\u8baf\u4e91\u57fa\u7840\u8bbe\u65bd\u53ca\u5176\u4ed6\u4e91\u670d\u52a1\u4ea7\u751f\u7684\u4e8b\u4ef6\u5173\u8054", "\u4e91\u51fd\u6570\u5728\u6267\u884c\u65f6\u5c06\u6839\u636e\u8bf7\u6c42\u8d1f\u8f7d\u6269\u7f29\u5bb9", "\u817e\u8baf\u4e91\u4e91\u51fd\u6570\u662f\u817e\u8baf\u4e91\u63d0\u4f9b\u7684 Serverless \u6267\u884c\u73af\u5883", "\u5728 COS Bucket \u4e0a\u4f20\u65f6\u3001\u5220\u9664\u6587\u4ef6\u65f6\u8fd0\u884c\u4e91\u51fd\u6570\u3001\u5e94\u7528\u7a0b\u5e8f\u901a\u8fc7 SDK \u8c03\u7528\u65f6\u8fd0\u884c\u4e91\u51fd\u6570", "\u53ea\u9700\u4e3a\u8fd0\u884c\u4e2d\u7684\u4e91\u51fd\u6570\u4ed8\u8d39"]}

----------
Log: 
START RequestId: 69ff3f4a-ffe4-11e9-a60a-525400cdceed
Event RequestId: 69ff3f4a-ffe4-11e9-a60a-525400cdceed
Building prefix dict from the default dictionary ...
Building prefix dict from the default dictionary ...
Dumping model to file cache /tmp/jieba.cache
Dumping model to file cache /tmp/jieba.cache
Loading model cost 1.092 seconds.
Loading model cost 1.092 seconds.
Prefix dict has been built succesfully.
Prefix dict has been built succesfully.

END RequestId: 69ff3f4a-ffe4-11e9-a60a-525400cdceed
Report RequestId: 69ff3f4a-ffe4-11e9-a60a-525400cdceed Duration:1237.17ms Memory:1024MB MaxMemoryUsed:658.383MB

```

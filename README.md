# Crawler_Facebook
Facebook crawler for Sentiment Analysis in Python.

大致流程：
从公开名单上获取种子url放入Crawling队列
--> 判断情感状态是否合法（数据库中statusid表里的都合法
--> 抓取基本信息 并 找到关系人（eg.男女朋友）和建立关系的时间
--> 抓取建立关系前三个月内两人在timeline上所有的交互信息
--> 封装入db

未解决的问题：
ajax 呜呜呜呜～～～～

已写类的简介：
MySQL_create 里面是建立数据库的sql
JustText 乱七八糟的测试
Crawler中，facebook_mysql     链接数据库
          fb_per_inf_crawer   寻找种子url ; main调用
          per_data            封装数据
          parse               对status、基本信息等的各种抽取
          
  没讲清楚的，随时发语音问我

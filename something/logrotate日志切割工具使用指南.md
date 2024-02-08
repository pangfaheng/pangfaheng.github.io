# 什么是logrotate

> logrotate是一个日志切割工具，基于crontab定时任务，可以自动完成切割、压缩、清理日志的工作。
>
> logrotate根据文件名、日期、文件大小等属性，自动识别需要清理的文件，支持linux环境和k8s环境。
>
> 本文将提供linux环境和k8s环境的部署方案，并结合logrotate的一些常用场景进行讲解。
>
> 其中，linux环境需要基于ansible进行自动部署，k8s环境基于argocd进行自动部署。
>
> 因此，在部署logrotate前需要参考我之前的文档，部署对应的服务。
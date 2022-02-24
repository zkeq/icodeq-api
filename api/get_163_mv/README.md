### 网易云 MV 直链转换 `API`

🚀 仓库地址：https://github.com/zkeq/icodeq-api/tree/main/api/get_163_mv

🚀 示例地址：https://api.icodeq.com/api/get_163_mv?14351340

🚀 本项目由两部分组成，数据库基于 `redis`

🚀 `/api/get_163_mv` 目录下的 `index.py` 是主要文件

🚀 它会去读取 `redis` 上面的 `163_mv_{id}` 的值

🚀 而 `/api/get_163_mv/Action-fresh.py` 则负责传递 `video` 的值。(部署至Github Action)

🚀 `Github-163-mv-2h.yml` 为定时任务，2小时执行一次

🚀 使用方法为替换 `Action-fresh.py` 里面的 `video_list` 为 mv 的 id
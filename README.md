## 自用API地址
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fzkeq%2Ficodeq-api.svg?type=small)](https://app.fossa.com/projects/git%2Bgithub.com%2Fzkeq%2Ficodeq-api?ref=badge_small)


### 视频解析 `/api/movie`

🚀 花了几小时写的视频解析接口

🚀 特性：实时生成，只要有数据返回就可以看

🚀 首页的解析链接各大平台均可用

🚀 推荐使用电脑访问

🚀 使用方法：使用首页链接或在网址后加问号加关键词搜索

🚀 地址：https://api.icodeq.com/api/movie

------------

### Github 日历 `/api/github`

🚀 原项目地址： https://github.com/Zfour/python_github_calendar_api

------------

### ~图欧君学习资源库短链服务 `/api/tuostudy`~

🚀 ~原理是爬虫读我的 `oss` 上面的 `json` 文件~

🚀 ~然后 `js`  `window.location.replace("/")`~

### 短链服务已成立分支仓库

🚀 https://github.com/zkeq/Tuostudy-Short-url

### `Notion` `database` 做数据库 `api`

🚀 仓库地址：https://github.com/zkeq/Tuostudy-Short-url/tree/main/api/notion-back-json

🚀 示例地址：https://tuo.icodeq.com/api/notion-back-json

### `Weibo` 直链转换 `API` 

🚀 （请在 `vercel` 环境变量中输入自己的 `redis` 密码）

🚀 仓库地址：https://github.com/zkeq/icodeq-api/tree/main/api/weibo_307_video

🚀 示例地址：https://api.icodeq.com/api/weibo_307_video/

🚀 本项目由两部分组成，并且数据库基于 `redis`

🚀 `/api/weibo_307_video` 目录下的 `index.py` 是主要文件

🚀 它会去读取 `redis` 上面的 `video` 的值。

🚀 而 `/api/weibo_307_video/get-new-url` 则负责传递 `video` 的值，每次访问都会传递。

🚀 所以需要将 `SCF_30_min_fresh.py` 部署至云函数，设置半小时刷新一次（每半小时请求一次刷新）

🚀 使用说明为修改成自己的 `redis`，修改自己的视频 ID 定位。

### 微信公共平台 直链转换 `API`

🚀 （请在 `vercel` 环境变量中输入自己的 `redis` 密码）

🚀 仓库地址：https://github.com/zkeq/icodeq-api/tree/main/api/wechat_video_public

🚀 示例地址：https://api.icodeq.com/api/wechat_video_public?wxv_2281669760981450761

🚀 本项目由两部分组成，并且数据库基于 `redis`

🚀 `/api/wechat_video_public` 目录下的 `index.py` 是主要文件

🚀 它会去读取 `redis` 上面的 `video` 的值，如果读不到就去给 `get-new-url` 获取请求，然后自己再去请求 `redis`

🚀 而 `/api/wechat_video_public/get-new-url` 则负责传递 `video` 的值。（支持失败推送堆糖）

🚀 使用说明为修改成自己的 `redis`。

### 网易云 MV 直链转换 `API` (爬虫版)

🚀 仓库地址：https://github.com/zkeq/icodeq-api/tree/main/api/get_163_mv

🚀 示例地址：https://api.icodeq.com/api/get_163_mv?14351340

🚀 本项目由两部分组成，数据库基于 `redis`

🚀 `/api/get_163_mv` 目录下的 `index.py` 是主要文件

🚀 它会去读取 `redis` 上面的 `163_mv_{id}` 的值

🚀 而 `/api/get_163_mv/Action-fresh.py` 则负责传递 `video` 的值。(部署至Github Action)

🚀 `Github-163-mv-2h.yml` 为定时任务，2小时执行一次

### 网易云 MV 直链转换 `API` (逆向版)

🚀 仓库地址：https://github.com/zkeq/icodeq-api/tree/main/api/get_163_mv_vercel

🚀 示例地址：https://api.icodeq.com/api/get_163_mv_vercel?14351340

🚀 后端由 Github Action 驱动！

🚀 本项目由两部分组成，数据库基于 `redis`。

🚀 `/api/get_163_mv_vercel` 目录下的 `index.py` 是主要文件

🚀 它会去读取 `Redis` 上面的 `163_mv_vercel_{id}` 的值

🚀 而 `/api/get_163_mv_vercel/main_local.py` 则负责传递 `video` 的值。

🚀 （爬虫数据依靠 `163.js` 加密函数加密后请求）

🚀 网易云的有效期为 2 小时左右，故两小时执行一次 Action .

> 注：本仓库所有的 `.pass` 后缀的文件，都是为了让 `vercel` 跳过这个文件部署云函数。
>
> 因为 `vercel` 函数一个项目免费版只能部署 12 个函数，所以如果查看的话请去掉 `.pass` 文件...


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fzkeq%2Ficodeq-api.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fzkeq%2Ficodeq-api?ref=badge_large)

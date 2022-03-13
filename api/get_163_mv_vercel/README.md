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

> 请将 `.PASS` 后缀去掉后查看！

### 163mv_fast_API.zip

```cmd
https:///163mv.icodeq.com/docs
```

1. 部署至服务器即可使用
2. 端口号和 `Redis` 地址 自己改
3. 使用说明为
4. https://163mv.icodeq.com/?vid={vid}
5. 详情见  [归档 | 全自动解析 微博/微信 视频 | ZkeqのCoding日志 (icodeq.com)](https://icodeq.com/2022/03e4ec0968c8/)


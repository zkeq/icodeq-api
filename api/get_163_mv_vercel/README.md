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

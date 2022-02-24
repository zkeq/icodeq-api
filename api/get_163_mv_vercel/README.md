### 网易云 MV 直链转换 `API` (解密版)

🚀 仓库地址：https://github.com/zkeq/icodeq-api/tree/main/api/get_163_mv_vercel

🚀 示例地址无，因为 `vercel` 的云函数没有 Node.js 环境，所以只能有了服务器自己搭建或者本地定时。

🚀 故本接口仅做归档处理（可惜 0.0 ）

🚀 本项目由两部分组成，数据库基于 `redis`。

🚀 `/api/get_163_mv_vercel` 目录下的 `index.py` 是主要文件

🚀 它会去读取 `redis` 上面的 `163_mv_{id}` 的值

🚀 而 `/api/get_163_mv_vercel/Action-fresh.py` 则负责传递 `video` 的值。

🚀 （爬虫数据依靠 `163.js` 加密函数加密后请求）

🚀 网易云的有效期为 2 小时左右

> 请将 `.PASS` 后缀去掉后查看！

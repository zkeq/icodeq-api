### 微信公共平台 直链转换 `API`

🚀 （请在 `vercel` 环境变量中输入自己的 `redis` 密码）

🚀 仓库地址：https://github.com/zkeq/icodeq-api/tree/main/api/wechat_video_public

🚀 示例地址：https://api.icodeq.com/api/wechat_video_public?wxv_2281669760981450761

🚀 本项目由两部分组成，并且数据库基于 `redis`

🚀 `/api/wechat_video_public` 目录下的 `index.py` 是主要文件

🚀 它会去读取 `redis` 上面的 `video` 的值，如果读不到就去给 `get-new-url` 获取请求，然后自己再去请求 `redis`

🚀 而 `/api/wechat_video_public/get-new-url` 则负责传递 `video` 的值。（支持失败推送堆糖）

🚀 使用说明为修改成自己的 `redis`。
#### 具体操作
1. 修改 `redis`
2. 测试 `https://api.icodeq.com/api/wechat_video_public/get-new-url?wxv_2281669760981450761`
3. 测试 `https://api.icodeq.com/api/wechat_video_public?wxv_2281669760981450761`

### `Weibo` 直链转换 `API`

🚀 仓库地址：https://github.com/zkeq/icodeq-api/tree/main/api/weibo_307_video

🚀 示例地址：https://api.icodeq.com/api/weibo_307_video/

🚀 本项目由两部分组成，并且数据库基于 `redis`

🚀 `/api/weibo_307_video` 目录下的 `index.py` 是主要文件

🚀 他会判断上次获取直链的时间是什么时候，如果大于 45 分钟就会触发 `/api/weibo_307_video/get-new-url`  

🚀 触发后会获取最新链接，然后更新，如果小于45分钟则直接请求之前获取到的链接返回

🚀 使用说明为修改成自己的 `redis`，修改自己的视频 ID 定位。

#### 具体操作
1. 修改 `redis`
2. 修改 微博获取列表 `url`
3. 修改 视频定位 `id`
4. 测试 `https://api.icodeq.com/api/weibo_307_video/get-new-url`
5. 测试 `https://api.icodeq.com/api/weibo_307_video`

# NetPulse
Smart Ping &amp; Network Analytics Tool
# NetPulse: 轻量级网络延迟与可用性监控工具

NetPulse 是一个用 Python 编写的轻量级、跨平台网络可用性监控工具，旨在帮助开发者和网络管理员实时追踪多个目标服务器的连通状态与网络延迟。项目无任何第三方依赖，即开即用。

## 功能特点

- **跨平台支持**：自动识别并适配 Windows、macOS 和 Linux 的 ping 命令参数。
- **零依赖自举**：仅使用 Python 标准库（`os`、`subprocess`、`time`），无任何多余包体积。
- **自定义监控目标**：支持通过修改配置文件轻松扩展需要监控的服务器集群。
- **清晰的日志输出**：结构化的控制台输出，并带有高精度的时间戳记录。

## 安装步骤

直接将本项目克隆到本地：

```bash
git clone [https://github.com/severus-S/NetPulse.git](https://github.com/severus-S/NetPulse.git)
cd NetPulse

使用说明
直接使用 Python 3 运行监控脚本：
python main.py


后续开发计划 (Roadmap)
[ ] 增加 JSON/CSV 格式日志导出功能，便于进行长期的网络质量数据分析。

[ ] 引入 asyncio 异步执行机制，实现成百上千个监控节点的并发测试。

[ ] 集成 Webhook 告警通知（如钉钉、企业微信、Discord），在服务器离线时实现秒级报警。

开源许可证
本项目基于 MIT 许可证开源 - 详情参见 LICENSE 文件。

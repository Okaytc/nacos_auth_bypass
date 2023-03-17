# nacos_auth_bypass
nacos(QVD-2023-6271)检测工具

本工具仅用于教育和研究目的，以提高安全意识和改进软件开发实践。在使用本工具之前，请确保您遵守了相关法律法规和道德准则。

开发环境：
python3

使用方式（支持单个URL检测和批量检测）：
//url做了合规处理，支持输入ip、ip:port样式
python nacos_auth_bypass.py -u
示例：python nacos_auth_bypass.py -u http://192.168.1.1/

python nacos_auth_bypass.py -f
示例：python nacos_auth_bypass.py -f url.txt

演示截图：
单个检测：

![图片](https://user-images.githubusercontent.com/50813688/225836092-b0aba5cf-5406-418c-afb8-4131dfea5b05.png)

批量检测：

![图片](https://user-images.githubusercontent.com/50813688/225835968-04ba88f8-2ae1-447a-a432-295fc65072df.png)

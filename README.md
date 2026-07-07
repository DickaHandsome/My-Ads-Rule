# My Ads Rule

一个自维护的 AdGuard 格式拦截规则集，覆盖通用去广告、隐私追踪拦截、流氓/钓鱼网站拦截三个方向。

## 规则分类

| 文件 | 说明 |
|------|------|
| [`rule/ads.txt`](rule/ads.txt) | 通用去广告：广告 SDK、开屏、信息流、横幅广告域名 |
| [`rule/privacy.txt`](rule/privacy.txt) | 隐私追踪拦截：统计分析、埋点、行为追踪、设备指纹 |
| [`rule/malware.txt`](rule/malware.txt) | 流氓/钓鱼网站拦截：赌博、诈骗、诱导下载、流氓推广 |
| [`MyRule.txt`](MyRule.txt) | 合并后的主规则文件（自动生成，请勿手动编辑） |

## 使用方法

将主规则文件的 raw 链接订阅到支持 AdGuard 规则的客户端：

```
https://raw.githubusercontent.com/DickaHandsome/My-Ads-Rule/main/MyRule.txt
```

支持的客户端（部分）：
- AdGuard / AdGuard Home
- AdAway
- v2rayNG / Clash（需配置规则集）
- Surge / Quantumult X / Shadowrocket

## 规则格式速查

```
||example.com^          拦截该域名及其所有子域名
@@||example.com^        白名单例外（优先级最高）
/regex/                 正则匹配
! 这是注释行
```

## 本地构建

修改 `rule/` 下的分类文件后，运行合并脚本生成主规则文件：

```bash
python scripts/build.py
```

脚本会读取 `rule/*.txt`，去重合并并生成带版本号的 `MyRule.txt`。

## 自动化

已配置 GitHub Actions（[`.github/workflows/update.yml`](.github/workflows/update.yml)）：
- 当 `rule/` 或 `scripts/` 内容变更并推送到 `main` 时自动重新构建
- 每天北京时间 00:00 定时构建
- 也可在 Actions 页面手动触发

> 首次使用前，请在仓库 **Settings → Actions → General → Workflow permissions** 中开启 **Read and write permissions**，否则自动提交会失败。

## 维护建议

- 新增规则时编辑 `rule/` 下对应分类文件，**不要**直接改 `MyRule.txt`
- 流氓/钓鱼域名时效性强，建议定期清理失效项
- 添加规则前建议用 `nslookup` 或抓包确认域名用途，避免误伤

## 协议

[MIT License](LICENSE)

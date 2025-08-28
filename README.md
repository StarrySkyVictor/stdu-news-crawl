# 石家庄铁道大学官网新闻爬虫（23级金融学生留）

本项目使用 **Playwright**、**Requests**、**BeautifulSoup** 等工具爬取 [石家庄铁道大学官网新闻网](https://xcbnew.stdu.edu.cn/news) 的新闻数据，包括标题、正文、字符数统计等，并支持多线程加速爬取。

---

## 功能特点

- 使用 **Playwright** 自动化获取每一页的新闻链接。
- 使用 **Requests + BeautifulSoup** 解析新闻页面内容。
- 支持 **多线程** 提升爬取速度。
- 自动统计正文的字符数。
- 输出结果至控制台（后续可扩展为保存到数据库/Excel/CSV）。

---

## 环境要求

- **Python 版本**: `Python 3.9+`（建议 3.9 或更高版本）

### 依赖库

安装依赖库：
```bash
pip install playwright requests beautifulsoup4 lxml



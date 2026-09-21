# QA Automation Portfolio

> 一套用 Python 从零搭建的自动化测试框架：覆盖 **Web UI 端到端自动化**、**接口自动化**、**数据驱动**、**CI 持续集成** 与 **大模型应用质量评测**。
> 仓库同时也是我的学习记录，**每天都有提交**。

---

## 一、这个项目包含什么

| 能力                     | 位置                          | 对应日期     |
| ---------------------- | --------------------------- | -------- |
| pytest 基础与数据驱动         | `tests/test_day01_first.py` | Day 1–2  |
| HTTP 协议与请求封装           | `utils/http_client.py`      | Day 3    |
| 测试用例设计文档               | `docs/testcases_login.md`   | Day 4    |
| 接口自动化 + 数据驱动           | `data/api_cases.yaml`       | Day 6    |
| Web UI 自动化（Playwright） | `tests/web/`                | Day 8–13 |
| Page Object 分层         | `tests/web/pages/`          | Day 10   |
| CI 持续集成                | `.github/workflows/ci.yml`  | Day 20   |
| 大模型评测（RAG / Agent）     | `tests/ai_eval/`            | Day 22 起 |

## 二、怎么跑起来

```bash
# 1. 创建虚拟环境
python -m venv venv

# 2. 激活（Windows）
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 安装 Playwright 浏览器（Web 自动化阶段才需要）
playwright install chromium

# 5. 跑全部用例
pytest

# 6. 只跑接口用例
pytest tests/api/ -v

# 7. 生成 HTML 报告
pytest --html=report.html --self-contained-html
```

## 三、目录结构

```
qa-portfolio/
├── conftest.py              # 全局 fixture（公共测试数据、浏览器实例）
├── pytest.ini               # pytest 配置
├── requirements.txt         # 依赖清单
├── utils/
│   └── http_client.py       # HTTP 请求封装层
├── data/
│   └── api_cases.yaml       # 测试用例数据（数据与代码分离）
├── docs/
│   └── testcases_login.md   # 手工测试用例设计
├── pages/                   # Page Object（页面对象层）
├── tests/
│   ├── api/                 # 接口自动化用例
│   └── web/                 # Web UI 自动化用例
└── .github/workflows/
    └── ci.yml               # GitHub Actions 持续集成
```

## 四、每日进度对照表

打卡用。每天完成后在后面打勾，目标：**连续 21 天不断绿**。

| Day | 日期    | 主题                      | 产出                       | 完成  |
| --- | ----- | ----------------------- | ------------------------ | --- |
| 1   | 09-17 | 环境搭建                    | 跑通第一个 pytest 用例          | √   |
| 2   | 09-18 | pytest 进阶 + 首次 HTTP 请求  | fixture / parametrize 用例 | √   |
| 3   | 09-19 | HTTP 协议 + 请求封装          | `http_client.py`         | √   |
| 4   | 09-20 | 测试理论 + 用例设计             | 30 条登录用例文档               | √   |
| 5   | 09-21 | Linux 命令 + SQL          | 能独立看日志定位问题               | √   |
| 6   | 09-22 | 接口自动化                   | 10 条数据驱动用例               | ☐   |
| 7   | 09-23 | 周中收尾                    | README + requirements    | ☐   |
| 8   | 09-24 | **投递日** + Playwright 首例 | 腾讯+荣耀+10 家               | ☐   |
| 9   | 09-25 | 元素定位与等待机制               | 稳定的 UI 用例                | ☐   |
| 10  | 09-26 | Page Object 改造          | `pages/` 分层              | ☐   |
| 11  | 09-27 | UI 用例扩展                 | 累计 10 个 UI 用例            | ☐   |
| 12  | 09-28 | 八股第一轮                   | 网络/OS 笔记                 | ☐   |
| 13  | 09-29 | 框架完善                    | headless + 失败重试          | ☐   |
| 14  | 09-30 | 周中收尾                    | 15 UI + 15 接口            | ☐   |
| 15  | 10-01 | **投递日**                 | 网易雷火 + 累计 40 家           | ☐   |
| 16  | 10-02 | 接口用例扩充                  | 累计 25 条                  | ☐   |
| 17  | 10-03 | 测试平台思维                  | 用例组织与标记                  | ☐   |
| 18  | 10-04 | 性能测试入门                  | Locust/JMeter 基础         | ☐   |
| 19  | 10-05 | 简历打磨                    | 简历 v2                    | ☐   |
| 20  | 10-06 | CI 集成                   | GitHub Actions 跑通        | ☐   |
| 21  | 10-07 | 八股冲刺                    | 手撕 30 题                  | ☐   |
| 22  | 10-08 | **投递日**                 | 美团 + 批量投递                | ☐   |

- 

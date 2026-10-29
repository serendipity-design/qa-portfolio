# QA Automation Portfolio

> 一套用 Python 从零搭建的自动化测试框架：覆盖 **Web UI 端到端自动化**、**接口自动化**、**数据驱动**、**CI 持续集成** 。

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



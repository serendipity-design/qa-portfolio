# 简历素材 · Day 16 版（2026-10-04）

> 所有数字均来自**项目实测**与**GitHub 提交记录**，可被面试官验证。
> 本版取代 `resume-project-week1.md`。Day 20 加了 CI 之后再升级一版。

---

## 一、项目经历（直接复制到简历）

**qa-portfolio —— Python 自动化测试框架**（个人开源项目）
2026.09 – 至今 ｜ Python / pytest / requests / Playwright / PyYAML / Flask / Git
github.com/serendipity-design/qa-portfolio

- 从零搭建覆盖**接口层 + Web UI 层**的 pytest 自动化测试框架，**55 条用例全量回归 25 秒完成**，一条命令触发
- 封装 HttpClient 请求层：统一 base_url / 超时 / 鉴权头入口，捕获 Timeout、ConnectionError 并转换为自定义异常，输出可直接定位的报错；用 session 级 fixture 复用连接
- **YAML 数据驱动 15 条接口用例**（覆盖 GET/POST/PUT/DELETE、404 异常场景、query 参数组合），parametrize 动态生成，**新增用例只需改 YAML、无需改动任何 Python 代码**；并加入响应耗时断言（< 2 秒）
- **自建 Flask 被测服务**（含 id 必传/空值/类型/范围/长度共 9 条校验规则），针对它设计 **10 条边界用例**，覆盖空值、负数、0、非数字、小数、特殊字符、32 位整数上限、超大整数、超长字符串；测试内置后台线程自动拉起被测服务
- Web UI 端采用 **Playwright + Page Object 模式**，封装 LoginPage / ProductPage 完成分层，覆盖登录（成功 / 密码错误 / 空值 / 锁定用户）、登出、商品列表、排序、加购、移除、购物车校验共 15 条用例，全部使用带自动重试的断言消除竞态
- 工程化配套：失败自动截图 hook、日志配置、pytest.ini 标记分组（smoke / regression）、.gitignore 规则、依赖固化

---

## 二、完整 STAR 版（面试照这个讲）

**S 情境**
在校期间为补齐工程实践能力独立发起的项目。起点是"用例散落在脚本里、每加一条就要复制粘贴一整段代码"——这种写法无法维护，也无法规模化成回归套件。

**T 任务**
四点：① 请求层统一封装并处理异常；② 用例数据与代码解耦；③ 覆盖 Web UI 端的端到端链路；④ 补上被测对象的可控性——外部接口不做业务校验，边界场景根本测不出来。

**A 行动**
1. 抽象 HttpClient 请求层，统一 base_url、超时、鉴权头注入入口；捕获 Timeout / ConnectionError 转为自定义 `APIRequestError`，把网络层原始报错转成可定位的提示；session 级 fixture 复用连接
2. 将 15 条接口用例抽到 YAML，用 `pytest.mark.parametrize` 动态生成，覆盖四类 HTTP 方法、404 异常场景与 query 参数；新增用例零代码改动；补响应耗时断言
3. 用 Flask 自建带完整参数校验的被测服务（校验链：必传 → 空值 → 特殊字符 → 非数字 → 小数 → 0 → 负数 → 超上限 → 长度），针对它设计 10 条边界用例，并让测试文件通过后台线程自动拉起服务
4. UI 端引入 Page Object 分层，封装 LoginPage / ProductPage，把元素定位收敛到页面类；用例层只描述业务动作。全部断言使用 Playwright 的 `expect()`（自带重试等待），消除页面渲染延迟导致的偶发失败
5. 补工程化：失败自动截图 hook（放在 `tests/web/conftest.py`，利用 conftest 的目录级作用范围，不影响接口用例）、日志配置、标记分组

**R 结果**
- **55 条用例、全量回归 25 秒**；10 条边界用例 2.18 秒跑完，全部命中预期状态码与错误提示
- 新增接口用例从"改 Python 代码"简化为"YAML 加一行"
- **14 次提交、覆盖 10 个开发日**，代码全部开源可查

---

## 三、面试口语版（30 秒，别背 bullet）

> "我的项目是一个 Python + pytest 的自动化测试框架，覆盖接口和 Web UI 两层。接口这块我做了三件事：一是封装请求层，统一超时和异常处理，网络错误会转成能定位的自定义异常；二是把用例数据抽到 YAML，用 parametrize 动态生成，现在加一条用例只需要改 YAML，Python 代码一行不动；三是用 Flask 自己写了一个带参数校验的被测服务，针对它设计了 10 条边界用例，覆盖空值、类型、范围、长度几个维度。UI 这块用 Playwright 加 Page Object 分层，覆盖登录、加购、购物车这些链路，断言全部用带自动重试的 expect，避免页面没渲染完导致的偶发失败。目前是 55 条用例，全量跑 25 秒。"

## 四、必被追问的问题（提前备好答案）

| 问题 | 回答要点 |
|---|---|
| **为什么做数据驱动？** | 三个点：非技术同学也能维护用例；加用例不碰代码、不会引入语法错误；数据与断言逻辑解耦 |
| **为什么要自建被测服务？** | jsonplaceholder 这类假数据站不做业务校验，永远是 200，边界场景测不出来。服务不可控时先 mock 出校验逻辑再测，这是常规做法 |
| **怎么解决用例偶发失败？** | 根因是页面渲染延迟导致的竞态。用带自动重试的 `expect()` 消除竞态；`--reruns` 只作为最后兜底，不是解决方案 |
| **Page Object 解决了什么？** | 元素定位收敛到页面类，页面改版只改一处；用例层只描述业务动作。同时在 conftest 层面用目录级作用域隔离接口与 UI 的配置 |
| **pytest.raises 什么场景用？** | 验证"应该报错"的用例，比如除零、非法入参。反向用例和正向用例同等重要 |

---

## 五、专业技能（按真实掌握程度分级，别拔高）

```
编程语言：Python（pytest / requests / Playwright 生态）、C（课程基础）

测试框架与库：pytest（fixture、参数化、断言、hook、标记分组）、requests、
             Playwright（同步 API、expect 断言、Page Object）

测试类型与方法：接口自动化、Web UI 自动化、数据驱动测试（DDT）、
               边界值分析与等价类划分、反向用例设计

工具与环境：Git / GitHub、Postman / Apifox、SQLite（增删改查 / 关联查询）、
           Linux 常用命令（grep / tail / curl）、YAML 数据管理、Flask 自建 Mock 服务

专业背景：智能科学与技术专业，修读机器学习、自然语言处理、模式识别、数据挖掘
```

**面试时对每条技能都要能接住追问**，所以上面没写的一律不加：
- ❌ **GitHub Actions / CI** —— Day 20 才做，现在写上去一问就穿帮
- ❌ **JSON Schema 校验** —— 没实现
- ❌ **MySQL** —— 只在 SQLite 上练过 SQL，别写 MySQL
- ❌ **性能测试（JMeter / Locust）** —— 装了 Locust 但没实际跑过压测场景
- ❌ **测试左移 / 右移、持续测试** —— 概念层面了解，但没有实践经历，被追问会悬空

---

## 六、简历数字卡（所有可验证的真实数据）

| 项目 | 数字 | 来源 |
|---|---|---|
| 用例总数 | 55 条 | 实测 `pytest -q` |
| 全量回归耗时 | 25.16 秒 | 实测 |
| 接口用例 | 25 条（15 数据驱动 + 10 边界） | 两个 YAML 实测 |
| HTTP 方法覆盖 | GET ×12 / POST ×11 / PUT ×1 / DELETE ×1 | YAML 统计 |
| 单元测试 | 15 条 | test_day01_first.py |
| UI 用例 | 15 条 | test_login.py + test_inventory.py |
| 边界用例耗时 | 2.18 秒 | 实测 |
| Mock 服务校验规则 | 9 条 | mock_server/app.py |
| 登录用例文档 | 17 条 | docs/testcases_login.md |
| Git 提交 | 14 次 / 覆盖 10 个开发日 | GitHub 提交记录 |

---

## ⚠️ 两个必须处理的诚实问题

**1. 不要写"连续 18 天每日提交"。**

GitHub 记录显示：**14 次提交，覆盖 10 个日期**（9/17、9/18、9/19、9/20、9/21、9/23、9/29、10/1、10/3、10/4）。9/24–9/28、9/30、10/2 是空的。写"连续"会被提交记录当场打脸，**写"14 次提交、跨 10 个开发日"一样有说服力，而且经得起查**。

**2. 有 5 条用例静默丢失，建议修掉。**

`tests/api/api_practice.py` 文件名**缺 `test_` 前缀**，而 pytest.ini 里 `python_files = test_*.py` —— 这 5 条接口练习用例**从未被收集执行**（不报错、不提示，静默消失）。两种处理：

```powershell
# 想让它跑起来：改回 test_ 前缀
mv tests/api/api_practice.py tests/api/test_api_practice.py
pytest -q      # 应该变成 60 passed

# 想归档不跑：移到 docs/ 或改名为 _archive_api_practice.py，并在 README 说明
```

**如果按第一种修，简历数字全部 +5：60 条用例**。修完告诉我，我更新简历里的数字。

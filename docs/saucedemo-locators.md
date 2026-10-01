# saucedemo 定位器速查表

> **所有定位器都是在真实站点上实测确认过的**（2026-10-01，Playwright + Chromium）。
> 写用例时直接查这里，不用每次跑 codegen。

站点：https://www.saucedemo.com/
账号：`standard_user` / `locked_out_user` 等，统一密码 `secret_sauce`

---

## 一、登录页

| 元素 | 定位器 | 备注 |
|---|---|---|
| 用户名输入框 | `#user-name` | |
| 密码输入框 | `#password` | |
| 登录按钮 | `#login-button` | |
| 错误提示 | `[data-test="error"]` | 登录失败时出现 |

**三种失败的真实文案（实测，可直接拿来做断言）：**

| 场景 | 错误文案 |
|---|---|
| 空用户名 | `Epic sadface: Username is required` |
| 密码错误 | `Epic sadface: Username and password do not match any user in this service` |
| 锁定用户（`locked_out_user`） | `Epic sadface: Sorry, this user has been locked out.` |

## 二、商品列表页（登录后的首页）

| 元素 | 定位器 | 备注 |
|---|---|---|
| 页面标题 | `.title` | 文本为 `Products` |
| 商品名 | `[data-test="inventory-item-name"]` | 6 个 |
| 商品价格 | `[data-test="inventory-item-price"]` | 6 个，如 `$29.99` |
| 加购按钮 | `button[data-test^="add-to-cart-"]` | **6 个**，`^=` 是"以...开头" |
| 移除按钮 | `button[data-test^="remove-"]` | 只在已加购的商品上出现 |
| 购物车角标 | `[data-test="shopping-cart-badge"]` | **未加购时不存在**，加购后显示数量 |
| 购物车图标 | `[data-test="shopping-cart-link"]` | 点击进入购物车页 |
| 排序下拉框 | `[data-test="product-sort-container"]` | 见下方选项值 |
| 汉堡菜单按钮 | `#react-burger-menu-btn`（或 `[data-test="open-menu"]`） | 点开侧边栏 |

**排序下拉框的选项值（实测）：**

| 选项值 | 含义 | 排序后第一个商品 |
|---|---|---|
| `az` | 名称 A→Z | — |
| `za` | 名称 Z→A | `Test.allTheThings() T-Shirt (Red)` |
| `lohi` | 价格低→高 | `$7.99` |
| `hilo` | 价格高→低 | — |

## 三、侧边栏菜单（点汉堡按钮后）

| 元素 | 定位器 |
|---|---|
| 登出 | `[data-test="logout-sidebar-link"]` |
| 关闭菜单 | `[data-test="close-menu"]` |
| 重置应用状态 | `[data-test="reset-sidebar-link"]` |

登出后回到登录页（URL `https://www.saucedemo.com/`）。

## 四、购物车页（点购物车图标后）

**注意：进入购物车页后，DOM 切换有延迟**，要等特征元素出现再查。

| 元素 | 定位器 | 备注 |
|---|---|---|
| 购物车里的商品名 | `[data-test="inventory-item-name"]` | 就绪后数量 = 已加购件数 |
| 商品条目容器 | `.cart_item` 或 `[data-test="inventory-item"]` | |
| 结算按钮 | `[data-test="checkout"]` | **用它判断"购物车页是否加载完成"** |
| 继续购物 | `[data-test="continue-shopping"]` | 返回商品列表 |
| 数量标签 | `[data-test="cart-quantity-label"]` | 表头文字 |

---

## 五、实测踩到的坑（写用例时必须知道）

**页面渲染有延迟，裸 `count()` 会拿到错误值。**

实测记录：登录后立刻 `page.locator('[data-test="inventory-item"]').count()` 返回 **0**；
点击购物车图标后立刻数 `[data-test="inventory-item-name"]` 返回 **6**（其实是上一个页面的残留）。
等页面真正就绪后，两个值分别是 6 和 1。

**所以：所有校验都用 `expect(...)`（带自动重试），不要用裸 `assert` + `count()`。**

```python
# ❌ 可能在页面切换的间隙读到旧值 → 偶发失败
assert page.locator('[data-test="inventory-item"]').count() == 6

# ✅ 自动重试，直到条件成立或超时
expect(page.locator('[data-test="inventory-item"]')).to_have_count(6)
```

需要显式等待某个页面加载完成时，等它的特征元素：

```python
page.locator('[data-test="shopping-cart-link"]').click()
page.wait_for_selector('[data-test="checkout"]')     # 等购物车页真正就绪
```

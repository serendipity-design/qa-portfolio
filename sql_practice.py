"""Day 4 附加练习：SQL 十题（SQLite 零配置，Python 自带）

运行方式（在项目根目录、venv 已激活）：
    python sql_practice.py

表结构说明（先看懂再写 SQL：
    students 学生表：id / 姓名 / 班级 / 城市
    scores   成绩表：id / 学生id(对应students.id) / 科目 / 分数
两表通过 scores.student_id = students.id 关联 —— 第 10 题 join 要用。
"""

import sqlite3

# ---------- 连接数据库（:memory: = 存在内存里，零配置，跑完即消失） ----------
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# ---------- 建表 ----------
cur.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    class TEXT,
    city TEXT
)
""")
cur.execute("""
CREATE TABLE scores (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject TEXT,
    score INTEGER
)
""")

# ---------- 造测试数据（埋了几个"不及格"，后面题目会用到） ----------
students = [
    (1, "张三", "智能科学1班", "重庆"),
    (2, "李四", "智能科学1班", "成都"),
    (3, "王五", "智能科学2班", "重庆"),
    (4, "赵六", "智能科学2班", "北京"),
    (5, "钱七", "软件工程1班", "重庆"),
]
scores = [
    (1, 1, "机器学习", 92),
    (2, 1, "Python",   88),
    (3, 2, "机器学习", 75),
    (4, 2, "Python",   95),
    (5, 3, "机器学习", 60),
    (6, 3, "Python",   58),   # 不及格
    (7, 4, "机器学习", 81),
    (8, 5, "Python",   47),   # 不及格
]
cur.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", students)
cur.executemany("INSERT INTO scores VALUES (?, ?, ?, ?)", scores)
conn.commit()

# ---------- 你的 10 条 SQL ----------
# 写法：把 None 换成 SQL 字符串。前两条已写好当示例。
exercises = [
    # 1. 查询所有学生
    ("1. 查询所有学生", "SELECT * FROM students"),

    # 2. 查询重庆的学生
    ("2. 查询重庆的学生（WHERE）", "SELECT * FROM students WHERE city = '重庆'"),

    # 3. 查询所有不及格（< 60）的成绩记录
    ("3. 不及格的成绩（WHERE）", "SELECT * FROM scores WHERE score < 60"),

    # 4. 查询重庆学生里班级为"智能科学1班"的人（WHERE + AND）
    ("4. 重庆的智能科学1班学生（AND）", "SELECT * FROM students WHERE city = '重庆' AND class = '智能科学1班'"),

    # 5. 所有成绩按分数从高到低排（ORDER BY ... DESC）
    ("5. 成绩降序排列（ORDER BY）", "SELECT * FROM scores ORDER BY score DESC"),

    # 6. 只要分数最高的前 3 条（LIMIT）
    ("6. 前 3 名（LIMIT）", "SELECT * FROM scores ORDER BY score DESC LIMIT 3"),

    # 7. 每个班分别有多少学生（GROUP BY + COUNT）
    #    期望输出三行：智能科学1班 2 / 智能科学2班 2 / 软件工程1班 1
    ("7. 各班人数（GROUP BY + COUNT）", "SELECT class, COUNT(*) FROM students GROUP BY class"),

    # 8. 每个科目的平均分（GROUP BY + AVG）
    #    期望输出两行：机器学习 77.0 / Python 72.0
    ("8. 各科平均分（AVG）", "SELECT subject,AVG(score) FROM scores GROUP BY subject"),

    # 9. 平均分低于 70 的科目（GROUP BY + AVG + HAVING）
    #    期望输出一行：Python 72.0？不对——再算算，72 不低于 70。
    #    提示：把阈值定在 75 试试，或者想想"低于 77"该写几。
    ("9. 平均分低于 75 的科目（HAVING）", "SELECT subject,AVG(score) FROM scores GROUP BY subject HAVING AVG(score) < 75"),

    # 10. 关联查询：显示每个学生的姓名 + 科目 + 分数（JOIN）
    #     期望输出 8 行，第一行形如：('张三', '机器学习', 92)
    #     提示：FROM scores JOIN students ON scores.student_id = students.id
    ("10. 学生姓名+科目+分数（JOIN）", "SELECT students.name, scores.subject, scores.score FROM scores JOIN students ON scores.student_id = students.id"),
]

# ---------- 执行并打印（这部分不用改） ----------
for title, sql in exercises:
    print(f"\n=== {title} ===")
    if sql is None:
        print("（还没写）")
        continue
    try:
        rows = list(cur.execute(sql))
        if not rows:
            print("（查询结果为空）")
        for row in rows:
            print(row)
    except Exception as e:
        print(f"SQL 写错了：{e}")

conn.close()
print("\n--- 练习结束。10 题全部出结果后，commit 这个文件。 ---")

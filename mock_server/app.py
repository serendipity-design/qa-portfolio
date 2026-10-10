"""本地被测服务（Mock Server）

为什么需要它？
jsonplaceholder 是"假数据站"——发什么它都返回 200/201，不做任何业务校验。
而你的 10 条边界用例期望的是「400 + 具体错误提示」，这种业务校验行为
必须由一个真实实现了校验逻辑的服务来提供.


启动方式：
    python mock_server/app.py
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

MAX_ID = 2147483647          # 32 位有符号整数上限
MAX_NAME_LEN = 50


@app.post("/users")
def create_user():
    data = request.get_json(silent=True)

    # 1. 请求体本身
    if not data or not isinstance(data, dict):
        return jsonify(msg="请求体不能为空"), 400

    # 2. id 必传
    if "id" not in data:
        return jsonify(msg="id为必传参数"), 400

    uid = data["id"]

    # 3. id 是字符串的两种情况：空串 / 含特殊字符 / 纯字母数字
    if uid == "":
        return jsonify(msg="id不能为空"), 400
    if isinstance(uid, str):
        if not uid.isalnum():                       # 含 @#$ 等特殊字符
            return jsonify(msg="id含有非法字符"), 400
        return jsonify(msg="id必须为数字"), 400       # "abc123xyz"

    # 4. 类型必须是数字（bool 要单独排除，Python 里 True 也是 int）
    if isinstance(uid, bool) or not isinstance(uid, (int, float)):
        return jsonify(msg="id必须为数字"), 400

    # 5. 小数
    if isinstance(uid, float) and not uid.is_integer():
        return jsonify(msg="id必须为整数"), 400
    uid = int(uid)

    # 6. 值的范围：0 / 负数 / 超上限
    if uid == 0:
        return jsonify(msg="id不能为0"), 400
    if uid < 0:
        return jsonify(msg="id不能为负数"), 400
    if uid > MAX_ID:
        return jsonify(msg="id超出范围"), 400

    # 7. name 长度
    name = data.get("name", "")
    if len(name) > MAX_NAME_LEN:
        return jsonify(msg="name超出长度限制"), 400

    return jsonify(msg="请求成功", id=uid, name=name), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)

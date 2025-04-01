import requests
import random
import string
import logging

# 设置日志格式和级别
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 定义 API 服务的基础域名
BASE_URL = "www.laoniu63.top"

class APIClient:
    def __init__(self, email=None, password=None):
        """初始化 API 客户端"""
        self.base_url = f"https://{BASE_URL}/api/v1"
        self.token = None
        self.email = email
        self.password = password

    def make_request(self, method, endpoint, data=None, headers=None):
        """执行 HTTP 请求，并处理错误"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(method, url, data=data, headers=headers, timeout=10)
            response.raise_for_status()  # 若响应出错，抛出异常
            return response.json()
        except requests.Timeout:
            logging.error("请求超时，请检查网络连接。")
        except requests.ConnectionError:
            logging.error("无法连接服务器，请稍后重试。")
        except requests.exceptions.HTTPError as e:
            error_msg = e.response.json().get("message", "未知错误")
            logging.error(f"HTTP 错误：{error_msg}")
        except Exception as e:
            logging.error(f"未知错误：{e}")
        return None

    def register_user(self):
        """注册用户"""
        data = {"email": self.email, "password": self.password}
        result = self.make_request("POST", "/passport/auth/register", data=data)
        if result:
            logging.info("注册成功")
        else:
            logging.error("注册失败")

    def authenticate_user(self):
        """用户登录，并获取 Token"""
        data = {"email": self.email, "password": self.password}
        result = self.make_request("POST", "/passport/auth/login", data=data)
        if result:
            self.token = result["data"]["auth_data"]
            logging.info(f"登录成功，Token: {result['data']['token']}")
        else:
            logging.error("登录失败")
            self.token = None

    def get_subscription_link(self, node_id=None):
        """获取用户订阅链接"""
        endpoint = "/user/getSubscribe"
        if node_id:
            endpoint += f"?node_id={node_id}"
        headers = {"Authorization": self.token}
        result = self.make_request("GET", endpoint, headers=headers)
        if result:
            return result["data"]["subscribe_url"]
        logging.error("获取订阅链接失败，请稍后再试。")
        return None

def generate_random_email():
    """生成随机邮箱地址"""
    domains = ["gmail.com", "qq.com", "163.com", "yahoo.com", 
               "sina.com", "126.com", "outlook.com", "yeah.net", 
               "foxmail.com"]
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_random_password():
    """生成随机密码"""
    safe_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(safe_chars) for _ in range(12))

if __name__ == "__main__":
    # 初始化客户端，并生成随机账号信息
    client = APIClient()
    email = generate_random_email()
    password = generate_random_password()

    logging.info(f"生成的邮箱: {email}")
    logging.info(f"生成的密码: {password}")

    # 注册并登录
    client.email = email
    client.password = password
    client.register_user()
    client.authenticate_user()

    # 获取订阅链接
    if client.token:
        logging.info("正在获取订阅链接...")
        subscription_link = client.get_subscription_link()
        if subscription_link:
            logging.info(f"订阅链接: {subscription_link}")
        else:
            logging.error("订阅链接获取失败，请稍后再试。")
    else:
        logging.error("无法获取订阅链接，用户登录失败。")

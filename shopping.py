from page.my_order_page import MyOrderPage, url
from common.base import open_browser
import unittest
from time import sleep


class TestShopping(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """执行用例前打开浏览器,并实例化MyOrderPage"""
        driver = open_browser()
        cls.my_order_page = MyOrderPage(driver)
        # cls.suborder_succeed_page = SuborderSucceedPage(driver)
        # cls.user_center_page = UserCenterPage(driver)

    def setUp(self):
        """执行每个用例前打开登录页面"""
        self.my_order_page.get_url(url)

    @classmethod
    def tearDownClass(cls):
        """执行完所有用例后关闭浏览器"""
        TestShopping().my_order_page.quit()

    def test_shopping_01(self):
        """登录--下单"""
        self.my_order_page.input_username('jumon777')  # 输入用户名
        self.my_order_page.input_password('123456')  # 输入密码
        self.my_order_page.click_submit()  # 点击"立即登录"
        self.my_order_page.click_homepage()  # 点击"主页"
        self.my_order_page.click_computer()  # 点击"电脑"
        self.my_order_page.click_buy_computer()  # 点击联想台式机下的"立即购买"
        self.my_order_page.add_to_cart()  # 点击联想台式机页面的"立即购买",将商品加入购物车
        self.my_order_page.click_checkout()  # 点击"去结算"
        self.my_order_page.click_surface_mail()  # 点击配送方式--"邮局平邮"
        self.my_order_page.click_alipay()  # 点击支付方式--"支付宝支付"
        self.my_order_page.click_suborder()  # 点击"提交订单"
        order_num = self.my_order_page.get_ordernum_in_sos()  # 获取订单号
        self.my_order_page.click_user_center()  # 点击"用户中心"
        self.my_order_page.click_my_order()  # 点击"我的订单"
        order_num_in_myorder = self.my_order_page.get_ordernum_in_myorder()  # 获取我的订单页面中的订单号
        self.assertEqual(order_num, order_num_in_myorder, msg='用例执行失败')

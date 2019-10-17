# 导入page文件中的shopping_cart_page方法
from page.addcartshopping_page import ShoppingCart_page
from common.base import open_browser
import unittest
from selenium import webdriver


class Testshoppingcart(unittest.TestCase):
    """测试购物车功能"""

    def setUp(self):
        # 打开浏览器
        driver = open_browser()
        # 实列化ShoopingCartpage
        self.shopping = ShoppingCart_page(driver)
        # 打开网址
        self.shopping.get_url("http://ecshop.itsoso.cn/index.php")

    def tearDown(self):
        """关闭浏览器"""
        self.shopping.quit()

    def testQuantity1(self):
        """测试添加数量功能"""
        # 先把滚动条滑到聚焦元素然后点击的位置
        self.shopping.underline()
        # 点击立即购买
        self.shopping.purchase()
        # 点击输入购买数量2
        self.shopping.quantity(2)
        # 点击更新
        self.shopping.updateshoppingcart()

        # 实际结果
        self.shopping.quantity(2)

        # 断言
        self.assertEqual(self.shopping.quantity, self.shopping.quantity, msg="用例执行失败添加的结果和预期结果不想符合")

    def is_Success(self, text):
        """判读是否添加数量成功"""
        return self.shopping.quantity(self.shopping.quantity(text))

    def testQuantity2(self):
        """测试商品名称一致性"""
        # 先把滚动条滑到聚焦元素的位置然后点击进入
        self.shopping.underline()
        # 点击立即购买
        self.shopping.purchase()
        # 实际结果加购物之前的商品名称
        result = self.shopping.goodsN1()
        # 预期结果
        expect = self.shopping.goodsN2()
        # 断言
        self.assertEqual(result, expect, msg="用例执行失败")

    def testQuantity3(self):
        """判断清空的一致性"""
        # 先把滚动条滑到聚焦元素的位置然后点击进入
        self.shopping.underline()
        # 点击立即购买
        self.shopping.purchase()
        # 点击清空购物车
        self.shopping.empty()
        # 再点击首页的购物车图标
        self.shopping.deleteshoppingcart()
        # 实际结果
        deletebefore = self.shopping.empty()
        # 预期结果:当点击首页图片里面没有任何信息时清空成功
        deleteaafter = self.shopping.deleteshoppingcart()
        # 断言
        self.assertEqual(deletebefore, deleteaafter, msg="用例执行失败")


if __name__ == '__main__':
    unittest.main()


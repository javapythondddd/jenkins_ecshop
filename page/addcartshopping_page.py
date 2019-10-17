"""
   #打开浏览器
    #输入网址
    #点击首页商品页面
    #点击商品
    #点击所选的商品
    #点击立即购买
    #判断是否和加购的商品相同
    #购物车商品的增删改查
"""
"""
做定位器
操作
"""
from common.base import open_browser
from common.base import Base
import time
#导入一个定位器方法
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser="Chrome"
class ShoppingCart_page(Base):
    """
    对购物车页面进行定位
    """
    abroad_loc=("class name","img-box")#定位家用电器无人机套装
    # number_loc=("css selector","#number")#定位购买数量
    purchase_loc=("css selector","a[href='javascript:addToCart(79)']>img")#定位立即购买
    Continueshopping_loc=("link text","themes/default/images/continue.gif")#定位继续购买按钮
    empty_loc=("css selector","input[type='button']")#定位清空删除购物车商品功能
    delete_loc=("class name","f6")#定位删除单个购物车商品
    purchaseQuantity_loc=("css selector","td[align='right']>input")#定义结算页面的购买数量输入框
    toupdate=("name","submit")#定位更新购物车输入框
    goodsname=("class name","goods_style_name")#加购之前的商品名称
    goodsname2=("class name","f6")#加购后的商品名称
    homeShoppingCart=("css selector","a[title='查看购物车']")



    def underline(self):
        """
        滚动条下划到指定元素位置
        点击进入商品详情页
        :return:
        """
        self.focus_element(self.abroad_loc)
        self.click(self.abroad_loc)

    def goodsN1(self):
        """
        点击立即购买之前的商品名称
        :return:
        """
        return self._Base__find_element(self.goodsname).text

    # def add_number(self,text):
    #     """
    #     输入购买数量
    #     :return:
    #     """
    #     element=self.number_loc
    #     self.send_keys(element,text)

    def purchase(self):
        """
        点击购买
        :return:
        """
        self.click(self.purchase_loc)
    def goodsN2(self):
        """
        点击立即购买后
        商品结算页的商品
        名称
        :return:
        """
        return self._Base__find_element(self.goodsname2).text




    def quantity(self,text):
        """
        输入结算页面的购买数量
        :return:
        """
        self.send_keys(self.purchaseQuantity_loc,text)



    def updateshoppingcart(self):
        """
        点击更新购物车
        :return:
        """
        self.click(self.toupdate)

    def empty(self):
        """
        点击清空购物车
        :return:
        """
        self.click(self.empty_loc)
    def deleteshoppingcart(self):
        """
        点击首页的购物车
        查看清空
        :return:
        """
        self.click(self.homeShoppingCart)


    def close(self):
        """关闭浏览器"""
        self.quit()

if __name__ == '__main__':
    driver=open_browser()
    #打开浏览器
    shopping=ShoppingCart_page(driver)
    #打开网址
    shopping.get_url("http://ecshop.itsoso.cn/index.php")

    shopping.underline()
    time.sleep(3)
    shopping.goodsN1()
    time.sleep(3)
    # shopping.add_number(2)
    shopping.purchase()
    time.sleep(3)
    shopping.goodsN2()
    time.sleep(3)
    shopping.quantity(3)
    time.sleep(3)
    shopping.updateshoppingcart()
    time.sleep(5)
    shopping.empty()
    time.sleep(3)
    shopping.deleteshoppingcart()
    time.sleep(3)
    shopping.quit()















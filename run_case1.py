import unittest
import HTMLTestRunnerPlugins
import time
#确定测试文件路径
test_dir="./script"
#将测试用例添加到测试套件中
discover=unittest.defaultTestLoader.discover(test_dir)
# 3.指定测试报告存放位置
report_dir = "./report"
# 4.命名测试报告名称
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_filename = report_dir + "/"+now+"report.html"  # 测试报告路径+名称
with open(report_filename,"wb") as fp:
    # 5.使用第三方插件执行并生成测试报告
    runner = HTMLTestRunnerPlugins.HTMLTestRunner(
        title="ECShop自动化测试报告",
        description="登录注册页面自动化",
        stream=fp
    )
    # 4.执行测试套件中的测试用例
    runner.run(discover)

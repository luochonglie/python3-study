import unittest
from tests.leetcode import test_three_sum

if __name__ == '__main__':
	suite = unittest.makeSuite(test_three_sum.TestSolution, 'test')
	runner = unittest.TextTestRunner()
	runner.run(suite)  # 执行测试用例

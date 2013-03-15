#!/usr/bin/env python
# vim: set fileencoding=utf-8
db = []
def getUserInput():
	input = raw_input('请按序输入以下信息，编号、持有股票、购买价格、当前价位：\n')
	items = input.strip().split(' ')
	data = [i for i in items]
	db.append(data)

def displayData():
    print '\n\n编号\t持有股票\t购买价格\t当前价位'
    for i in db:
        for data in i:
            print '%s\t' % data,
        print

# TODO
def showSortMenus():
    pass

def showMenus():
	prompt = '''\n请选择以下功能：
(1)输入数据；
(2)显示所有数据；
(3)数据排序；
(4)退出。请输入：'''
	while True:
		while True:
			try:
				input = raw_input(prompt)
			except (EOFError, KeyBoardInterrupt):
				input = '4'
			print '\n您选择了[%s]' % input,
			if input and (input in '1234'):
				break
			else:
				print '请选择正确的序号！'

		if '4' == input:
			break
		elif '1' == input:
			getUserInput()
		elif '2' == input:
			displayData()
		else:
			showSortMenus()

if __name__ == '__main__':
	showMenus()

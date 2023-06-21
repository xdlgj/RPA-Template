# -*- encoding: utf-8 -*-
'''
@File    :   cwlog.py
@Time    :   2022/05/23 17:49:15
@Author  :   zws 
@Version :   1.0
@Contact :   zhuws@huayunsoft.com

usage: 
	1、use execute python script in CMIPAStudio and set searching path to "./" or "directory"
	2、import cwlog
	3、set global variable like this : logger = cwlog.Logger(os.path.join(output_directory,'log.txt'))
	4、do logging like this : logger.info('flow started')
	5、check your log file : ${output_directory}/log.txt
'''
import logging
import logging.handlers
class Logger():
    	
	def __init__(self,fileName):
		"""
		日志处理
		"""
		self.fileName = fileName
		fmt = '[%(asctime)s] - [%(levelname)s] - %(message)s'
		logging.basicConfig(level=logging.DEBUG, format=fmt)

		filehandler = logging.handlers.TimedRotatingFileHandler(fileName, when="D", interval=1, backupCount=0, encoding=None, delay=False, utc=False)
		filehandler.suffix = "%Y%m%d.log"
		filehandler.setFormatter(logging.Formatter(fmt))
		logging.getLogger('').addHandler(filehandler)

		self.logger = logging.getLogger()
		self.logger.debug("log initialize finish")
		self.logger.setLevel(logging.DEBUG)
	
	def format(self, msg):
		return "%s" % (msg)
	
	def info(self, msg):
		self.logger.info(format(msg))
		
	def debug(self, msg):
		self.logger.debug(format(msg))
		
	def critical(self, msg):
		self.logger.critical(format(msg))
	
	def error(self, msg):
		self.logger.error(format(msg))
		
	def warning(self, msg):
		self.logger.warning(format(msg))


import configparser

def get_config():

	config = configparser.ConfigParser()
	config.read('config/mysql.ini')
	config_data = dict()
	config_data['user'] = config['mysql']['user']
	config_data['password'] = config['mysql']['password']
	config_data['host'] = config['mysql']['host']
	config_data['database'] = config['mysql']['database']
	return config_data
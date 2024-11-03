config:
	cp ../var/config.py config.py

clean:
	rm config.py

install_requirements:
	pip3 install -r requirements.txt

uninstall_requirements:
	pip3 uninstall -r requirements.txt

freeze:
	pip3 freeze > requirements.txt


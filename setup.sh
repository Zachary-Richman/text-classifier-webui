if [ ! python3 ]; then
	echo "ERROR: Python3 is not installed"
   	exit 1
else
	echo "Python3 Installed."
	git clone https://www.github.com/Zachary-Richman/text-classifier-webui
	cd text-classifier-webui
	python3 -m venv .venv
	source ./.venv/bin/activate
	pip install -r requirements.txt
	pip list
	echo "done."

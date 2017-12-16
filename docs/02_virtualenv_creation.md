```
	MacBook-Pro-2:~ admin$ virtualenv venv2 --python=`which python2`
	Running virtualenv with interpreter /usr/local/bin/python2
	New python executable in /Users/admin/venv2/bin/python
	Installing setuptools, pip, wheel...done.
	MacBook-Pro-2:~ admin$ 
	MacBook-Pro-2:~ admin$ ls venv2/bin/
	activate		easy_install		pip2.7			python2.7
	activate.csh		easy_install-2.7	python			wheel
	activate.fish		pip			python-config
	activate_this.py	pip2			python2
	MacBook-Pro-2:~ admin$ 
	MacBook-Pro-2:~ admin$ 
	MacBook-Pro-2:~ admin$ virtualenv venv3 --python=`which python3`
	Running virtualenv with interpreter /usr/local/bin/python3
	Using base prefix '/Library/Frameworks/Python.framework/Versions/3.6'
	New python executable in /Users/admin/venv3/bin/python3
	Also creating executable in /Users/admin/venv3/bin/python
	Installing setuptools, pip, wheel...done.
	MacBook-Pro-2:~ admin$ 
	MacBook-Pro-2:~ admin$ ls venv3/bin/
	activate		easy_install		pip3.6			python3.6
	activate.csh		easy_install-3.6	python			wheel
	activate.fish		pip			python-config
	activate_this.py	pip3			python3
	MacBook-Pro-2:~ admin$ 
	MacBook-Pro-2:~ admin$ which python2
	/usr/local/bin/python2
	MacBook-Pro-2:~ admin$ 
	MacBook-Pro-2:~ admin$ which python3
	/usr/local/bin/python3
	MacBook-Pro-2:~ admin$ 
```
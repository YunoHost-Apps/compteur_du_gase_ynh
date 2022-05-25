command = '/opt/__APP__/venv/bin/gunicorn'
pythonpath = '/opt/__APP__'
workers = 4
user = '__APP__'
bind = 'unix:/opt/__APP__/sock'
pid = '/run/gunicorn/__APP__-pid'
errorlog = '/var/log/__APP__/error.log'
accesslog = '/var/log/__APP__/access.log'
access_log_format = '%({X-Real-IP}i)s %({X-Forwarded-For}i)s %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
loglevel = 'warning'
capture_output = True

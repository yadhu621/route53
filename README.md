# How to run 
```
route53> ./venv/Scripts/activate
(venv) route53> pip install -r requirements.txt

(venv) route53> cd .\app\  
(venv) app> $env:AWS_ACCESS_KEY_ID='AKIA4******PM2'
(venv) app> $env:AWS_SECRET_ACCESS_KEY='DE8L**************************+/qL8V'
(venv) app> $env:HOSTED_ZONE_ID='ABCDEFGHIJK'

(venv) app> python .\main.py
(venv) app> python .\main.py
2022-09-06 10:30:41,725 INFO route53 : Inside __init__ of Route53 class
2022-09-06 10:30:41,726 INFO route53 : Adding CNAME record on AWS Route53
2022-09-06 10:30:41,727 INFO route53 : CNAME record mapping: app.italia.it --> vip-prod.cloud.com"
2022-09-06 10:30:42,640 INFO route53 : Successfully added CNAME record on AWS Route53
```

def my_cron_job():
    print("Hello")
    f=open('/home/abhinav/test.txt','w')
    f.write("print using crontab again")
    f.close()
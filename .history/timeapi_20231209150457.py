import datetime,time

class AppTime:
    def stime(self):
        ctime = time.strftime("%T",time.localtime(time.time()))
        return ctime
    
    def sdate(self):
        cdate = time.strftime("%d-%b-%Y",time.localtime(time.time()))
        return cdate
    
    def shour(self):
        chour = time.strftime("%H",time.localtime(time.time()))
        return chour

    def sshift(self):
        now = self.shour()
        if now in self.shift_A:
            cshift = "A"
            return cshift
        elif now in self.shift_B:
            cshift = "B"
            return cshift
        elif now in self.shift_C:
            cshift = "C"
            return cshift
        
    def timeframe(self,unixtimes,out):
        ctime = datetime.datetime.fromtimestamp(int(round(unixtimes)))
        stime = ctime.replace(minute=0, second=0).timestamp()
        etime = stime + 3600
        ptime = stime - 3600

        if out =='s':
            return stime
        elif out == 'e':
            return etime
        
    def cTimeFrame(self):
        unixtimes = time.time()
        ctime = datetime.datetime.fromtimestamp(int(round(unixtimes)))
        stime = ctime.replace(minute=0, second=0).timestamp()
        etime = stime + 3600
        ptime = stime - 3600
        return [round(stime),round(etime),round(ctime.timestamp())]

        
    def unixnow(self):
        unix = round(time.time())
        return unix      
       
    
    def __init__(self):
        self.shift_C = ['23','00','01','02','03','04','05','06']
        self.shift_A = ['07','08','09','10','11','12','13','14']
        self.shift_B = ['15','16','17','18','19','20','21','22']
        

apptime = AppTime()




class OpenRWAclose:
    def __init__(self, filename, mode, pullstyle):
        self.filename=filename
        self.mode=mode
        self.pullstyle=pullstyle
    def fileAct(self):
        """open the file with the data to be read in a read-mode"""
        f=open(self.filename, self.mode);
        """Read all the lines of the file into the working storage area (buffer)"""
        dlist=f.readlines()
        
        """close the file we opened"""
        f.close()
        return dlist

class MonthRange(OpenRWAclose):
    def __init__(self, filename, mode, pullstyle, month):
        OpenRWAclose.__init__(self, filename, mode, pullstyle)
        self.month=month
    def getMonthRange(self):    
        monthEntry = {'JANUARY':[0,31], 'FEBRUARY':[32,59], 'MARCH':[60,90], 'APRIL':[91,120], 'MAY':[121,151],
         'JUNE':[152,181], 'JULY':[182,212], 'AUGUST':[213,243], 'SEPTEMBER':[244,273],
         'OCTOBER':[274,304], 'NOVEMBER':[305,334], 'DECEMBER':[335,365]}
        """
        IF EVER YOU NEED TO CONVERT LIST OF NUMBERS TO INTEGERS, TRY ONE OF THE FF
        monthEntryInt = {key: [int(x) for x in val] for key, val in monthEntry.items()}
        monthlyInteger= [int(item) for item in monthly]
        END OF INT CONVERT NOTE
        """
        mmRange=monthEntry.get(self.month)
        return mmRange
#############

def monthlydata():
    dlist=fileOp.fileAct()
    ############
    ############
    """create a list variable which is empty which you will append 
    the list of numbers from the read file
    to after you have stripped it off the line-break code
    """
    stepslist=[]
            
    """use a loop to strip the items in the list from the line-break"""
    for i in dlist:
        stepslist.append(int(i.strip('\n')))
            
    """set up the accumulator variable and set it to zero"""
    addUp = 0 
    
    """Receive the range for the month provided """
    monthly=fileOp.getMonthRange()
    """
    use loop to accumulate the steps for the month in question.
    Use the appropriate range the month as provided in the dictionary function set previously
    """
    for steps in range(monthly[0],monthly[1]):
        addUp += stepslist[steps]
        activeMonthList=[]
        activeMonthList.append(stepslist[steps])
        maxsteps=max(activeMonthList)
    
    """
    Set up the variable to get the number of days of that month so you can 
    pass it to find the average steps
    """
    if monthly[0]==0:
        monthdays=(monthly[1] - monthly[0])
    else:
        monthdays=(monthly[1] - monthly[0] +1)
    
    print(f"This is for the month of {fileOp.month} which has {monthdays} days.")
    """
    When you fix the above, create input functions to ask the user to enter in the 
    month they want the data for. or type A or all if they want all printed. 
    
    Print the results for the screen """    
    print(f'The total number of steps in {fileOp.month} is {addUp}.') 
    print(f'The average number of steps in {fileOp.month} was {float(addUp/monthdays):.2f} per day')
    print(f'The maximum number of steps in a day during the month of {fileOp.month} was {maxsteps}.') 


"""Opening, processing and closing the file as well as month for which data is to be used.""" 
fileOp = MonthRange("steps.txt", "r", "readlines", "JANUARY")
monthlydata()    
print ('\n')
"""Opening, processing and closing the file as well as month for which data is to be used.""" 
fileOp = MonthRange("steps.txt", "r", "readlines", "FEBRUARY")
monthlydata() 
print ('\n')
"""Opening, processing and closing the file as well as month for which data is to be used.""" 
fileOp = MonthRange("steps.txt", "r", "readlines", "MARCH")
monthlydata() 
print ('\n')
"""Opening, processing and closing the file as well as month for which data is to be used.""" 
fileOp = MonthRange("steps.txt", "r", "readlines", "APRIL")
monthlydata() 
print ('\n')
"""Opening, processing and closing the file as well as month for which data is to be used.""" 
fileOp = MonthRange("steps.txt", "r", "readlines", "MAY")
monthlydata() 
print ('\n')
"""Opening, processing and closing the file as well as month for which data is to be used.""" 
fileOp = MonthRange("steps.txt", "r", "readlines", "JUNE")
monthlydata() 
print ('\n')
"""Opening, processing and closing the file as well as month for which data is to be used.""" 
fileOp = MonthRange("steps.txt", "r", "readlines", "JULY")
monthlydata() 
print ('\n')
"""Opening, processing and closing the file as well as month for which data is to be used.""" 
fileOp = MonthRange("steps.txt", "r", "readlines", "AUGUST")
monthlydata() 
print ('\n')
"""Opening, processing and closing the file as well as month for which data is to be used.""" 
fileOp = MonthRange("steps.txt", "r", "readlines", "SEPTEMBER")
monthlydata() 
print ('\n')
"""Opening, processing and closing the file as well as month for which data is to be used.""" 
fileOp = MonthRange("steps.txt", "r", "readlines", "OCTOBER")
monthlydata() 
print ('\n')
"""Opening, processing and closing the file as well as month for which data is to be used.""" 
fileOp = MonthRange("steps.txt", "r", "readlines", "NOVEMBER")
monthlydata() 
print ('\n')
"""Opening, processing and closing the file as well as month for which data is to be used.""" 
fileOp = MonthRange("steps.txt", "r", "readlines", "DECEMBER")
monthlydata() 
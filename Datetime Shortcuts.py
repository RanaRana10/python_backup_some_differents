from datetime import datetime



List = f"""" 
Year in Full Form: (%Y) :{datetime.now().strftime("%Y")}
Month Name Full Form: (%B) :{datetime.now().strftime("%B")}
Month Name Short Form: (%b) :{datetime.now().strftime("%b")}

Day Name Full Form: (%A) :{datetime.now().strftime("%A")}
Day Name Short Form: (%a) :{datetime.now().strftime("%a")}

Date of Day: (%d) : {datetime.now().strftime("%d")}
Date of Month: (%m) : {datetime.now().strftime("%m")}

Day Name Short Form: ("%a-%A-%b-%B-%Y") :{datetime.now().strftime("%a-%A-%b-%B-%Y")}

Hour in 24 Hour Format: (%H) : {datetime.now().strftime('%H')}
Hour in 12 Hour Format: (%I) : {datetime.now().strftime('%I')}
AM or PM Know: (%p) : {datetime.now().strftime('%p')}
Current Minute Time: (%M) : {datetime.now().strftime('%M')}
Current Second Time: (%S) : {datetime.now().strftime('%S')}
Current Mili-Second Time: (%f) : {datetime.now().strftime('%f')}

Time in 24 Format: ('%H-%M-%S')    {datetime.now().strftime('%H-%M-%S')}
Time in 24 Format: ('%I-%M-%S %p')    {datetime.now().strftime('%I-%M-%S %p')}
Date Today Special: ('%Y - %m - %d')    {datetime.now().strftime('%Y - %m - %d')}


"""

print(List)



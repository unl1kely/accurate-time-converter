# years
years2months = lambda years: years*12
years2days = lambda years: years*365.24
years2hours = lambda hours: years*8765.76
years2minutes = lambda minutes: years*525945.6
years2seconds = lambda years: years*31556736
#months
months2years = lambda months: months/12
months2days = lambda months: (months*365.24)/12
months2hours = lambda months: months*730.48
months2minutes = lambda months: months*43828.8
months2seconds = lambda months: months*2629728
#days
days2years = lambda days: days/365.24
days2months = lambda days: (days*12)/365.24
days2hours = lambda days: days*24
days2minutes = lambda days: days*1440
days2seconds = lambda days: days*86400
#hours
hours2years = lambda hours: hours/8765.76
hours2months = lambda hours: hours/730.48
hours2days = lambda hours: hours/24
hours2minutes = lambda hours: hours*60
hours2seconds = lambda hours: hours*3600
#minutes
minutes2years = lambda minutes: minutes/525945.6
minutes2months = lambda minutes: minutes/43828.8
minutes2days = lambda minutes: minutes/1440
minutes2hours = lambda minutes: minutes/60
minutes2seconds = lambda minutes: minutes*60
#seconds
seconds2years = lambda seconds: seconds/31556736
seconds2months = lambda seconds: seconds/2629728
seconds2days = lambda seconds: seconds/86400
seconds2hours = lambda seconds: seconds/3600
seconds2minutes = lambda seconds: seconds/60
# usage example
# myvar = years2seconds(78)

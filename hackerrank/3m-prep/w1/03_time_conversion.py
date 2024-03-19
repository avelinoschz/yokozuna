# https://www.hackerrank.com/challenges/three-month-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
# Example

# s = '12:01:00PM'
# Return '12:01:00'.

# s = '12:01:00AM'
# Return '00:01:00'.

def timeConversion(s):
    meridian = s[-2:]
    split_time = s.split(':')

    if meridian == 'AM':
        if s[:2] == '12':
            split_time[0] = '00'
    else:
    	if s[:2] != '12':
	    	hours_str = split_time[0]
	    	hours_int = int(hours_str)
	    	militar_hours = hours_int + 12
	    	split_time[0] = str(militar_hours)
    
    return ':'.join(split_time)[:-2]


s = '12:01:00PM'
result = timeConversion(s)
print(result)
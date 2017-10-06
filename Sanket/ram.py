import os
import argparse

parser = argparse.ArgumentParser(description='RAM related metrics')
parser.add_argument('value',help="pass argument to show related information",type=str)
args = parser.parse_args()

if args.value=='ram':    #statistics of ram
	tot_m, used_m, free_m, s,b,c = map(int, os.popen('free -t -m').readlines()[1].split()[1:])
	print ''
	print 'total ram memory: ',tot_m, 'MB'
	print 'used ram memory: ',used_m, 'MB'
	print 'free ram memory: ',free_m, 'MB'
	print ''
	
if args.value=='swap':    #statistics of swap memory
	tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[3].split()[1:])
	print ''
	print 'total swap memory: ',tot_m, 'MB'
	print 'used swap memory: ',used_m, 'MB'
	print 'free swap memory: ',free_m, 'MB'
	print ''

if args.value=='shared':  #amount of shared memory
	s,b,c = map(int, os.popen('free -t -m').readlines()[1].split()[4:7])
	print ''
	print 'shared memory: ',s,' MB'
	print ''
	
if args.value=='buffers':  #amount of memory used as buffer
	s,b,c = map(int, os.popen('free -t -m').readlines()[1].split()[4:7])	
	print ''
	print 'memory used as buffer: ',b,' MB'
	print ''
	
if args.value=='cached':   #amount of memory used as cache
	s,b,c = map(int, os.popen('free -t -m').readlines()[1].split()[4:7])	
	print ''
	print 'memory used as cache: ',c,' MB'
	print ''
	
if args.value=='waitingproc':     #number of runnable processes (waiting for run time)
	r,b = map(int, os.popen('vmstat').readlines()[2].split()[0:2])
	print ''
	print 'Number of processes wiating for runtime: ',r
	print ''
	
if args.value=='siso':      #memory swapped in from/to disk
	si,so = map(int, os.popen('vmstat').readlines()[2].split()[6:8])
	print ''
	print 'memory swapped in from disk: ',si/1024, 'MB'
	print 'memory swapped to disk: ',so/1024, 'MB'
	print ''
	
if args.value=='bibo':     #blocks received/sent from/to block device
	bi,bo = map(int, os.popen('vmstat').readlines()[2].split()[8:10])
	print ''
	print 'blocks received from block device: ',bi
	print 'block sent to block device: ',bo
	print ''
	
if args.value=='intrptpersec':     #number of interrupts per second
	in1,cs = map(int, os.popen('vmstat').readlines()[2].split()[10:12])
	print ''
	print 'number of interrupts per second ',in1
	print ''
	
if args.value=='conswitchpersec':     #number of context switches per second
	in1,cs = map(int, os.popen('vmstat').readlines()[2].split()[10:12])
	print ''
	print 'number of context switches per second ',cs
	print ''
	
if args.value=='largeproc':     #process consuming more memory
	usr,pid = map(str, os.popen('ps aux --sort -%mem').readlines()[1].split()[0:2])
	
	cpu,mem = map(float, os.popen('ps aux --sort -%mem').readlines()[1].split()[2:4])
	
	vsz,rss = map(int, os.popen('ps aux --sort -%mem').readlines()[1].split()[4:6])
	
	time,name = map(str, os.popen('ps aux --sort -%mem').readlines()[1].split()[9:11])
	
	print ''
	print 'Greatest process executing in ram: '
	print 'user: ',usr
	print 'PID: ',pid
	print 'CPU%: ',cpu, '%'
	print 'MEM%: ',mem,'%'
	print 'memory usage: ',rss/1024,' MB'
	print 'Process: ',name
	print ''
	
	
'''	

output:

shivam@shivam-desktop:~/GS$ python ram.py ram

total ram memory:  1842 MB
used ram memory:  1211 MB
free ram memory:  631 MB

shivam@shivam-desktop:~/GS$ python ram.py swap

total swap memory:  7811 MB
used swap memory:  276 MB
free swap memory:  7535 MB

shivam@shivam-desktop:~/GS$ python ram.py shared

shared memory:  139  MB

shivam@shivam-desktop:~/GS$ python ram.py buffers

memory used as buffer:  47  MB

shivam@shivam-desktop:~/GS$ python ram.py cached

memory used as cache:  297  MB

shivam@shivam-desktop:~/GS$ python ram.py waitingproc

Number of processes wiating for runtime:  1

shivam@shivam-desktop:~/GS$ python ram.py siso

memory swapped in from disk:  0 MB
memory swapped to disk:  0 MB

shivam@shivam-desktop:~/GS$ python ram.py waitingproc

Number of processes wiating for runtime:  1

shivam@shivam-desktop:~/GS$ python ram.py waitingproc

Number of processes wiating for runtime:  5

shivam@shivam-desktop:~/GS$ python ram.py siso

memory swapped in from disk:  0 MB
memory swapped to disk:  0 MB

shivam@shivam-desktop:~/GS$ python ram.py bibo

blocks received from block device:  55
block sent to block device:  43

shivam@shivam-desktop:~/GS$ python ram.py intrptpersec

number of interrupts per second  179

shivam@shivam-desktop:~/GS$ python ram.py conswitchpersec

number of context switches per second  737

shivam@shivam-desktop:~/GS$ python ram.py largeproc

Greatest process executing in ram: 
user:  shivam
PID:  4973
CPU%:  115.0 %
MEM%:  31.9 %
memory usage:  589  MB
Process:  /home/shivam/jdk1.8.0_101/bin/java

shivam@shivam-desktop:~/GS$ python ram.py ram

total ram memory:  1842 MB
used ram memory:  1686 MB
free ram memory:  156 MB

shivam@shivam-desktop:~/GS$ python ram.py swap

total swap memory:  7811 MB
used swap memory:  374 MB
free swap memory:  7437 MB

shivam@shivam-desktop:~/GS$ python ram.py largeproc

Greatest process executing in ram: 
user:  shivam
PID:  2283
CPU%:  25.8 %
MEM%:  26.1 %
memory usage:  482  MB
Process:  /usr/lib/firefox/firefox

shivam@shivam-desktop:~/GS$ 

'''

Load Testing
============

Load testing is the process of putting demand on a software system or 
computing device and measuring its response. 

In this suite, we make use of JMeter.

How to use
----------

```
    $ jmeter
```

and click File > Open > select "loadtesting.jmx". 

Installation on Mac
-------------------

1. JMeter

    First of all, you need to install Java runtime, also known as JRE. 
    In case of Mac, check this [link](https://support.apple.com/kb/DL1572?locale=en_US) to install a proper JRE. 
    The easiest way to install JMeter is using Homebrew as follows:

    ```
    brew install jmeter --with-plugins
    ```

Test cases
----------

In JMeter, we can make use of postprocessing. 

**post analysis**

Endpoints may work well for the small group of users, for example, up 
to 50. However, it may not be able to support 10,000 users at the same 
time, and may be some of them do not recieve any data at all, or get 
some of data not whole.

Here this suite extracts JSON data from responses for a post analysis, 
and checks contents whether or not its contents have valid format. 

** parameter **

The suite imports csv files to specify target parameters without fixing 
JMeter script. In this script, it is used to specify catch id and page 
id. 

- catches_ids.csv : the list of target catch ids
- catches_pageids.csv : the list of target catch page ids

Limitation
----------

1. For each Thread Group, I only assigned 10, 1, and 10 for the number 
of threads, ramp-up period, and a loop count due to the hardware 
limitation.

2. This suite aims to test `catches` API only, and do not check 
parameters depending on its verbosity. However, other cases should be 
covered in load testing scenario also.


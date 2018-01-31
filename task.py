from bs4 import BeautifulSoup
from selenium import webdriver
import re

"""The driver.get method will navigate to a page given by the URL.
WebDriver will wait until the page has fully loaded (that is, the “onload”
event has fired) before returning control to your test or script. It’s worth
noting that if your page uses a lot of AJAX on load then WebDriver may not know when
it has completely loaded.:"""

"""XPath is the language used for locating nodes in an XML document"""


# ***************************************

def get_avg(elements):
    """gives the average value of ace% per player using selenium"""

    driver.get(url)
    driver.refresh()
    print(driver)

    # finding element using "find_element_by_xpath"
    # elements1 = driver.find_element_by_xpath("""//*[@id="matches"]/tbody""")
    elements = driver.find_element_by_xpath("""//*[@id="splitsbody"]""")
    result = re.split(r"Grass|Clay|Hard|Cemented", elements.text)
    # result = re.split(r"Grass|Clay|Hard|Cemented",elements1.text)

    # for saving values
    ace = []
    spw = []
    rpw = []
    element_APercent = []

    for i, data in enumerate(result):  # rolling over all the results as it's in form of a list
        # y = re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*", data)
        # nested_elements.append(y)
        # print i
        x = re.findall(r"\d+\.\d+", result[i][:])
        # print x
        if not x:
            print("No__****__Value")

        else:
            element_APercent.append((x[0], x[5], x[7]))

    # coverting into list of value for specific requirements
    for i, data in enumerate(element_APercent):
        ace.append(data[0])
        spw.append(data[1])
        rpw.append(data[2])

    # taking values from the list of floats
    # converting unicode to int
    int_ace = [float(i) for i in ace]
    int_spw = [float(i) for i in spw]
    int_rpw = [float(i) for i in rpw]

    if len(element_APercent) == 0:
        # avg = "zero values"
        avg_ace, avg_spw, avg_rpw = 0, 0, 0
        return avg_ace, avg_spw, avg_rpw
    else:
        avg_ace = sum(int_ace) / (len(int_ace))
        avg_spw = sum(int_spw) / (len(int_spw))
        avg_rpw = sum(int_rpw) / (len(int_rpw))

        print({"Ace_percent": avg_ace, "spw ": avg_spw, "rpw ": avg_rpw})
        return avg_ace, avg_spw, avg_rpw

path = r"/home/srishti/Downloads/chromedriver"

"""WebDriver is a tool for automating web application
testing, and in particular to verify that they work as expected"""
driver = webdriver.Chrome(path)
url = 'http://www.tennisabstract.com/cgi-bin/player.cgi?p=KeiNishikori&f=&view=singles'
print(url)
x,y,z = get_avg(url)
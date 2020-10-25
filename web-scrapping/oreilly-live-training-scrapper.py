"""Example of python scrapper for O'Reilly live-training schedule page"""

import requests
from bs4 import BeautifulSoup as bs
from bs4 import element as bs_element
import json
from datetime import datetime

base_url = 'https://learning.oreilly.com/live-training/'

def extract_course_time(dom):
    start_datetime = [datetime.fromisoformat(date['datetime']).astimezone()
                      for date 
                      in dom.find_all(itemprop = 'startDate')]    
    end_datetime = datetime.fromisoformat(dom.find(itemprop = 'endDate')['content']).astimezone()
    
    # in case of multi-day course, course time is calculated base in last day info. Assume that course lenght is constant every day
    course_dates = [d.strftime("%y/%m/%d") for d in start_datetime]
    course_length = end_datetime - start_datetime[-1]
    course_time = [f"{t.strftime('%H:%M')}-{(t+course_length).strftime('%H:%M')}" for t in start_datetime]
    
    #remove duplicates
    course_time = list(dict.fromkeys(course_time))
    
    return (course_dates, course_time, str(course_length))


def extract_free_places(dom):
    places = dom.find(class_ = 'course-spots').get_text().strip()
    if places == 'Registration closed':
        return 'closed'
    elif places == 'Wait list started':
        return 'wait'
    else:
        return int([c for c in places.split() if c.isdigit()][0])


def extract_authors(dom):
    presenters = dom.find(class_ = 'presenters')
    return [name.get_text() for name in presenters.find_all(itemprop = 'name')]


def extract_course_info(course_dom):
    result = {}    
    
    result['course_dates'], result['time'], result['length'] = extract_course_time(course_dom)

    # extract title and url
    title_tag = course_dom.find(class_ = 'title')
    result['title'] = title_tag.a.get_text().strip()
    result['url'] = f"https://learning.oreilly.com{title_tag.a['href']}"    
    result['places'] = extract_free_places(course_dom)
    
    # extract course id
    result['course_id'] = course_dom['data-course-id']    
    result['authors'] = extract_authors(course_dom)
    
    return result


response = requests.get(base_url)
dom = bs(response.text)
course_list = dom.find(class_="course-list")
courses = course_list.find_all('article')
print(f"{len(courses)} courses")

[extract_course_info(c) for c in courses]

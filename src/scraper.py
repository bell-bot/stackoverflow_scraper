import csv
import logging
import re
import time

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG)

BASE_URL = "https://stackoverflow.com"
SEARCH_RESULTS_URL = "https://stackoverflow.com/questions/tagged/python?page="
QUESTION_URL_PATTERN = re.compile('<a href="(/questions/[0-9]+/[0-9a-zA-Z-]+)" class="s-link">')


def get_page_url(page):
    return f"{SEARCH_RESULTS_URL}{page}"


def get_questions_on_page(page_url):

    search_results = requests.get(page_url)
    if search_results.status_code == 200:
        links = re.findall(QUESTION_URL_PATTERN, search_results.text)

        return [BASE_URL + link for link in links]

    logging.info(f"Request failed with code: {search_results.status_code}")


def parse_question(url, _writer, max_retries=3):
    for i in range(max_retries):
        try:
            html_content = get_html_content(url)
            if not html_content:
                logging.info("Page not reachable")
                return

            soup = BeautifulSoup(html_content, 'html.parser')
            question_id = get_question_id(soup)
            question_header = get_question_header(soup)
            question_content = get_question_content(soup)
            question_answers = get_question_answers(soup)

            if question_answers:
                write_question_to_csv_file(_writer, question_id, question_header, question_content, question_answers)
            return
        except TypeError:
            logging.info(f"Attempt {i+1}: Parsing Error")
            time.sleep(20)


def get_html_content(url, max_retries=3):
    for i in range(max_retries):
        try:
            return requests.get(url).text
        except ConnectionError:
            logging.info(f"Attempt {i + 1}: Unable to retrieve question.")
            time.sleep(20)


def write_question_to_csv_file(writer, question_id, question_header, question_content, question_answers):
    for answer in question_answers:
        writer.writerow([question_id, question_header, question_content] + [answer])


def get_question_id(soup):
    return soup.find(id="question")['data-questionid']


def get_question_header(soup):
    try:
        header = soup.find(id="question-header").h1.text
        logging.info(f"Found header: {header}")
        return header
    except AttributeError:
        logging.info("No header found.")


def get_question_content(soup):
    try:
        content = soup.find(id="question").find(attrs={"class": "s-prose js-post-body", "itemprop": "text"}).text
        logging.info(f"Found question: {content}")
        return content
    except AttributeError:
        logging.info("No content found.")


def get_question_answers(soup):
    try:
        answers = soup.find(id="answers").find_all("div", id=re.compile('answer-[0-9]+'))
        return parse_answers(answers)
    except AttributeError:
        logging.info("No questions found.")


def parse_answers(answers):
    for answer in answers:
        answer_id = answer['data-answerid']
        answer_content = answer.find("div", attrs={"class": "s-prose js-post-body"}).text
        answer_rating = answer['data-score']
        logging.info(f"Found answer {answer_id} with rating {answer_rating}: {answer_content}")
        return [answer_id, answer_rating, answer_content]


def scrape(writer):
    current_page = 1
    while True:
        page_url = get_page_url(current_page)
        logging.info(f"Retrieved page {current_page}.")
        current_page += 1
        try:
            questions = get_questions_on_page(page_url)
            logging.info(f"Found {len(questions)} questions.")
            for question in questions:
                parse_question(question, writer)
        except ConnectionError:
            break
        time.sleep(5)


def init_csv_writer():
    file = open("stackoverflow_common_python_questions.csv", "w")
    _writer = csv.writer(file)
    cols = ["question_id", "question_header", "question_content", "answer_id", "answer_rating", "answer_content"]
    _writer.writerow(cols)
    return _writer


if __name__ == "__main__":
    writer = init_csv_writer()
    scrape(writer)

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

all_jobs = []
keywords = ['flutter', 'python', 'goaling']

def scrape_page(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    job_titles = soup.find_all("a", class_="preventLink")
    company_names = soup.find_all("span", class_="companyLink")

    for job, company in zip(job_titles, company_names):
        job_title_element = job.find("h2")
        url = job["href"]

        if job_title_element is None:
            continue

        job_title = job_title_element.text.strip()
        company_name = company.text.strip()

        if not job_title or not company_name:
            continue

        job_data = {"title": job_title, "company": company_name, "link": f"https://remoteok.com{url}"}
        all_jobs.append(job_data)

for i in keywords:
    url = f"https://remoteok.com/remote-{i}-jobs"
    scrape_page(url)

print(all_jobs)

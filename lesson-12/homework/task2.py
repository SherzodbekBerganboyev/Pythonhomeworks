
import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd

# Ma'lumotlar bazasi
conn = sqlite3.connect("jobs.db")
c = conn.cursor()

# Jadval yaratish
c.execute("""CREATE TABLE IF NOT EXISTS jobs (
    job_title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    apply_link TEXT,
    PRIMARY KEY (job_title, company, location)
)""")

# Saytdan ma'lumotlarni olish
url = "https://realpython.github.io/fake-jobs"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    desc = job.find("div", class_="content").text.strip()
    link = job.find("a")["href"]

    c.execute("SELECT * FROM jobs WHERE job_title=? AND company=? AND location=?", (title, company, location))
    existing = c.fetchone()

    if existing:
        if existing[3] != desc or existing[4] != link:
            c.execute("""UPDATE jobs SET description=?, apply_link=?
                         WHERE job_title=? AND company=? AND location=?""",
                      (desc, link, title, company, location))
    else:
        c.execute("INSERT INTO jobs VALUES (?, ?, ?, ?, ?)", (title, company, location, desc, link))

conn.commit()
conn.close()

def export_filtered_jobs(filter_by="location", value="Remote"):
    conn = sqlite3.connect("jobs.db")
    query = f"SELECT * FROM jobs WHERE {filter_by} = ?"
    df = pd.read_sql_query(query, conn, params=(value,))
    df.to_csv(f"filtered_jobs_by_{filter_by}_{value}.csv", index=False)
    conn.close()

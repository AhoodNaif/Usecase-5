# Job Market Dataset Analysis

## Overview

This project analyzes a job market dataset containing various job postings, with a focus on factors such as job titles, salaries, experience requirements, and gender preferences. The analysis helps identify key trends in the job market, such as opportunities for fresh graduates, salary distributions, and region-specific job availability.

### Dataset Description

The dataset includes the following columns:

- **job_title**: Title of the job position.
- **job_date**: Date when the job was posted.
- **comp_name**: Name of the company offering the job.
- **comp_type**: Type of the company (e.g., private, public).
- **comp_size**: Company size (e.g., small, medium, large).
- **eco_activity**: The economic activity or sector of the job.
- **qualif**: Qualifications required for the job.
- **region**: The region where the job is offered.
- **city**: The city where the job is located.
- **salary**: Salary offered for the job.
- **contract**: Type of employment contract (e.g., full-time, part-time).
- **positions**: Number of positions available for the job.
- **job_post_id**: Unique identifier for each job posting.
- **exper**: Number of years of experience required.
- **gender**: Gender preference for the job (M, F, or both).

## Project Goals

- Analyze the distribution of job postings by experience level, gender preference, and region.
- Identify the most common job titles and their corresponding salaries.
- Understand the opportunities for fresh graduates in the job market.
- Visualize key trends in the job market using interactive charts.

## Setup and Installation

### Prerequisites

Ensure you have the following libraries installed:

```bash
pip install pandas numpy plotly streamlit
```

## Analysis Insights
Experience Requirements: The majority of job postings (698 out of 1168) do not require prior experience, indicating a strong market for fresh graduates.

Gender Distribution: A large proportion of job postings (37.5%) are open to both genders, demonstrating inclusivity in the job market.

Salary Analysis: The average salary for a "Big Data Specialist" is 7500 SAR, which is higher than the overall average salary of 4792 SAR.

Regional Job Postings: Most job postings are concentrated in Riyadh, followed by Makkah and the Eastern Province, offering the most opportunities.

## License
This project is open-source and available under the MIT License.

## Streamlit link app
[click here](https://usecase-5-4tzjxdidx584kjejynoohy.streamlit.app/)

# Cusat exam scraper

Scrape [exam.cusat.ac.in](https://exam.cusat.ac.in).

First run `examtypes.py` to get the exam combinations, then run the `scraper.py` to scrape data for each of exam.


## Data format

```js
{
  "name": "FAKE NAME",
  "month": "April",
  "sem": "8",
  "exam": "Regular",
  "year": "2018",
  "reg_no": 00000000,
  "results": [
    {
      "code": "CS 1801",
      "subject": "ADVANCED ARCHITECTURE AND PARALLEL PROCESSING",
      "marks": "89",
      "grade": "D",
      "passed": true
    },
    {
      "code": "CS 1802",
      "subject": "OBJECT ORIENTED MODELING AND DESIGN",
      "marks": "115",
      "grade": "B",
      "passed": true
    },
    {
      "code": "CS 1803",
      "subject": "DISTRIBUTED COMPUTING",
      "marks": "96",
      "grade": "C",
      "passed": true
    },
    {
      "code": "CS 1804 E2",
      "subject": "DATA MINING",
      "marks": "112",
      "grade": "B",
      "passed": true
    },
    {
      "code": "CS 18L1",
      "subject": "PROJECT",
      "marks": "290",
      "grade": "S",
      "passed": true
    },
    {
      "code": "CS 18L2",
      "subject": "VIVA-VOCE",
      "marks": "82",
      "grade": "A",
      "passed": true
    }
  ],
  "total": 784,
  "gpa": 8.41,
  "cgpa": 7.86,
  "classification": "First Class"
}
```

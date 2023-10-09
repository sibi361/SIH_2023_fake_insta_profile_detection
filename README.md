# SIH_2023_fake_insta_profile_detection

PS1364 Fake Social Media Profile detection and reporting

## Flowchart

![flowchart](/images/flowchart.png)

## Dataset

`fusers.csv`: fake users

`users.csv`: real users

## Usage

```uvicorn run api:app --reload```

Frontend will be available at `http://127.0.0.1:8000/`

API will be available at `http://127.0.0.1:8000/api/v1/predict`

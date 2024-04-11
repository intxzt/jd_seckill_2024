FROM python:3.9
ADD . /jd_seckill_2024
WORKDIR /jd_seckill_2024
RUN pip install -r requirements.txt
CMD ["python", "main.py"]

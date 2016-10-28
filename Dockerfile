FROM python:2.7.9

ADD sieve_s.py /

CMD ["python", "/sieve_s.py"]

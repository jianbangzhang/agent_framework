FROM python3.10

WORKDIR /home/workspace

COPY . /home/workspace/

RUN pip install -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/home/workspace"

CMD ["python", "app/app.py"]
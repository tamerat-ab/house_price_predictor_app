# FROM python:3.10.11
# FROM tiangolo/uvicorn-gunicorn:python3.10.11
FROM python:3.10.11
WORKDIR /H_prediction_app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8501
COPY . .
# CMD streamlit run frontend.py 
ENTRYPOINT ["streamlit", "run", "frontend.py", "--server.port=8501", "--server.address=localhost"]

# 
FROM python:3.9

# 
WORKDIR /desafio_backend_conta_digital

# 
COPY ./requirements.txt /desafio_backend_conta_digital/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /desafio_backend_conta_digital/requirements.txt

# 
COPY ./ /desafio_backend_conta_digital

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

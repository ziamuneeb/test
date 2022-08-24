FROM python:3
ARG var_1
ARG var_2
ENV v_1=$var_1
ENV v_2=$var_2
COPY . /usr/app
WORKDIR /usr/app
RUN pip install -r requirements.txt
CMD python app.py
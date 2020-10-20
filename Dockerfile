FROM python:3.9-alpine
LABEL MAINTAINER="Dan Manners (daniel.a.manners@gmail.com)"

# Change the working directory
WORKDIR /opt/nda

# Add Files
ADD * /opt/nda/
ADD db/ /opt/nda/db/
ADD routes /opt/nda/routes/
RUN pip install -U pip && pip install -r /opt/nda/req.txt

# Expose port 3000
EXPOSE 3000

# Run the Code
ENTRYPOINT [ "python","main.py" ]

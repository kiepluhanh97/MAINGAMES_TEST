# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app

COPY test_data /app/test_data
COPY test_utils /app/test_utils
COPY train_src /app/train_src
COPY . /app/
RUN apt-get update && apt-get install -y libgl1-mesa-glx
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable to avoid buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Run the command to start your Python process (replace `app.py` with your actual script name)
ENTRYPOINT cd /app && python3 test.py --model-path ./train_src/backup-tiny/custom-obj-tiny_last.weights --cfg-path ./train_src/custom-obj-tiny.cfg --images-path ./test_data/test_images/ --labels-path ./test_data/test.txt
# CMD ["python", "test.py --model-path './train_src/backup-tiny/custom-obj-tiny_last.weights' --cfg-path './train_src/custom-obj-tiny.cfg' --images-path './test_data/test_images/' --labels-path './test_data/test.txt'"]
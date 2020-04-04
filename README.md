This is a consumer intended to demonstrate basic functionality of the pipeline. It is not fault-tolerant and not suitable for production use.

If you want to modify the `consumer.py` file and test out your changes in a venice pipeline, you can run `docker build --tag YOUR_IMAGE_NAME.` in this repo, then use `image: YOUR_IMAGE_NAME` in your `docker-compose.yml` file.

If you are making many changes and you want docker-compose to build your image every time you run `docker-compose up --build`, you can use `build: PATH_TO_THIS_REPO` in your `docker-compose.yml` file.

If you want to save your image and push to an image registry, you can use `YOUR_REGISTRY_ACCOUNT/YOUR_IMAGE_NAME` to have the image tagged as `latest` by default, or `YOUR_REGISTRY_ACCOUNT/YOUR_IMAGE_NAME:YOUR_TAG` if you want to specify a tag.

Reference: https://github.com/confluentinc/confluent-kafka-python
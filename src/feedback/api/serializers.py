from rest_framework import serializers

from feedback.models import FeedbackPost

import cv2
import sys
import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

IMAGE_SIZE_MAX_BYTES = 1024 * 1024 * 2  # 2MB
MIN_TITLE_LENGTH = 1
MIN_BODY_LENGTH = 0

from feedback.utils import is_image_aspect_ratio_valid, is_image_size_valid


# class FeedbackPostSerializer(serializers.ModelSerializer):
#     username = serializers.SerializerMethodField('get_username_from_author')
#
#     class Meta:
#         model = FeedbackPost
#         fields = ['title', 'body', 'image', 'date_updated', 'username', 'slug']
#
#     def get_username_from_author(self, feedback_post):
#         username = feedback_post.author.username
#         return username


class FeedbackPostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_author')

    # image = serializers.SerializerMethodField('validate_image_url')

    class Meta:
        model = FeedbackPost
        fields = ['pk', 'title', 'slug', 'body', 'image', 'date_updated', 'username']

    def get_username_from_author(self, feedback_post):
        username = feedback_post.author.username
        return username

    # def validate_image_url(self, feedback_post):
    #     image = feedback_post.image
    #     new_url = image.url
    #     if "?" in new_url:
    #         new_url = image.url[:image.url.rfind("?")]
    #     return new_url


class FeedbackPostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackPost
        fields = ['title', 'body', 'image']

    def validate(self, feedback_post):
        try:
            title = feedback_post['title']
            if len(title) < MIN_TITLE_LENGTH:
                raise serializers.ValidationError(
                    {"response": "Enter a title longer than " + str(MIN_TITLE_LENGTH) + " characters."})

            body = feedback_post['body']
            if len(body) < MIN_BODY_LENGTH:
                raise serializers.ValidationError(
                    {"response": "Enter a body longer than " + str(MIN_BODY_LENGTH) + " characters."})

            image = feedback_post['image']
            url = os.path.join(settings.TEMP, str(image))
            storage = FileSystemStorage(location=url)

            with storage.open('', 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
                destination.close()

            # Check image size
            if not is_image_size_valid(url, IMAGE_SIZE_MAX_BYTES):
                os.remove(url)
                raise serializers.ValidationError(
                    {"response": "That image is too large. Images must be less than 2 MB. Try a different image."})

            # Check image aspect ratio
            if not is_image_aspect_ratio_valid(url):
                os.remove(url)
                raise serializers.ValidationError(
                    {"response": "Image height must not exceed image width. Try a different image."})

            os.remove(url)
        except KeyError:
            pass
        return feedback_post


class FeedbackPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackPost
        fields = ['title', 'body', 'image', 'date_updated', 'author']

    def save(self):

        try:
            image = self.validated_data['image']
            title = self.validated_data['title']
            if len(title) < MIN_TITLE_LENGTH:
                raise serializers.ValidationError(
                    {"response": "Enter a title longer than " + str(MIN_TITLE_LENGTH) + " characters."})

            body = self.validated_data['body']
            if len(body) < MIN_BODY_LENGTH:
                raise serializers.ValidationError(
                    {"response": "Enter a body longer than " + str(MIN_BODY_LENGTH) + " characters."})

            feedback_post = FeedbackPost(
                author=self.validated_data['author'],
                title=title,
                body=body,
                image=image,
            )

            url = os.path.join(settings.TEMP, str(image))
            storage = FileSystemStorage(location=url)

            with storage.open('', 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
                destination.close()

            # Check image size
            if not is_image_size_valid(url, IMAGE_SIZE_MAX_BYTES):
                os.remove(url)
                raise serializers.ValidationError(
                    {"response": "That image is too large. Images must be less than 2 MB. Try a different image."})

            # Check image aspect ratio
            if not is_image_aspect_ratio_valid(url):
                os.remove(url)
                raise serializers.ValidationError(
                    {"response": "Image height must not exceed image width. Try a different image."})

            os.remove(url)
            feedback_post.save()
            return feedback_post
        except KeyError:
            raise serializers.ValidationError({"response": "You must have a title, some content, and an image."})

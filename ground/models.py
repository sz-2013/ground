# -*- coding: utf-8 -*-
import os
from django.db import models
from imagekit import models as imagekit_models


class ImgModels(models.Model):
    DIRECTORY = ''

    def get_image_path(self, filename):
        return os.path.join(os.path.join('media', self.DIRECTORY), filename)

    class Meta:
        abstract = True

    name = models.CharField(
        max_length=16, unique=True)
    img = imagekit_models.ProcessedImageField(
        upload_to=get_image_path,
        options={"quality": 85}
    )

    def __unicode__(self):
        return self.name


class Background(ImgModels):
    DIRECTORY = 'bg'


class Image(ImgModels):
    DIRECTORY = 'img'
    description = models.TextField()
    bg = models.ForeignKey(Background)

import uuid
import json  # Сугубо из уважения к Ивану. И так как eval == evil

from django.db import models
from typing import (
    List
)


class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    break_length = models.PositiveSmallIntegerField()
    lesson_length = models.PositiveSmallIntegerField()
    lessons_per_day = models.PositiveSmallIntegerField()
    training_days = models.PositiveSmallIntegerField()


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    school_id = models.ForeignKey(School, on_delete=models.SET_NULL)
    full_name = models.CharField(max_length=200)
    work_schedule = models.TextField()

    def get_work_schedule(self) -> List[int]:
        return json.loads(self.work_schedule)["content"]


class Group:
    count = models.PositiveSmallIntegerField()


class Subject:
    name = models.CharField(max_length=200)
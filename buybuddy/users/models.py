from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


@property
def final_cost(self):
    total_cost_sum = self.total_costs.aggregate(
        sum=models.Sum("total_cost"))["sum"]
    if total_cost_sum == None:
        return 0
    else:
        return total_cost_sum

from django.db import models

BREAKFAST = 1
BRUNCH = 2
ELEVENSES = 3
LUNCH = 4
TEA = 5
SUPPER = 6
DINNER = 7

MEAL_TYPE_CHOICES = (
      (BREAKFAST, 'Breakfast'),
      (BRUNCH, 'Brunch'),
      (ELEVENSES, 'Elevenses'),
      (LUNCH, 'Lunch'),
      (TEA, 'Tea'),
      (SUPPER, 'Supper'),
      (DINNER, 'Dinner')
)

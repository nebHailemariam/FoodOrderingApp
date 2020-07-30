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

WAITING = 1
ON_THE_WAY = 2
DELIVERED = 3
FAILED = 4

DELIVERY_STATUS_TYPE = (
      (WAITING, "Waiting for Deliveryman"),
      (ON_THE_WAY, "On the Way"),
      (DELIVERED, "Delivered"),
      (FAILED, "Failed")
)
import myfitnesspal
from myfitnesspal.keyring_utils import get_password_from_keyring
from datetime import date

#getting the current date
today = date.today()


#logging into my fitnesspal and calculating the daily total calories from macros
username = 'dan2001tran@gmail.com'
client = myfitnesspal.Client(username, get_password_from_keyring(username))d

day = client.get_date(today.year, today.month, today.day)

calculatedDailyTotalCalories = day.totals['carbohydrates'] * 4 + day.totals['protein'] * 4 + day.totals['fat'] * 9
print(calculatedDailyTotalCalories)


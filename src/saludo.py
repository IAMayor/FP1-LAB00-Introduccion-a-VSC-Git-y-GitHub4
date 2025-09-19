from datetime import datetime

hora_actual = datetime.now().hour
if hora_actual<12:
    print("Buenos días, Jose Carlos")
elif hora_actual>=12 and hora_actual<20:
    print("Buenas tardes, Jose Carlos")
else:
    print("Buenas noches, Jose Carlos")